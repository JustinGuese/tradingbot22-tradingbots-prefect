import time
from os import environ

import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from db import AlphaSentiment, AlphaSentimentArticle, Bot, SessionLocal, Trade
from fp.fp import FreeProxy
from googlesearch import search
from openai import OpenAI
from tqdm import tqdm

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
}

client = OpenAI(
    # base_url="http://10.147.17.74:1337/v1",
    # This is the default and can be omitted
    api_key=environ["OPENAI_API_KEY"],
)


NEWSPATH = "../hugo/content/english/news/"


with open("newsTemplate.md", "r") as file:
    newsTemplate = file.read()


def yfLink(ticker):
    return f"<a href='https://finance.yahoo.com/quote/{ticker}' target='_blank'>{ticker}</a>"


def listifyTickers(tickers):
    return ", ".join(yfLink(ticker) for ticker in tickers)


def titlefy(title):
    title = title.replace(" ", "-").replace('"', "").replace("'", "").lower()
    # remove all non alphanumeric characters
    title = "".join([c for c in title if c.isalnum() or c == "-"])
    return title


def getGPTTitle(prompt):
    global client
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "you are a professional finance journalist.",
            },
            {
                "role": "user",
                "content": "create a catchy, seo friendly title based on this summary. just reply with the title, nothing else: "
                + prompt,
            },
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


def getGPTSummary(prompt):
    global client
    messages = [
        {
            "role": "system",
            "content": "you are a professional finance journalist.",
        },
        {
            "role": "user",
            "content": "create a news article based on this information. try to create short paragraphs. reply in markdown. just reply with the article, nothing else. remove promotional content including contact information or anything about the source. you are only writing for ai-investing-bots.com and should not mention competition. content: "
            + prompt,
        },
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


def getGPTTickerReasons(article, tickers):
    global client

    tickerResp = dict()
    for ticker, polarity in tickers:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "assistant",
                    "content": article,
                },
                {
                    "role": "user",
                    "content": f"in this context, reply with a 1-3 sentence reply why the ticker {ticker} will be affected {polarity} by this. if the ticker is not mentioned, just guess that the article is about the ticker. never reply you do not know, or that in this context you cant say why. just guess the reason that it is affected {polarity} from the article. ",
                },
            ],
            model="gpt-3.5-turbo",
        )
        tickerResp[ticker] = chat_completion.choices[0].message.content
    return tickerResp


def tag_visible(element):
    if element.parent.name in [
        "style",
        "script",
        "head",
        "title",
        "meta",
        "[document]",
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, "html.parser")
    texts = soup.find_all(string=True)
    visible_texts = filter(tag_visible, texts)
    return " ".join(t.strip() for t in visible_texts)


def getGoogleHit(source, title, timestamp):
    term = "news " + source + " " + title + " " + timestamp.strftime("%Y-%m-%d")
    content = search(term, num_results=1, advanced=True)
    url = next(content)
    url = url.url

    content = requests.get(url, headers=HEADERS).text
    content = text_from_html(content)
    return title, url, content


