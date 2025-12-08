import jwt


class ApiVerifyClass:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def verify_token(self, token):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except Exception as e:
            return {"error": "An error occurred"}

        def create_token(self, payload):
            token = jwt.encode(payload, self.secret_key, algorithm="HS256")
            return token
