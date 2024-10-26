from dotenv import load_dotenv
import os
import requests


def ask_ai_for_advice(health_problem):
    load_dotenv()
    api_key = os.getenv('HackApi')
    url = "https://api.openai.com/v1/chat/completions"

   
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    print(health_problem)
    data = {
        "model": "gpt-3.5-turbo-0125",  
        "messages": [
            {
                "role": "user",
                "content": "Jestem w pracy. Przydalaby mi sie przerwa. co moge teraz zrobic zebym troche lepiej sie czul. Opaska wykryla u mnie: {health_problem}. krotka odpowiedz"
            }
        ]
    }

    # Make the API call
    response = requests.post(url, headers=headers, json=data)
   
    
    if response.status_code == 200:
        response_data = response.json()
        chat_response = response_data['choices'][0]['message']['content']
        return chat_response
    else:
        print("Error:", response.status_code, response.text)
