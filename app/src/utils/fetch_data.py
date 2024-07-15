import requests


def fetch_currency_data(currency: str) -> dict:
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@2024.7.14/v1/currencies/{currency}.json"
    # print("URL is: ", url)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[currency]
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")