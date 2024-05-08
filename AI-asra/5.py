import nltk
import random
from nltk.chat.util import Chat, reflections

# Define the patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am fine, thanks for asking.']),
    (r'what is your name?', ['You can call me ChatBot.', 'I am ChatBot, nice to meet you!']),
    (r'what can you do for me?', ['I can help you with basic inquiries. Feel free to ask me anything!']),
    (r'(.*) help (.*)', ['Sure, I can help you. What do you need help with?']),
    (r'quit', ['Bye, take care!', 'Goodbye!']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Define the main function to chat
def chat():
    print("Hi, I'm ChatBot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() == 'quit':
            break

# Run the chat function
if __name__ == "__main__":
    chat()
