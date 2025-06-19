import requests
import os
if not os.environ.get("RENDER"):
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("dotenv not available; skipping .env load")

def is_fed_expected_to_cut():
    """
    Forecast if the Fed is expected to cut based on CME FedWatch Tool data.
    """
    try:
        # CME FedWatch scraper (no API needed)
        url = "https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        # If using headless browser or Selenium, you could parse the actual rate cut probability
        # For now, use placeholder logic as parsing is complex due to JS rendering
        # Simplified alternative: fallback to latest rate data from FRED
        FRED_API_KEY = os.getenv("FRED_API_KEY")
        fred_url = f"https://api.stlouisfed.org/fred/series/observations?series_id=FEDFUNDS&api_key={FRED_API_KEY}&file_type=json"
        fred_response = requests.get(fred_url)
        data = fred_response.json()

        observations = data.get("observations", [])
        latest_valid = next((obs for obs in reversed(observations) if obs["value"] not in ("", ".")), None)
        if not latest_valid:
            return False

        fed_funds_rate = float(latest_valid["value"])
        return fed_funds_rate < 4.0  # Still a basic check fallback

    except Exception as e:
        print("Fed expectation fetch error:", e)
        return False


def is_cpi_nfp_weakening():
    """
    Forecast CPI/NFP weakening using forecast vs previous values from TradingEconomics.
    """
    try:
        API_KEY = os.getenv("TRADE_ECONOMICS_API_KEY")
        headers = {"Accept": "application/json"}

        # CPI Forecast
        forecast_cpi_url = f"https://api.tradingeconomics.com/forecast/country/united states/indicator/cpi?c={API_KEY}"
        forecast_cpi_data = requests.get(forecast_cpi_url, headers=headers).json()
        forecast_cpi = float(forecast_cpi_data[0]["Forecast"]) if forecast_cpi_data else None

        cpi_url = f"https://api.tradingeconomics.com/historical/country/united states/indicator/cpi?c={API_KEY}"
        actual_cpi_data = requests.get(cpi_url, headers=headers).json()
        actual_cpi = float(actual_cpi_data[0]["Value"]) if actual_cpi_data else None

        cpi_weak = forecast_cpi is not None and actual_cpi is not None and forecast_cpi < actual_cpi

        # NFP Forecast
        forecast_nfp_url = f"https://api.tradingeconomics.com/forecast/country/united states/indicator/non farm payrolls?c={API_KEY}"
        forecast_nfp_data = requests.get(forecast_nfp_url, headers=headers).json()
        forecast_nfp = float(forecast_nfp_data[0]["Forecast"]) if forecast_nfp_data else None

        nfp_url = f"https://api.tradingeconomics.com/historical/country/united states/indicator/non farm payrolls?c={API_KEY}"
        actual_nfp_data = requests.get(nfp_url, headers=headers).json()
        actual_nfp = float(actual_nfp_data[0]["Value"]) if actual_nfp_data else None

        nfp_weak = forecast_nfp is not None and actual_nfp is not None and forecast_nfp < actual_nfp

        return cpi_weak or nfp_weak

    except Exception as e:
        print("CPI/NFP data error:", e)
        return False
