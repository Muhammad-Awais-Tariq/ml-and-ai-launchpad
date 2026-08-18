import argparse
import os
from pathlib import Path

import pandas as pd
import requests

try:
    from dotenv import load_dotenv
except ImportError: 
    def load_dotenv(dotenv_path):
        if not dotenv_path.exists():
            return False

        for line in dotenv_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))
        return True

load_dotenv(dotenv_path=Path(__file__).resolve().with_name(".env"))

API_KEY = os.getenv("API_KEY", "").strip()


def fetch_stock_data(symbol: str = "TSLA") -> pd.DataFrame:
    if not API_KEY:
        raise ValueError("API_KEY is not set. Add it to the scripts/.env file as API_KEY=your_key")

    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Convert daily time series to a pandas DataFrame
    ts_data = data.get("Time Series (Daily)", {})
    return pd.DataFrame.from_dict(ts_data, orient="index")


def main() -> None:
    parser = argparse.ArgumentParser(description="Download stock data from Alpha Vantage")
    parser.add_argument("--symbol", default="TSLA", help="Stock symbol to fetch")
    parser.add_argument("--download", action="store_true", help="Save the dataframe to an Excel file")
    parser.add_argument("--output", default=None, help="Optional output Excel path")
    args = parser.parse_args()

    df = fetch_stock_data(args.symbol)

    if args.download:
        output_path = Path(args.output) if args.output else Path(__file__).resolve().with_name(f"{args.symbol.lower()}_daily.xlsx")
        if output_path.suffix.lower() != ".xlsx":
            output_path = output_path.with_suffix(".xlsx")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_excel(output_path, index=True)
        print(f"Downloaded dataframe to {output_path}")
    else:
        print(df.head())


if __name__ == "__main__":
    main()
