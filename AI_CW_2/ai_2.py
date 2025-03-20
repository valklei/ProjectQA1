from google import genai
import os

from google import genai

api_key = ''
# Загрузка API-ключа из переменной окружения
#api_key = os.getenv("GEMINI_API_KEY")
# Создание клиента API
client = genai.Client(api_key=api_key)
# Отправка запроса к модели
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["Напиши четверостищье о погоде"]
)
# Вывод ответа
print(response.text)

hidden_number = str(random.randint(a:1, d:100))
