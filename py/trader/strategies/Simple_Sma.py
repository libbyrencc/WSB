import alpaca_backtrader_api
import backtrader as bt
from datetime import datetime

ALPACA_API_KEY ="PK8SSSXD3FX164IYREJ5"
ALPACA_SECRET_KEY ="NPKEgtQyt3fsRodbOqn4d46V19XI5W9S8Cv64dDT"
ALPACA_PAPER = True

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)
    