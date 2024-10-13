from app.applicant.domain.repositories.openai_repository import OpenaiRepository
from openai import OpenAI


class OpenaiRepositoryImpl(OpenaiRepository):

    def search_by_prompt(self, prompt: str):
        try:
            client = OpenAI(
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

            print(completion.choices[0].message)

            return completion.choices
        except ZeroDivisionError as e:
            print(f"Ocurrió un error: {e}")
            return ''

