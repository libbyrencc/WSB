import alpaca_backtrader_api
import backtrader as bt
from datetime import datetime
import sys 
sys.path.append("..") 

from setting import *


class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)
    def log(self, txt, dt=None):
         dt = dt or self.data.datetime[0]
         dt = bt.num2date(dt)
         print('%s, %s' % (dt.isoformat(), txt))

    def notify_trade(self, trade):
         if not trade.isclosed:
             return

         self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' %
                  (trade.pnl, trade.pnlcomm))

    def notify_order(self, order):
         if order.status in [order.Submitted, order.Accepted]:
             # Buy/Sell order submitted/accepted to/by broker - Nothing to do
             return

         # Check if an order has been completed
         # Attention: broker could reject order if not enough cash
         if order.status in [order.Completed]:
             if order.isbuy():
                 self.log(
                     'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                     (order.executed.price,
                      order.executed.value,
                      order.executed.comm))

                 self.buyprice = order.executed.price
                 self.buycomm = order.executed.comm
             else:  # Sell
                 self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                          (order.executed.price,
                           order.executed.value,
                           order.executed.comm))

             self.bar_executed = len(self)

         elif order.status in [order.Canceled, order.Margin, order.Rejected]:
             self.log('Order Canceled/Margin/Rejected')

         self.order = None
    def notify_store(self, msg, *args, **kwargs):
         super().notify_store(msg, *args, **kwargs)
         self.log(msg)

    def stop(self):
         print('==================================================')
         print('Starting Value - %.2f' % self.broker.startingcash)
         print('Ending   Value - %.2f' % self.broker.getvalue())
         print('==================================================')
         
    def notify_data(self, data, status, *args, **kwargs):
        super().notify_data(data, status, *args, **kwargs)
        print('*' * 5, 'DATA NOTIF:', data._getstatusname(status), *args)
        if data._getstatusname(status) == "LIVE":
            self.live_bars = True