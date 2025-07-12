#!/Users/dino/.pyenv/versions/swiftbar-plugins-env/bin/python3

import yfinance as yf

SYMBOL = "AAPL"

def main():
    stock = yf.Ticker(SYMBOL)
    hist = stock.history(period="1d")

    if hist.empty:
        print("📉 Data error")
        return

    current = hist["Close"].iloc[-1]
    open_price = hist["Open"].iloc[0]
    change = ((current - open_price) / open_price) * 100

    print(f"{SYMBOL}: ${current:.2f} ({change:+.2f}%)")
    print("---")
    print("Click to open Yahoo Finance | href=https://finance.yahoo.com/quote/AAPL")

if __name__ == "__main__":
    main()
