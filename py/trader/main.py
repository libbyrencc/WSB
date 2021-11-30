import alpaca_backtrader_api
import backtrader as bt
from datetime import datetime
from strategies.Sma_Rsi import Sma_Rsi_Cross
from strategies.Sma_Rsi import SessionFilter
#from strategies.Simple_Sma import SmaCross


#import 

from backtrader import strategy


# Your credentials here
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
symbol = "TSLA"
begindate=datetime(2021, 5, 1,9,30)
enddate=datetime(2021, 11, 15,9,30)
bt_timeframe=bt.TimeFrame.Minutes
strategy_main=Sma_Rsi_Cross

if __name__ == '__main__':
    import logging
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    cerebro = bt.Cerebro()
    cerebro.addstrategy(strategy_main)
    store = alpaca_backtrader_api.AlpacaStore(
        key_id=ALPACA_API_KEY,
        secret_key=ALPACA_SECRET_KEY,
        paper=not IS_LIVE,
    )

    DataFactory = store.getdata  # or use alpaca_backtrader_api.AlpacaData
    if IS_BACKTEST:
        data0 = DataFactory(dataname=symbol, historical=True,
                            fromdate=begindate,
                            todate=enddate,
                            timeframe=bt_timeframe,
                            data_feed='CTA')

    else:
        data0 = DataFactory(dataname=symbol,
                            historical=False,
                            timeframe=bt.TimeFrame.Ticks,
                            backfill_start=False,
                            data_feed='CTA')
        # or just alpaca_backtrader_api.AlpacaBroker()
        broker = store.getbroker()
        cerebro.setbroker(broker)
    data0.addfilter(SessionFilter)
    cerebro.adddata(data0)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name = 'SharpeRatio')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='DW')
    if IS_BACKTEST:
        # backtrader broker set initial simulated cash
        cerebro.broker.setcash(100000.0)

    #cerebro.run()
    result=cerebro.run()
    #strat=result[0]
    #print('Sharpe ratio:', strat.analyzers.SharpeRatio.get_analysis())
    #cerebro.plot(iplot=False)