from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify

def expire_date():
    now = datetime.now()
    new = now + timedelta(1)
    return new

def write_token(data: dict):
    token = encode(payload = {**data, "exp": expire_date()}, key = getenv('KEY'), algorithm = "HS256")
    return token.encode("UTF-8")

def val_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("KEY"), algorithms=["HS256"])
        decode(token, key=getenv("KEY"), algorithms=["HS256"])
    except exceptions.DecodeError:
        response = jsonify({"message": "Invalid Token"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({"message": "Token Expired"})
        response.status_code = 401
        return response