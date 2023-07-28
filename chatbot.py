import openai
import config      #to hide our SECRET API key as it is protected

def get_chatbot_response(prompt):
    openai.api_key = config.OPENAI_API_KEY
    response = openai.Completion.create(
        engine="text-davinci-003",  # Replace with "text-davinci-003" for GPT-3.5 or other relevant engine
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Chatbot: Hello! I'm your chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        chatbot_response = get_chatbot_response("User: " + user_input + "\nChatbot:")
        print("Chatbot:", chatbot_response)

if __name__ == "__main__":
    main()
