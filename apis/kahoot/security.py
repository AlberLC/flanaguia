import hashlib
import os
import secrets
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2
from jose import jwt

HASH_ITERATIONS = 500_000


def compare_digest(a: bytes, b: bytes) -> bool:
    return secrets.compare_digest(a, b)


def create_key() -> str:
    return secrets.token_hex(32)


def decode_jwt_token(token: str) -> dict:
    return jwt.decode(token, os.environ['SECRET_KEY'])


def encode_jwt_token(payload: dict) -> str:
    return jwt.encode(payload, os.environ['SECRET_KEY'])


def get_bearer_token(authorization_value: Annotated[str, Depends(OAuth2())]) -> str | None:
    try:
        return authorization_value.split()[1]
    except IndexError:
        pass


def hash_password(password: str, salt: str) -> str:
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), HASH_ITERATIONS).hex()
