# MacMenuBar: Custom SwiftBar Stock Tracker

This project integrates a Python-based stock ticker plugin into the macOS menu bar using [SwiftBar](https://github.com/swiftbar/SwiftBar). It includes:

- `SwiftBarPlugins/stockbar.1m.py`: A lightweight plugin that fetches real-time stock data via `yfinance`
- `SwiftBarPlugins/config.yaml`: A config file that lists the tracked ticker symbols
- `stockbar-ui/main.py`: A tkinter-based GUI to edit the ticker config

---

## 🔧 Requirements

- macOS (tested on macOS 15.5+)
- [Xcode](https://apps.apple.com/us/app/xcode/id497799835) (to build SwiftBar, optional)
- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
- Homebrew-installed `tcl-tk` (for the tkinter UI):
  ```bash
  brew install tcl-tk
  ```

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/MacMenuBar.git
cd MacMenuBar
```

### 2. Create Python environments

```bash
pyenv virtualenv 3.13.5 swiftbar-plugins-env
pyenv virtualenv 3.13.5 stockbar-ui-env
```

### 3. Install dependencies

```bash
pyenv activate swiftbar-plugins-env
pip install -r SwiftBarPlugins/requirements.txt

pyenv activate stockbar-ui-env
pip install -r stockbar-ui/requirements.txt
```

---

## 🏃‍♂️ Running the App

### SwiftBar

1. Open `SwiftBar.xcodeproj` in Xcode
2. Build and run the SwiftBar app
3. Set the **Plugin Folder** to:
   ```
   ~/Workspace/MacMenuBar/SwiftBarPlugins/
   ```

### Stockbar UI

```bash
cd stockbar-ui
pyenv activate stockbar-ui-env
python main.py
```

---

## 📁 Project Layout

```
MacMenuBar/
├── SwiftBar/                 # SwiftBar source code
├── SwiftBarPlugins/          # Live Python plugin + config
│   └── stockbar.1m.py
│   └── config.yaml
├── stockbar-ui/              # Standalone UI editor
│   └── main.py
├── PROJECT-README.md         # <— YOU ARE HERE
├── macmenubar.code-workspace
```

---

## 💬 Questions?

Maintainer: @shakeNbake312
