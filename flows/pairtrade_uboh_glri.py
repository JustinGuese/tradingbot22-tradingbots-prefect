from pairTrade import pairTrade
from prefect import flow


@flow(log_prints=True)
def pairTradeUBOHGLRI():
    pairTrade("UBOH", "GLRI", 20, 1.0, 1.0)
