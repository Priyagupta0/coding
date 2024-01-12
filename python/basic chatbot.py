import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you", ["I'm good, thanks!", "I'm doing well, how about you?"]],
    ["(what's|what is) your name", ["I'm a chatbot.", "You can call me ChatGPT."]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]],
]

# Create a chatbot using the pairs
chatbot = Chat(pairs, reflections)

# Function to start the chat
def start_chat():
    print("Hi! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

# Start the chat
start_chat()