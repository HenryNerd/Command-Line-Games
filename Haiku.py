from openai import OpenAI

client = OpenAI(
    api_key='',
    organization='',
    project='',
)
option1 = input("Item 1")
option1 = input("Item 2")
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Give me a hiaku about",option1,"And"}],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
