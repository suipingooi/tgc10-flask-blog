from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.template.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host='localhost',
            port=8080,
            debug=True)