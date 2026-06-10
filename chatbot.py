import anthropic
from dotenv import load_dotenv
import os

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

messages = []
while True:
    user_input = input("Tu: ")
    messages.append({"role": "user", "content": user_input})

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system="Esti un asistent util care raspunde doar in romana.",
        messages= messages
    )

    print(message.content[0].text)