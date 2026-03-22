import os

import requests
from dotenv import load_dotenv 

load_dotenv()

class Request:

    URL = "http://fastapi:8000/api/v1/ask_assistent_ia"

    @staticmethod
    def post(payload: dict):
        try:
            response = requests.post(
                url=Request.URL,
                json=payload
            )

            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            return {"answer": f"Erro na comunicação com a API: {str(e)}"}