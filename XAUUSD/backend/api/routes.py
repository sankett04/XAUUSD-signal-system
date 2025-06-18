from flask import Blueprint, jsonify
from api.gold import get_gold_data
from api.dxy import get_dxy_data
from api.events import is_fed_expected_to_cut, is_cpi_nfp_weakening

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route("/api/checklist")
def get_checklist():
    dxy = get_dxy_data()
    xau = get_gold_data()
    latest_dxy = dxy.iloc[-1]
    latest_xau = xau.iloc[-1]

    rules = {
        "dxy_below_50ema": bool(latest_dxy["Close"] < latest_dxy["ema_50"]),
        "dxy_rsi_weak": bool(latest_dxy["rsi"] < 40),
        "fed_cut_expected": bool(is_fed_expected_to_cut()),
        "cpi_nfp_weakening": bool(is_cpi_nfp_weakening()),
        "xau_bounce_200ema": bool(latest_xau["Close"] > latest_xau["ema_200"]),
        "xau_macd_crossover": bool(
            xau["macd"].iloc[-2] < xau["macd_signal"].iloc[-2] and
            xau["macd"].iloc[-1] > xau["macd_signal"].iloc[-1]
        )
    }

    # Convert to standard Python types
    rules["score"] = int(sum(rules.values()))
    rules["signal"] = "BUY" if rules["score"] >= 3 else "WAIT"

    return jsonify(rules)
