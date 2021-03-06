
import sys 
sys.path.append("..") 

from setting import *

class SessionFilter(object):
    def __init__(self, data):
        pass
    def __call__(self, data):
        if data.p.sessionstart <= data.datetime.time() <= data.p.sessionend:
            return False  
        data.backwards()  
        return True 
class Sma_Rsi_Cross(bt.Strategy):
    params = dict(
        pfast=5,  # period for the fast moving average
        pslow=15,   # period for the slow moving average
        rsi_per=14,
        rsi_upper=60.0,
        rsi_lower=40.0,
        rsi_out=50.0,
        warmup=35
    )

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
            
            return
        if order.status in [order.Completed]:
            self.startValue=self.broker.getvalue()
            self.prePrice=self.dataclose[0]
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
                self.shortprice = order.executed.price
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

    def __init__(self):
        self.live_bars = False
        self.dataclose = self.datas[0].close
        #add indicate here
        sma1 = bt.ind.SMA(self.data0, period=self.p.pfast)
        sma2 = bt.ind.SMA(self.data0, period=self.p.pslow)
         #not plot all lines or the vis will be too big
        self.crossover = bt.ind.CrossOver(sma1, sma2,plotskip=True)

        rsi = bt.indicators.RSI(period=self.p.rsi_per,
                                upperband=self.p.rsi_upper,
                                lowerband=self.p.rsi_lower,plotskip=True)

        self.crossdown = bt.ind.CrossDown(rsi, self.p.rsi_upper,plotskip=True)
        self.crossup = bt.ind.CrossUp(rsi, self.p.rsi_lower,plotskip=True)

    def notify_data(self, data, status, *args, **kwargs):
        super().notify_data(data, status, *args, **kwargs)
        print('*' * 5, 'DATA NOTIF:', data._getstatusname(status), *args)
        if data._getstatusname(status) == "LIVE":
            self.live_bars = True

    def next(self):
        if not self.live_bars and not IS_BACKTEST:
            return
        #if we do not have positions
        if not self.position:
            if self.crossover > 0 or self.crossup > 0:
                #open long position
                self.buy(size=(self.broker.get_cash()*0.95//self.data.close[0]))  
            if self.crossover <= 0 and self.crossup < 0:
                #open short position
                self.sell(size=(self.broker.get_cash()*0.95//self.data.close[0])) 
        
        #if we have short positions
        if self.position.size <0:
            condition = (self.dataclose[0] - self.prePrice) / self.dataclose[0]
            # stop loss/ take profit
            if condition > 0.05 or condition < -0.01:
               self.order = self.close()
            #the indicator's change
            if self.crossover > 0 or self.crossup > 0:
                self.order=self.close()
         #if we have long positions
        if self.position.size >0:
            condition = -(self.dataclose[0] - self.prePrice) / self.dataclose[0]
            # stop loss/ take profit
            if condition > 0.05 or condition < -0.01:
               self.order = self.close()
               #the indicator's change
            if self.crossover <= 0 or self.crossup < 0:
                self.order=self.close()
        