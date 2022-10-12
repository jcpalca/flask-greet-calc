# Put your app in here.
from flask import Flask, request
import operations

app= Flask(__name__)

@app.get('/add')
def add_nums(a, b):
    """Return simple evaluation of adding the parameters a and b"""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)

    result = operations.add(a,b)
    print(result)

    html = f"<html><body><h1>{result}</h1><body><html>"

    return html


