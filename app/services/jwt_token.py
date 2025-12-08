import jwt


class TokenService:
    secret_key = # TODO get key from .env and create class instances via containers
                 # it might also be nice to use class not only as wrapper for functions.
                 # Additionally if you do so, it's probably better to go for @staticmethod
                 # not classmethod

    @classmethod
    def verify_token(cls, token):
        try:
            payload = jwt.decode(token, cls.secret_key, algorithms=["HS256"])
            return payload
        except Exception as e:
            return {"error": "An error occurred"}

    @classmethod
    def create_token(cls, payload):
        token = jwt.encode(payload, cls.secret_key, algorithm="HS256")
        return token
