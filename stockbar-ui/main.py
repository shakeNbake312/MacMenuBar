# Import standard libraries
import os
import tkinter as tk
from tkinter import messagebox, simpledialog
import yaml  # Third-party library for reading/writing YAML

# -----------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------

# Define the path to config.yaml used by the SwiftBar plugin
# This assumes config.yaml is located in: ../SwiftBarPlugins/config.yaml
CONFIG_PATH = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "SwiftBarPlugins", "config.yaml"
))

# -----------------------------------------------------
# UTILITY FUNCTIONS
# -----------------------------------------------------

def load_symbols():
    """
    Load the stock symbols from the config.yaml file.
    Returns a list of symbols (e.g., ['AAPL', 'TSLA']).
    If the file doesn't exist or is invalid, returns an empty list.
    """
    if not os.path.exists(CONFIG_PATH):
        return []
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f) or {}
    return config.get("symbols", [])

def save_symbols(symbols):
    """
    Save the given list of stock symbols to config.yaml.
    This will overwrite the entire file with a single 'symbols' key.
    """
    with open(CONFIG_PATH, "w") as f:
        yaml.dump({"symbols": symbols}, f)

# -----------------------------------------------------
# CALLBACK FUNCTIONS FOR BUTTONS
# -----------------------------------------------------

def add_symbol():
    """
    Prompt the user to input a new stock symbol.
    If valid and not a duplicate, add it to the list and update the UI.
    """
    symbol = simpledialog.askstring("Add Symbol", "Enter stock symbol:")
    if symbol:
        symbol = symbol.strip().upper()
        if symbol in symbols:
            messagebox.showinfo("Info", f"{symbol} is already in the list.")
        else:
            symbols.append(symbol)
            update_listbox()

def remove_selected():
    """
    Remove the currently selected symbol(s) from the list.
    Supports multi-select removal.
    """
    selected = listbox.curselection()
    if not selected:
        return
    # Reverse iteration to safely delete by index
    for index in reversed(selected):
        del symbols[index]
    update_listbox()

def update_listbox():
    """
    Clear and repopulate the listbox with the current symbol list.
    """
    listbox.delete(0, tk.END)
    for symbol in symbols:
        listbox.insert(tk.END, symbol)

def save_and_exit():
    """
    Save the current symbol list to config.yaml and close the app.
    """
    save_symbols(symbols)
    root.destroy()

# -----------------------------------------------------
# GUI SETUP
# -----------------------------------------------------

# Load current list of symbols
symbols = load_symbols()

# Initialize the root Tkinter window
root = tk.Tk()
root.title("StockBar Config Editor")

# Create and pack the listbox to show current symbols
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=30)
listbox.pack(padx=10, pady=10)

# Populate the listbox with existing symbols
update_listbox()

# Create a button frame for Add/Remove buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

# Add buttons to the frame
tk.Button(btn_frame, text="Add Symbol", command=add_symbol).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Remove Selected", command=remove_selected).grid(row=0, column=1, padx=5)

# Add a Save and Exit button below the frame
tk.Button(root, text="Save and Exit", command=save_and_exit).pack(pady=(0, 10))

# Start the main GUI event loop
root.mainloop()
