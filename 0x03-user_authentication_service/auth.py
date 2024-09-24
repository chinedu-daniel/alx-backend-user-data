#!/usr/bin/env python3
"""Hash password"""

import bcrypt


def _hash_password(self, password: str) -> bytes:
    # Convert the password string to bytes
    password_bytes = password.encode('utf-8')

    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    # Return the hashed password as bytes
    return hashed_password
