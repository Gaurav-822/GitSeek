from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
import requests
import json

# Configuring Flask Application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("username")
        url = f'https://api.github.com/users/{name}'
        response = requests.get(url)

        # Check the status code
        if response.status_code == 200:
            # Decode the JSON response
            data = json.loads(response.content)

            # Print the user's name
            return render_template("index.html", name=data["name"], profile_image=data["avatar_url"], bio=data["bio"], location=data["location"], followers=data["followers"], following=data["following"], link=data["html_url"], repos=data["public_repos"])
        else:
            return f'Request failed with status code: {response.status_code}'

    return render_template("index.html")
