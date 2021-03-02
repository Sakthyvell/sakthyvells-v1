import os

from flask import Flask, render_template


def create_app(test_config=None):
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def home():
        return render_template("index.html");

    return app


if __name__ == '__main__':
    create_app()