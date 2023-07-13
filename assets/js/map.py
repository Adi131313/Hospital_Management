
from ctypes import _NamedFuncPointer
from urllib import response
import requests

def get_google_maps_js():
    api_key = 'AIzaSyDQCH4PJ6SlpMeS2BVhWiCv8k3C_RSrEVU'
    url = f'https://maps.googleapis.com/maps/api/js?key={api_key}'
    response = requests.get(url)
    returnnew_func()

def new_func():
    return response.text

from flask import Flask, render_template

def new_func1():
    return _NamedFuncPointer

app = Flask(new_func1())

@app.route('/')
def index():
    google_maps_js = get_google_maps_js()
    return render_template('index.html', google_maps_js=google_maps_js)