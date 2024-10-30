from applicant.domain.repositories.openai_repository import OpenaiRepository
from openai import OpenAI
import json

import os
from flask import Blueprint, jsonify, request, current_app

class OpenaiRepositoryImpl(OpenaiRepository):

    def search_by_prompt(self, prompt: str):
        try:
            print(os.environ.get("OPENAI_API_KEY"))
            client = OpenAI(
                api_key=os.environ.get("OPENAI_API_KEY"),
            )


            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "que caracteristicas tiene un profesor de quimica."},
                    {
                        "role": "user",
                        "content": "María tiene un doctorado en química orgánica, lo que le permite tener un conocimiento detallado de la estructura molecular y las reacciones químicas. Ha publicado varios artículos sobre catálisis en revistas científicas. Es un profesor de quimica."
                    }
                ]
            )

            current_app.logger.info(f"response: {completion.choices[0].message.content}")

            return completion.choices[0].message.content
        except ZeroDivisionError as e:
            print(f"Ocurrió un error: {e}")
            return ''

