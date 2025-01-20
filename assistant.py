import openai

class Assistant:
    @staticmethod
    def generate_response(message: str):
        response = openai.Completion.create(model="gpt-3.5-turbo", prompt=message, max_tokens=150)
        return response.choices[0].text.strip()
