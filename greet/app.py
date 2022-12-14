from urllib.request import AbstractDigestAuthHandler
from flask import Flask, request

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    """Return simple 'welcome' greeting"""
    html = "<html><body><h1>welcome</h1></body></html>"
    return html

@app.get("/welcome/home")
def welcome_home():
    """Return simple 'welcome home' greeting"""
    html = "<html><body><h1>welcome home</h1></body></html>"
    return html

@app.get("/welcome/back")
def welcome_back():
    """Return simple 'welcome back' greeting"""
    html = "<html><body><h1>welcome back</h1></body></html>"
    return html
