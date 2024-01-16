from pairTrade import pairTrade
from prefect import flow


@flow(log_prints=True)
def pairTradeGLRIVSTM():
    pairTrade("GLRI", "VSTM")
