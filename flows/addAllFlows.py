from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        "https://github.com/JustinGuese/tradingbot22-tradingbots-prefect.git",
        entrypoint="flows/headAndShoulders/headShoulderPrefect.py:headAndShoulderPrefect",
    ).deploy(
        name="headAndShoulderPrefect",
        work_pool_name="local-process",
        image="guestros/tradingbot-prefect-agent:latest",
    )
