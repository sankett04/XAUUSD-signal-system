import streamlit as st
import requests

# -----------------------
# Config
# -----------------------
API_URL = "http://localhost:5000/api/checklist"  # Change if hosted elsewhere

st.set_page_config(page_title="Gold Buy Signal Checker", layout="centered")

# -----------------------
# App UI
# -----------------------
st.title("📈 Gold Buy Signal Checklist")

with st.spinner("Fetching latest market data..."):
    try:
        response = requests.get(API_URL)
        data = response.json()
    except Exception as e:
        st.error("Failed to connect to backend API.")
        st.stop()

# -----------------------
# Display Rules
# -----------------------
st.subheader("Checklist Evaluation")

rules = {
    "DXY is below 50 EMA": data.get("dxy_below_50ema"),
    "RSI on DXY < 40 (weak momentum)": data.get("dxy_rsi_weak"),
    "Fed is expected to cut rates next meeting": data.get("fed_cut_expected"),
    "US CPI and NFP data are weakening": data.get("cpi_nfp_weakening"),
    "Gold bouncing from 200 EMA": data.get("xau_bounce_200ema"),
    "MACD crossover on Gold": data.get("xau_macd_crossover"),
}

for rule, passed in rules.items():
    st.write(f"✅ {rule}" if passed else f"❌ {rule}")

# -----------------------
# Score and Signal
# -----------------------
score = data.get("score", 0)
signal = data.get("signal", "WAIT")

st.markdown("---")
st.markdown(f"### 🔢 **Total Signals Met:** `{score}/6`")
st.markdown(f"### 🚦 **Gold Trading Signal:** `{signal}`")

if signal == "BUY":
    st.success("High probability BUY opportunity on Gold (XAU/USD)")
else:
    st.info("Conditions not strong enough. Better to WAIT.")

