#!/usr/bin/env python
import re
import time
from ast import Num
from turtle import update
import requests

def get_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return data["bpi"]["USD"]["rate_float"]

def check_price_change():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    current_time = data["time"]["updated"]
    current_price = data["bpi"]["USD"]["rate_float"]
    old_price = current_price
    time.sleep(86400)
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    current_time = data["time"]["updated"]
    current_price = data["bpi"]["USD"]["rate_float"]
    new_price = current_price
    return (new_price - old_price)/old_price * 100
