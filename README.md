# XAUUSD-signal-system

# 🟡 Gold Buy Signal System (XAU/USD)

A full-stack trading assistant that evaluates a checklist of macroeconomic and technical signals to determine whether it's a good time to BUY gold (XAU/USD).

Built with:
- 🔙 Flask REST API (deployed on Render)
- 🔼 Streamlit Frontend (deployed on Streamlit Cloud)
- 📡 External data from TradingEconomics, FRED, Yahoo Finance


## 📊 Features

- Live checklist of 6 gold trading conditions:
  - DXY below 50 EMA
  - DXY RSI < 40
  - Fed rate cut expectation
  - Weakening CPI/NFP data
  - 200 EMA bounce for gold
  - MACD crossover for gold
- Composite score + signal: **BUY** or **WAIT**
- Real-time data fetching from financial APIs

---


## 🚀 Live Demos

- 🔼View App[](https://goldsignalsystem.streamlit.app/)
-

## 🛠️ Requirements

* `Flask`, `Flask-CORS`
* `requests`, `yfinance`, `pandas_ta`
* `numpy==1.24.4`
* `gunicorn` (for Render)
* `streamlit` (for frontend)
* `python-dotenv` (for loading API keys locally)

---

## 📌 TODO / Improvements

* Add fallback logic if APIs fail
* Add auth/token system for API
* Optional: add email alert for “BUY” signal

---

## 🧠 Author

**Sanket Talele**
🌐 [GitHub](https://github.com/sankett04)

---

## 📜 License

This project is open-source under the MIT License.




