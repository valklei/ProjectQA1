import json
import random

from google import genai
from dotenv import load_dotenv  # Функция для загрузки переменных окружения из файла .env.
import os  # Модуль для работы с операционной системой, в частности, для работы с переменными окружения.

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем API-ключ для модели Gemini и Tavily из переменных окружения
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")


api_key = 'GEMINI_API_KEY'
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