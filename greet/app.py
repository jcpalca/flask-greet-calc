from urllib.request import AbstractDigestAuthHandler
from flask import Flask, request

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    """Return simple 'welcome' greeting"""
    html = "<html><body><h1>welcome</h1></body></html>"
    return html

