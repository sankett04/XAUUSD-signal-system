# XAUUSD-signal-system

# 🟡 Gold Buy Signal System (XAU/USD)

A full-stack trading assistant that evaluates a checklist of macroeconomic and technical signals to determine whether it's a good time to BUY gold (XAU/USD).

Built with:
- 🔙 Flask REST API (deployed on Render)
- 🔼 Streamlit Frontend (deployed on Streamlit Cloud)
- 📡 External data from TradingEconomics, FRED, Yahoo Finance

---

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

## 🧠 Project Structure

