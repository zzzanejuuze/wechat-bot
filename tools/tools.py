import json

def get_stock_price(ticker): 
    try:
        stock = {
                "AAPL": 100,
                "MSFT": 1000,
            }
        price = stock[ticker]
        return json.dumps({"company ticker": ticker, "price": price})
    except Exception as e:
        return json.dumps({"message": "error occur"})

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get the current stock price for a given ticker symbol of a company",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": "The stock ticker symbol for a company (eg. APPL for Apple)",
                    }
                },
            "required" : ["ticker"],
            },
        },
    }
]