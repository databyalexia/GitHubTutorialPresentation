from greetings import english_greeting, spanish_greeting, french_greeting, swahili_greeting

def main():
    print("Welcome to the Collaborative Greetings App!")
    print("Here are the greetings that we have: ")
    print("-" *30)
    english_greeting()
    spanish_greeting()
    french_greeting()
    swahili_greeting()

if __name__ == "__main__":
        main()