import json
from datetime import datetime

import pytz
import requests

ALPHAVANTAGE_API_KEY = "2QVPVABKG30QMEMW"


def convert(value: float, currency_from: str, currency_to: str) -> float:

    response: requests.Response = requests.get(
        f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency_from}&to_currency={currency_to}&apikey={ALPHAVANTAGE_API_KEY}"
    )
    result: dict = response.json()

    obj = datetime.now()
    tz = pytz.timezone("Europe/Kiev")
    new_obj = tz.localize(obj)

    new_data = (
        {
            "currency_from": currency_from,
            "currency_to": currency_to,
            "rate": result["Realtime Currency Exchange Rate"]["5. Exchange Rate"],
            "timestamp": new_obj.isoformat(),
        },
    )

    with open("logs.json") as f:
        data = json.load(f)

    data["results"] += list(new_data)

    with open("logs.json", "w") as f:
        json.dump(data, f)

    coefficient: float = float(
        result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    )
    return value * coefficient