def createNews():
    db = SessionLocal()

    allNews = (
        db.query(
            AlphaSentimentArticle.id,
            AlphaSentimentArticle.title,
            AlphaSentimentArticle.timestamp,
            AlphaSentimentArticle.source,
            AlphaSentimentArticle.summary,
            AlphaSentimentArticle.ai_summary,
            AlphaSentimentArticle.ai_title,
            AlphaSentimentArticle.ai_url,
            AlphaSentimentArticle.ai_ticker_reasons,
        )
        .order_by(AlphaSentimentArticle.timestamp.desc())
        .all()
    )
    for news in tqdm(allNews):
        # get all tickers from this article with positive sentiment score
        try:
            positiveTickers = (
                db.query(
                    AlphaSentiment.ticker,
                    AlphaSentiment.article_relevance_score,
                    AlphaSentiment.article_sentiment_score,
                )
                .filter(AlphaSentiment.article_id == news.id)
                .filter(
                    AlphaSentiment.article_sentiment_score > 0
                )  # Filter positive sentiment score
                .order_by(
                    AlphaSentiment.article_sentiment_score.desc()
                )  # Order by sentiment score descending
                .all()
            )
            negativeTickers = (
                db.query(
                    AlphaSentiment.ticker,
                    AlphaSentiment.article_relevance_score,
                    AlphaSentiment.article_sentiment_score,
                )
                .filter(AlphaSentiment.article_id == news.id)
                .filter(
                    AlphaSentiment.article_sentiment_score < 0
                )  # Filter positive sentiment score
                .order_by(
                    AlphaSentiment.article_sentiment_score
                )  # Order by sentiment score descending
                .all()
            )
            if len(positiveTickers) == 0 and len(negativeTickers) == 0:
                continue

            # then get all the bots that have used these tickers
            positiveTickers = [ticker.ticker for ticker in positiveTickers]
            negativeTickers = [ticker.ticker for ticker in negativeTickers]

            allUsedTickers = positiveTickers + negativeTickers

            # check if ai_title is already set
            if (
                news.ai_title is None
                or news.ai_title == ""
                or news.ai_ticker_reasons is None
            ):
                # need to create it
                if news.ai_title is None:
                    title, url, content = getGoogleHit(
                        news.source, news.title, news.timestamp
                    )
                    aisummary = getGPTSummary(news.summary + ". \n" + content)
                    aititle = getGPTTitle(title + " ." + news.summary)
                else:
                    aisummary = news.ai_summary
                    url = news.ai_url
                    aititle = news.ai_title

                tickerReasons = list(
                    zip(
                        allUsedTickers,
                        ["positively" for _ in positiveTickers]
                        + ["negatively" for _ in negativeTickers],
                    )
                )
                tickerReasons = getGPTTickerReasons(aisummary, tickerReasons)

                # update news object
                db.query(AlphaSentimentArticle).filter_by(id=news.id).update(
                    {
                        "ai_title": aititle,
                        "ai_summary": aisummary,
                        "ai_url": url,
                        "ai_ticker_reasons": tickerReasons,
                    }
                )
                db.commit()
                # refresh
                news = db.query(AlphaSentimentArticle).filter_by(id=news.id).first()

            botsUsing = (
                db.query(Trade.bot).filter(Trade.ticker.in_(allUsedTickers)).all()
            )
            botsUsing = list(set([bot.bot for bot in botsUsing]))
            if len(botsUsing) > 0:
                # then we have to get the nicename
                for i in range(len(botsUsing)):
                    nicename = (
                        db.query(Bot.nicename).filter_by(name=botsUsing[i]).first()[0]
                    )
                    if nicename is None:
                        nicename = botsUsing[i]
                    botsUsing[i] = nicename
                # linkify
                botsUsing = [f"[{bot}](/strategies/{bot})" for bot in botsUsing]

            template = newsTemplate
            template = template.replace(
                "{{title}}", news.ai_title.replace('"', "").replace("'", "")
            )
            template = template.replace("{{source}}", news.source)
            template = template.replace(
                "{{crntDate}}", news.timestamp.strftime("%Y-%m-%d %H:%M:%S")
            )
            template = template.replace("{{summary}}", news.ai_summary)
            template = template.replace(
                "{{url}}", f"<a href='{news.ai_url}' target='_blank'>{news.source}</a>"
            )

            # positiveTickersList
            template = template.replace(
                "{{positiveTickersList}}", listifyTickers(positiveTickers)
            )
            # negativeTickersList
            template = template.replace(
                "{{negativeTickersList}}", listifyTickers(negativeTickers)
            )
            # then add the ticker responses
            # positiveTickersMDTable
            positiveTickersMDTable = "| ticker | polarity | why? |\n|------------|------------|------------|\n"
            for ticker in positiveTickers:
                positiveTickersMDTable += (
                    f"| {ticker} | positively | {news.ai_ticker_reasons[ticker]} |\n"
                )
            template = template.replace(
                "{{positiveTickersMDTable}}", positiveTickersMDTable
            )
            # negativeTickersMDTable
            negativeTickersMDTable = ""
            for ticker in negativeTickers:
                negativeTickersMDTable += (
                    f"| {ticker} | negatively | {news.ai_ticker_reasons[ticker]} |\n"
                )
            template = template.replace(
                "{{negativeTickersMDTable}}", negativeTickersMDTable
            )

            # strategis and bots
            if len(botsUsing) > 0:
                template = template.replace("{{strategyList}}", ", ".join(botsUsing))
            else:
                template = template.replace("{{strategyList}}", "None so far...")

            with open(NEWSPATH + titlefy(news.ai_title) + ".md", "w") as file:
                file.write(template)
        except Exception as e:
            print("problem with. skip : ", news.title)
            print(e)
            continue


if __name__ == "__main__":
    createNews()
