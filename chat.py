import os

messages = []

name = input("Name: ")

while True:
    os.system('cls')

    if len(messages) > 0:
        for m in messages:
            print(f"{m["name"]}: {m["text"]}")

    text = input("Message: ")

    if text == "close":
        print("You left the chat!")
        break

    messages.append({
        "name": name,
        "text": text
    })