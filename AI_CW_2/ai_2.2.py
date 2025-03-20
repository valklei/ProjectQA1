import random

from google import genai


api_key = 'AIzaSyClTgBLxK5FR5mrV9cV765QeA4DKeLmHfs'
# Создание клиента API
client = genai.Client(api_key=api_key)
hidden_number = str(random.randint(1, 100))
start_message = f"""Мы с тобой сыграем в игру. ты загадал число {hidden_number} (принадлежит диапазону 1-100).
Моя задача - отгадать это число. Твоя задача - либо сказать 'Победа' (Только одно слово), если я отгадал число, либо 
написать четверостишие, о том, 'горячо' или 'холодно' если названное мной число близко к загаданному 
разница в пределах 20ти - тепло
разница в пределах 10ти - горячо
разница в пределах 40 - прохладно
если разница больше 40 - морозно
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