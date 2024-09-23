#!/usr/bin/env python3

from flask import Flask, request

def create_app():
    app1 = Flask(__name__)
    @app1.route("/")
    def main():
        return '''
     <form action="/echo_user_input" method="POST">
         <input name="user_input">
         <input type="submit" value="Submit!">
     </form>
     '''
    @app1.route("/echo_user_input", methods=["POST"])
    def echo_input():
        input_text = request.form.get("user_input", "")
        return "You entered: " + input_text
app1 = create_app()
