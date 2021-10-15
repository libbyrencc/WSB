PIC 16B Project

# Tic-Tac-Toe
. . .
. x .
. . o


# Project Proposal

## Abstract

This project will help people to predict the trend of the stock market in a short time (Day) and take advantage of that to trade. This algorithm will include some basic trading strategies. During the trading, we will use machine learning tools to improve the algorithm in order to adapt to the current stock market.

## Planned Deliverables

The stuff we are trying to make is a program that will get the stock market data, analyze the data, and predict the future price trend in a short time. Then, we make decisions to open an order to buy or short some amount of stocks, and close positions when the program thinks it is right.

* “Full success.” 

If everything works out for us exactly as you plan, the program runs properly, making ideal predictions, and will post orders to our paper trading brokerage account. And have profit not only in the backtesting but also in real-time trading. Last, our algorithm will be deliverable.

* “Partial success.” 

If things don’t 100% work out, which means that the algorithm is not making a profit in the real-time market, but in backtesting, it will predict the stock price with a success rate > 50% in the future 5-30 mins. However, in the stock trading strategy, we have another solution which is called the public opinion trading system, which is to follow some government policies or some market sentiment of shareholders to trade.

## Resources Required

1. Stock market data (both historical and real-time) from Alpaca:

https://github.com/alpacahq/alpaca-trade-api-python

2. The algorithm trading platform from Alpaca (paper trading):

https://alpaca.markets/

## Tools and Skills Required

* `**Skill**`: Machine learning, Linear Regression, Data-visualization DNN

* **Python packages**: SQLite3,Tstable, scikit-learn


## What You Will Learn

The things we will learn by completing this project:

* Exploring Rolling Mean and Return Rate of Stocks
 
* Return Deviation — to determine risk and return
 
* Correlation Analysis — Does one competitor affect others?
 
Three machine learning models we may use to predict our stocks:

* Simple Linear Analysis
* Quadratic Discriminant Analysis (QDA)
* K Nearest Neighbor (KNN)

## Risks

The models we train may only have good predictive accuracy in certain situations, but in real trading, their accuracy may be really low, and the degree of difference between the models is low either.
 
One of the biggest problems in finance is the inability to quantify historical financial data. For example, for stock data, the most commonly used method is the K-chart, which contains four price data: high price, low price, open price, and close price. But beyond those four basic prices, all the data is likely to be supplemented by our imaginations.
 
Besides, The complete stock forecasting problem is very complicated because various factors have different scales of influence on the final price:
 
1. Both high-frequency trading and algorithmic trading are carried out in a very short period of time (the interval is generally less than 1 day), so they are the main factors affecting price changes;
2. Both opening and closing prices have their own calculation models -- whether in stocks or futures;
3. Company news and rumors are very important drivers of stock trading. Specific company news happens all the time, but it doesn't come to you. So if you can follow the news in real time, or even know it in advance, it's a very good source of data for your stock trading.
4. It is important to find some business cycles for investing in price movements over many years. For example, the cyclical volatility of pharmaceutical stocks.

## Ethics
 
**Should this app exist?**
 
In our opinion, this app should exist. For sure, people who profit from the stock market through our models have the potential to benefit from the existence of our product. At the same time, someone's going to make money means someone's going to lose money, and those who lose money have the potential to be harmed from the existence of our product.

In our perspective, the world will become an overall better place because of the existence of our product? I take two examples to illustrate it.

* People do not have to spend time doing some mechanical repetitive operations so that they can work efficiently.
 
* Correspondingly prevent the internal personnel of stock companies to make use of their own authority to operate the abnormal trading behavior, carrying out financial fraud.

## Tentative Timeline

**Week 3**: Building programs that could get data from API and orders can be transmitted to the trading platform

**Week 4-5**: Data analysis 

**Week 6-7**: Running some basic trading strategies

**Week 7-10**: Improve trading strategy by machine learning
