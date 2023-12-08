print("Welcome to my Chatbot")

import openai


api_key = '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'


openai.api_key = api_key

def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  
        prompt=prompt,
        max_tokens=50,  #
    )
    return response.choices[0].text.strip()

# Main chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    
   
    prompt = f"You: {user_input}\nBot:"
    
    bot_response = chat_with_bot(prompt)
    print(f"Bot: {bot_response}")

print("Chatbot: Goodbye!")
