def labelToSignal(df):
    signal = []
    crntSig = 0
    if "Up Trend" not in df.columns or "Down Trend" not in df.columns:
        print("Up Trend or Down Trend not in columns: ", df.columns)
        if "Up Trend" not in df.columns:
            df["Up Trend"] = "n"
        if "Down Trend" not in df.columns:
            df["Down Trend"] = "n"
    elif "Up Trend" not in df.columns and "Down Trend" not in df.columns:
        raise ValueError("Up Trend and Down Trend not in columns")
    for i in range(len(df)):

        if df["Up Trend"][i] == "n" and df["Down Trend"][i] == "n":
            # look into future, which is the one label that is not "n"
            nextSig = None
            for j in range(i, len(df)):
                if df["Up Trend"][j] != "n" or df["Down Trend"][j] != "n":
                    if df["Close"][j] > df["Close"][i]:
                        nextSig = 1
                    else:
                        nextSig = -1
                    break
            if nextSig is None:
                # print("next sig is none at ", i, j)
                nextSig = 0
            else:
                crntSig = nextSig
        if df["Up Trend"][i] != "n":
            crntSig = 1
        elif df["Down Trend"][i] != "n":
            crntSig = -1
        signal.append(crntSig)
    return signal
