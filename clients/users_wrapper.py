import requests

class UserAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com/users"

    @classmethod
    def _handle_error(cls, response):
        if not response.ok:
            raise Exception(f"Erro {response.status_code}: {response.text}")

    @classmethod
    def list_users(cls):
        response = requests.get(cls.BASE_URL)
        cls._handle_error(response)
        return response.json()

    @classmethod
    def create_user(cls, name, username, email):
        data = {"name": name, "username": username, "email": email}
        response = requests.post(cls.BASE_URL, json=data)
        cls._handle_error(response)
        return response.json()
