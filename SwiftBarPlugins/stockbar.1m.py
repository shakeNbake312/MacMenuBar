#!/Users/dino/.pyenv/versions/swiftbar-plugins-env/bin/python3

# Import standard libraries
import os

# Import third-party packages
import yaml  # For reading YAML config files
import yfinance as yf  # For fetching real-time stock data

# Path to the config file (same directory as this script)
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")

def load_symbols():
    """
    Load stock symbols from the config.yaml file.
    Returns a list of symbols (e.g., ['AAPL', 'TSLA', 'MSFT']).
    If the file is missing or invalid, returns an empty list.
    """
    try:
        with open(CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f)  # Parse the YAML content
        return config.get("symbols", [])  # Fallback to empty list
    except Exception as e:
        # If anything goes wrong, show a warning and return []
        print("⚠️ Error reading config")
        print("---")
        print(str(e))
        return []

def main():
    """
    Main SwiftBar plugin logic:
    - Reads symbols from config
    - Prints header and stock data for each symbol
    - Output is picked up by SwiftBar and displayed in the menu bar
    """
    symbols = load_symbols()

    if not symbols:
        # If no symbols are configured, show a fallback
        print("📉 No symbols configured")
        return

    # Show number of tracked symbols in the menu bar
    print(f"🧾 {len(symbols)}")
    print("---")  # SwiftBar syntax: separates the dropdown from the title

    for symbol in symbols:
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d")  # Get today's open/close data

            if hist.empty:
                print(f"{symbol}: no data")
                continue

            current = hist["Close"].iloc[-1]  # Latest price
            open_price = hist["Open"].iloc[0]  # Opening price
            change = ((current - open_price) / open_price) * 100  # Percent change

            # Display: e.g., AAPL: $192.34 (+1.23%)
            print(f"{symbol}: ${current:.2f} ({change:+.2f}%)")
        except Exception as e:
            # If there's a problem with this symbol, display the error
            print(f"{symbol}: error")
            print(f"-- {e}")

# Only run if this script is executed directly (standard Python entry point)
if __name__ == "__main__":
    main()
