#!/usr/bin/env python3
"""Hash password"""

from db import DB
from user import User
import bcrypt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        # Convert the password string to bytes
        password_bytes = password.encode('utf-8')

        # Generate a salt
        salt = bcrypt.gensalt()

        # Hash the password with the salt
        hashed_password = bcrypt.hashpw(password_bytes, salt)

        # Return the hashed password as bytes
        return hashed_password

    def register_user(self, email: str, password: str) -> User:
        # Check if user already exists
        if self._db.user_exists(email):  # Assuming this method checks for existing users
            raise ValueError(f"User {email} already exists.")

        # Hash the password
        hashed_password = self._hash_password(password)

        # Create a new User object (assuming User has an init method that accepts email and hashed_password)
        user = User(email=email, password=hashed_password)

        # Save the user to the database
        self._db.save_user(user)  # Assuming this method saves the user object to the database

        # Return the new User object
        return user
