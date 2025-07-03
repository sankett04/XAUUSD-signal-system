import yfinance as yf
import pandas_ta as ta

def get_gold_data():
    # Use longer period to ensure enough data for 200 EMA and MACD
    data = yf.Ticker("GC=F").history(period="60d", interval="15m")

    if data.empty or "Close" not in data.columns:
        print("⚠️ Failed to fetch Gold (XAU/USD) data")
        return None

    # Add 200 EMA
    data["ema_200"] = ta.ema(data["Close"], length=200)

    # Add MACD
    macd = ta.macd(data["Close"])
    if macd is not None:
        data["macd"] = macd["MACD_12_26_9"]
        data["macd_signal"] = macd["MACDs_12_26_9"]
    else:
        print("⚠️ Failed to calculate MACD")
        return None

    return data.dropna()
