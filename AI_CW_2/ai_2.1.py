import random


import os
import faiss
from dotenv import load_dotenv
from google import genai
import numpy as np
load_dotenv()

# Получаем API-ключ для модели Gemini и Tavily из переменных окружения
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")


api_key = 'GEMINI_API_KEY'
# Создание клиента API
client = genai.Client(api_key=api_key)
hidden_number = str(random.randint(1, 100))
start_message = f"""Мы с тобой сыграем в игру. ты загадал число {hidden_number} (принадлежит диапазону 1-100).
Моя задача - отгадать это число. Твоя задача - либо сказать 'Победа' (Только одно слово), если я отгадал число, либо 
'больше' -если названное мной число меньше твоего,или 'меньше' если названное мной число больше загаданному.
User: {input('Введите вашу попытку: ')}"""

messages = [f'System: {start_message}']
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=messages
)
while response.text != 'Победа':
    print(response.text)
    messages.append(f'Agent: {response.text}')
    messages.append(f'User: {input("Введите вашу попытку: ")}')
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=messages
    )
print(response.text)