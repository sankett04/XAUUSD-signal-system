import yfinance as yf
import pandas_ta as ta

def get_dxy_data():
    data = yf.Ticker("DX-Y.NYB").history(period="12mo", interval="1h")

    if data.empty or "Close" not in data.columns:
        print("⚠️ Failed to fetch DXY data")
        return None

    data["ema_50"] = ta.ema(data["Close"], length=50)
    data["rsi"] = ta.rsi(data["Close"], length=14)

    return data.dropna()
