import json
import nltk
from nltk.chat.util import Chat, reflections

# Load data from the JSON file
with open("responses.json", "r") as data_file:
    chatbot_data = json.load(data_file)

pairs = [
    [
        r"(hi|hello|hey)(.*)",
        chatbot_data["greetings"]
    ],
    [
        r"what is your name?",
        chatbot_data["name"]
    ],
    [
        r"help",
        [chatbot_data["commands"]["help"]]  
    ],
    [
        r"time",
        [chatbot_data["commands"]["time"]]  
    ],
    [
       r"weather",
        [chatbot_data["commands"]["weather"]]
    ],
    [
     r"news",
        [chatbot_data["commands"]["news"]]
    ],
    [
       r"bye",
        [chatbot_data["commands"]["goodbye"]]
    ],
    [
        r"(.*)",
        chatbot_data["fallback"]
    ]
]

chatbot = Chat(pairs, reflections)

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("ChatBot: Goodbye")
        break
    else:
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
