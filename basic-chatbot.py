#: Build a simple rule-based chatbot
def chatbot():
    print("welcome to chatbot :type 'quit' to exit")
    while True:
        user_input = input("you: ").lower()
        if user_input == "hello":
            print("Bot: hi")
        elif user_input == "how are you":
            print("Bot:i'm fine,thanks")
        elif user_input == "bye":
            print("Bot:goodbye...")
        elif user_input == "quit":
            print("Bot:existing ..have nice day")
            break
        else:
            print("i don't understand that ...")
            
chatbot()