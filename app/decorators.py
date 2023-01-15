import jwt
from flask import request, abort

from app.constants import JWT_SECRET, JWT_ALGORITHM


def auth_required(func):
    """
    The decorator function "auth_required" provides access to the endpoint only for registered users.
    """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)
        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    """
    The decorator function "admin_required" provides access to the endpoint only for registered users
    who have registered as an administrator.
    """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]
        role = None
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            role = user.get("role", "user")
        except Exception as e:
            print('JWT Decode Exception', e)
            abort(401)
        if role != 'admin':
            abort(403)
        return func(*args, **kwargs)
    return wrapper
