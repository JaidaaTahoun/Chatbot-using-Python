# Import the openai library so we can talk to OpenAI's models
import openai

# Your OpenAI API key goes here. It's like a password for using the API. To create API key go to Openai website and create a secret key. 
openai.api_key = "#openai key goes here"

# Define a function to send a chat message to GPT and get a response
def chat_with_gpt(prompt):
    # Send a message to GPT and get its response using the specified model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # This tells which version of GPT to use
        messages=[{"role": "user", "content": prompt}]  
    )
    
    return response.choices[0].message.content.strip()

# This part checks if you're running this script directly
if __name__ == "__main__":
    # Start a loop to keep chatting until you decide to stop
    while True:
        user_input = input("You: ")  
        # If you type "quit", "exit", or "bye", the chat will end
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)


