import jwt


class ApiVerifyClass:
<<<<<<< HEAD
    secret_key = "HKJWERFKJHFKJHFEWEKJH"
=======
    secret_key = "thilvrcvzckzeiejzprymoisrfnaypzxqnoxizimmxfkrdrmbyrhtibsjxjbijjliwfhjrtwmoecldkzdgsshsehnyubnzbvigdcfhwzcvbcplhogtawpsffqmffjndj"
>>>>>>> origin/containers

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
