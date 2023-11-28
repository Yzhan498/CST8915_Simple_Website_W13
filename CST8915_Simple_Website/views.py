from flask import Flask
from flask import render_template
from datetime import datetime
from . import app, request

import requests
import os
import uuid
import json
from dotenv import load_dotenv
load_dotenv()


@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")
