To run the trader, type `python main.py > output.txt` in the command line.

And edit  `setting.py` to initialize some IMPORTANT data::

In `setting.py`

Three options:
 - backtest (IS_BACKTEST=True, IS_LIVE=False)
 - paper trade (IS_BACKTEST=False, IS_LIVE=False)
 - live trade (IS_BACKTEST=False, IS_LIVE=True)


IS_BACKTEST = True            #see information above
IS_LIVE = False               #see inofrmation above
symbol = "TSLA"               #stock ticker
begindate=datetime(2021, 9, 1,9,30)      #start time if is backtest
enddate=datetime(2021, 11, 15,9,30)      #end time if is backtest
bt_timeframe=bt.TimeFrame.Minutes       #min time inteval

```
py
│   predictor.py
│   __init__.py
│   
└───trader
    │   main.py	                  ----main python file
    │   setting.py                ----use to set target 'startdate','stock ticker'....
    │   __init__.py
    │   
    ├───analyzers                 ----analyzer for backtesting
    │           
    ├───strategies               ----store strategies
```

