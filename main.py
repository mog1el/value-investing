import yfinance as yf
#%%
def check_stock_criteria(symbol):
    stock = yf.Ticker(symbol)
    market = yf.Ticker("SPY")
    stock_info = stock.info
    price = stock_info.get('currentPrice', None)
    print(f"Price: ${price}")
    EPS = stock_info.get('trailingEps', None)
    PE = round(price / EPS, 4)
    print(f"P/E: {PE}")
    market_info = market.info
    marketPE = market_info.get('trailingPE', None)
    print(f"Market P/E: {marketPE}")
    stock_dividend_yield = stock_info.get('dividendYield', None)
    print(f"Dividend Yield: {stock_dividend_yield}")
    stock_dividend_yield_1y = round(stock_info.get('trailingAnnualDividendYield', None), 4)
    print(f"1y average dividend yield: {stock_dividend_yield_1y}")
    dividends = stock.dividends
    stock_dividend_yield_5y = round(dividends.tail(5).mean() / price, 4)
    print(f"5y average dividend yield: {stock_dividend_yield_5y}")

    #%%
    balance_sheet = stock.balance_sheet
    #print(balance_sheet) I have to make total assets/total liabilities > 1

    #%%
    #Operating income/Total revenue > 15

    #%%
    if (PE < marketPE and
            stock_dividend_yield > stock_dividend_yield_1y and
            stock_dividend_yield_1y > stock_dividend_yield_5y):
        return True
    else:
        return False
#%%
stock = input("Enter stock symbol: ")
if check_stock_criteria(stock):
    print(f"{stock} is porfect!")
else:
    print(f"{stock} is NOT porfect!")
