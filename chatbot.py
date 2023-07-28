import nltk
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download the necessary resources for nltk
nltk.download('punkt')
nltk.download('stopwords')

# Pre-defined responses for the chatbot
responses = {
    'hello': 'Hello! How can I assist you today?',
    'how are you': 'I am just a bot, but thanks for asking!',
    'bye': 'Goodbye! Have a great day!',
    'default': 'I am not sure how to respond to that. Can you rephrase?',
    #you can add many more responses of your own wish
}

# Set of words to identify greeting and farewell
greetings = set(['hello', 'hi', 'hey'])
farewells = set(['bye', 'goodbye'])

def preprocess_input(user_input):
    # Tokenize the user input and remove stop words
    tokens = word_tokenize(user_input.lower())
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token not in stop_words]

def generate_response(user_input):
    tokens = preprocess_input(user_input)
    
    # Check for greetings or farewells and respond accordingly
    if any(word in greetings for word in tokens):
        return responses['hello']
    elif any(word in farewells for word in tokens):
        return responses['bye']
    
    # If no specific keyword matches, return a default response
    return responses['default']

def main():
    print("Chatbot: Hi there! I'm your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
