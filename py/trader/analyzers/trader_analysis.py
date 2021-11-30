def printTradeAnalysis(analyzer):
    '''
    Function to print the Technical Analysis results in a nice format.
    '''
    #Get the results we are interested in
    total_open = analyzer.total.open
    total_closed = analyzer.total.closed
    total_won = analyzer.won.total
    total_lost = analyzer.lost.total
    win_streak = analyzer.streak.won.longest
    lose_streak = analyzer.streak.lost.longest
    pnl_net = round(analyzer.pnl.net.total,2)
    strike_rate = (total_won / total_closed) * 100
    print("Trade Analysis Results:")
    print("    Total Closed:  ",total_closed)
    print("    Total Won:  ",total_won)
    print("    Total Lost:  ",total_lost)
    print("    Pnl_Net:  ",pnl_net)
#source: https://backtest-rookies.com/2017/06/11/using-analyzers-backtrader/