#!/Users/dino/.pyenv/versions/swiftbar-plugins-env/bin/python3

# Import standard libraries
import os

# Import third-party packages
import yaml  # For reading YAML config files
import yfinance as yf  # For fetching real-time stock data

# Path to the config file (same directory as this script)
CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.yaml"))


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
    # Load the list of stock symbols from config.yaml
    symbols = load_symbols()

    # If no symbols are configured, show a fallback message in the menu bar
    if not symbols:
        print("📉 No symbols configured")
        return

    # --------------------------------------------
    # Initialize output containers:
    # - output_lines: formatted dropdown entries with color
    # - menu_symbols: compact summary with emoji for menu bar
    # --------------------------------------------
    output_lines = []
    menu_symbols = []

    # Loop through each configured ticker symbol
    for symbol in symbols:
        try:
            # Use yfinance to fetch intraday data for the current day
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d")

            # If no data is available, handle gracefully
            if hist.empty:
                output_lines.append(f"{symbol}: no data")
                menu_symbols.append(f"⚪ {symbol}")
                continue

            # Extract most recent closing price and today's open
            current = hist["Close"].iloc[-1]
            open_price = hist["Open"].iloc[0]

            # Calculate percent change since market open
            change = ((current - open_price) / open_price) * 100

            # --------------------------------------------
            # Determine visual indicators:
            # - Dropdown color (using SwiftBar's color tag)
            # - Emoji icon for menu bar
            # --------------------------------------------
            if change > 0:
                color = "#00cc00"  # green
                emoji = "🟢"
            elif change < 0:
                color = "#cc0000"  # red
                emoji = "🔴"
            else:
                color = "#cccccc"  # gray (no movement)
                emoji = "⚪"

            # Format dropdown line with price and percent change + color
            dropdown_line = f"{symbol} {current:.0f} ({change:+.2f}%) | color={color}"
            output_lines.append(dropdown_line)

            # Format menu bar entry
            menu_symbols.append(f"{emoji} {symbol} {current:.0f} ({change:+.2f}%)")


        except Exception:
            # Handle unexpected errors during data fetch
            output_lines.append(f"{symbol}: error")
            menu_symbols.append(f"⚠️ {symbol}")

    # --------------------------------------------
    # MENU BAR OUTPUT (top line)
    # - Combine all emoji-enhanced ticker lines into one string
    # - This line is shown in the menu bar
    # - Must NOT include SwiftBar metadata (like "| color")
    # --------------------------------------------
    print("  ".join(menu_symbols))

    # --------------------------------------------
    # DROPDOWN OUTPUT (lines after '---')
    # - Each line includes price + percent change with color styling
    # --------------------------------------------
    print("---")
    for line in output_lines:
        print(line)


# Only run if this script is executed directly (standard Python entry point)
if __name__ == "__main__":
    main()
