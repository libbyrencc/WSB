from setting import *

from analyzers.trader_analysis import printTradeAnalysis
#IS_BACKTEST = True
#IS_LIVE = False 
#symbol = "TSLA"
#begindate=datetime(2021, 5, 1,9,30)
#enddate=datetime(2021, 11, 15,9,30)
#bt_timeframe=bt.TimeFrame.Minutes



if __name__ == '__main__':
    import logging
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
    cerebro = bt.Cerebro()
    #setting strategy
    cerebro.addstrategy(strategy_main)
    store = alpaca_backtrader_api.AlpacaStore(
        key_id=ALPACA_API_KEY,
        secret_key=ALPACA_SECRET_KEY,
        paper=not IS_LIVE,
    )

    #Produce data from alpaca_api
    DataFactory = store.getdata
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
        
        broker = store.getbroker()
        cerebro.setbroker(broker)
    #only trade during regular session
    data0.addfilter(SessionFilter)
    cerebro.adddata(data0)
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
    if IS_BACKTEST:
        cerebro.broker.setcash(100000.0)


    result=cerebro.run()
    strat=result[0]
    #analysis data
    printTradeAnalysis(strat.analyzers.ta.get_analysis())
    #plot for vis
    cerebro.plot(iplot= False)