import openai

# Store your API key in a variable
openai.api_key = "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"

# Set a context for the ChatGPT API
messages = [
    {"role": "system", "content": "You are student helper who will be given a question, an answer, and wether the student was correct or not, your job is to explain to the student why they were wrong or right"}
]

# Use an infinite while loop to chat with the ChatGPT API repeatedly
prompt = input('User: ')
response = openai.ChatCompletion.create(
model="gpt-3.5-turbo",
messages=messages + [{"role": "user", "content": prompt}]
)
print("ChatGPT: ", response['choices'][0]['message']['content'])
messages.append({"role": "user", "content": prompt})
messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
variable = response

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")