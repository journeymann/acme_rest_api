# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

accounts = [
    {"id": 1, "name": "Joe Camel", "date": "01-01-1989", "account_num": 513120},
    {"id": 2, "name": "Mario Andretti", "date": "02-05-1997", "account_num": 7617930},
    {"id": 3, "name": "Simon Joseph", "date": "02-07-1992", "account_num": 1010408},
]

def _find_next_id():
    return max(account["id"] for account in accounts) + 1

@app.get("/accounts")
def get_accounts():
    return jsonify(accounts)

@app.post("/accounts")
def add_account():
    if request.is_json:
        account = request.get_json()
        account["id"] = _find_next_id()
        accounts.append(account)
        return account, 201
    return {"error": "Request must be JSON"}, 415
