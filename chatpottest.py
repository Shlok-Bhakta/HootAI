
import openai

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are student helper who will be given a question, an answer, and wether the student was correct or not, your job is to explain to the student why they were wrong or right. The questions will in the format 'question: answer' your job is to check if the quesiton is right and wrong and say why"}
]

print("Your new assistant is ready!")


message = input()
messages.append({"role": "user", "content": message})
print(message)
response = openai.ChatCompletion.create(

model="gpt-3.5-turbo",
messages=messages)
reply = response["choices"][0]["message"]["content"]

print("\n" + reply + "\n")
