from openai import OpenAI
from dotenv import load_dotenv
import os
#load cofigurations
load_dotenv()

#send up the client
client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key= os.getenv("API_KEY")
)



#send a question to the AI model

while True:
    question = input("\nWhat do you want to ask? ")

    if question.lower() == "quit":
        print("Goodbye!")
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("AI:", response.choices[0].message.content)


print("All good")