import json
import pandas as pd
from datetime import datetime 


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


def save_todo(todo):
    current_date = datetime.now()
    todo_list = [{"datetime": current_date,
                  "todo": todo}]

    try:
        todo_df = pd.read_csv("todo.csv", index_col=0)
    except:
        todo_df = pd.DataFrame()

    todo_df = todo_df.append(todo_list)
    todo_df.to_csv("todo.csv")

    complete_msg = "TODO Saved!!!"

    return complete_msg


def query_todo():
    try:
        concate_string = ""
        n = 0
        todo_df = pd.read_csv("todo.csv", index_col=0)
        for i, r in todo_df.iterrows():
            n += 1
            todo = r['todo']
            date = pd.to_datetime(r['datetime']).date()
            todo_str = f"{n}. {str(date)} - {todo}\n"
            concate_string += todo_str
    except:
        concate_string = "TODO list is empty"

    return concate_string


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
    },
    {
        "type": "function",
        "function": {
            "name": "save_todo",
            "description": "Save the todo for a given todo item",
            "parameters": {
                "type": "object",
                "properties": {
                    "todo": {
                        "type": "string",
                        "description": "TODO item (eg. buy some apples)",
                    }
                },
            "required" : ["todo"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "query_todo",
            "description": "query the todo or memo list",
            "parameters": {
                "type": "object",
                "properties": {

                },
            "required" : [],
            },
        },
    }
]






