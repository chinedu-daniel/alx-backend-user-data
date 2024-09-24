#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify
from auth import Auth


AUTH = Auth()

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    # Get the email and password from the form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email and password were provided
    if not email or not password:
        return jsonify({"message": "email and password required"}), 400

    try:
        # Register the user using the Auth class
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 201
    except ValueError:
        # If the user already exists, return an error message
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
