#!/usr/bin/env python3
"""Basic Authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method"""

        if not path:
            return True

        if not excluded_paths:
            return True

        normalized_path = path if path.endswith('/') else path + '/'

        if normalized_path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> None:
        """public method"""

        key = 'Authorization'

        if request is None or key not in request.headers:
            return
        return request.headers.get(key)

        if request.headers.get("Authorization") is None:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """public method"""
        return None
