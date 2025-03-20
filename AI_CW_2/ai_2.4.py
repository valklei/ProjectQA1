import json
import random

from google import genai


api_key = ''
client = genai.Client(api_key=api_key)
hidden_number = str(random.randint(1, 100))
user_parameters = {
    'weight': input('Введите ваш вес: '),
    'height': input('Введите ваш рост: '),
    'age': input('Введите ваш возраст: ')
}
start_message = f"""Ты специалист по здоровому питанию. Ты умеешь составлять меню на день
исходя из возраста, роста и веса. 
Вот параметры пользователя:
{'\n'.join(f"{key}: {value}" for key, value in user_parameters.items())}""" + \
"""Ответ на сообщение пользователя структурируй следующим образом:
{
 day_menu: в этом поле распиши меню на день (str),
    user_parameters: {
        weight: вес либо из ранее предоставленных данных, либо согласно новым данным от пользователя,
        height: высота либо из ранее предоставленных данных, либо согласно новым данным от пользователя,
        age: возраст либо из ранее предоставленных данных, либо согласно новым данным от пользователя,
    }
}
Убедись, что в ответ ты передаешь только валидный JSON
"""

messages = [f'System: {start_message}']
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=messages
)
while True:
    data = json.loads(response.text)
    print(data.get('day_menu'))
    user_parameters = data.get('user_parameters')
    messages.append(f'Agent: {response.text}')
    messages.append(f'User: {input("Введите ваши изменения: ")}')
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=messages
    )
print(response.text)