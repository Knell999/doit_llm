from openai import OpenAI
from dotenv import load_dotenv
import os

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0.1,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant"
        },
        {
            "role": "user",
            "content": "2002년 월드컵 우승 팀은 어디야?"
        }
    ]
)

print(response)

print('----')
print(response.choices[0].message.content)
