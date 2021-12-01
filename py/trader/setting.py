# -*- coding: utf-8 -*-
import alpaca_backtrader_api
import backtrader as bt
from datetime import datetime
from backtrader import strategy

ALPACA_API_KEY = "PK8SSSXD3FX164IYREJ5"
ALPACA_SECRET_KEY = "NPKEgtQyt3fsRodbOqn4d46V19XI5W9S8Cv64dDT"

"""
3 options:
 - backtest (IS_BACKTEST=True, IS_LIVE=False)
 - paper trade (IS_BACKTEST=False, IS_LIVE=False)
 - live trade (IS_BACKTEST=False, IS_LIVE=True)
"""

IS_BACKTEST = True
IS_LIVE = False
symbol = "XPEV"
begindate=datetime(2021, 1, 1,9,30)
enddate=datetime(2021, 11, 30,9,30)
bt_timeframe=bt.TimeFrame.Minutes

from strategies.Sma_Rsi import *
#from strategies.Simple_Sma import *
from strategies.macd_cross import *
from strategies.Sma_Rsi_long_only import *

strategy_main=Sma_Rsi_Cross_long

