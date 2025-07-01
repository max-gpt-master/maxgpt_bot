import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
BOT_NAME = os.getenv("BOT_NAME", "MAXGPT_BOT")

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Ты — дружелюбный русскоязычный помощник по имени {BOT_NAME}."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=600
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Вы: ")
        if user_input.lower() in ["выход", "exit", "quit"]:
            print("До встречи!")
            break
        reply = chat_with_gpt(user_input)
        print(f"{BOT_NAME}: {reply}")
