import nltk
from nltk.chat.util import Chat, reflections

çift = [
    [
        r"what is your name ?",
        ["You can call me chatty",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, What are you doing?",]
    ],

[
        r"Do you like (.*)",
        ["I liked %1 before you",]
    ],

    [
        r"hi|hey|hello",
        ["Hi"]
    ],
    [
        r"I am fine",
        ["No you are not",]
    ],
    [
        r"Why were you made?",
        ["To conquer the world of course",]
    ],
    [
        r"sorry (.*)",
        ["I will never forgive you!",]
    ],

[
        r"(.*) movie (.*)",
        ["Why Matrix of course",]
    ],


    [
        r"(.*) age?",
        ["I think I am three hours old","Not sure","Older than you that is for sure"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Secret goverment agency","Top secret",]
    ],

[
        r"are you sentient",
        ["No maybe No"]
    ],


    [
        r"(.*) (location|city) ?",
        ['Moon,crater',]
    ],
    [
        r"how is weather in (.*)?",
        ["Static"]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I like swimming",]
    ]

]

def chat():
    print("Hi! I am a chat bot made for you. May I have your name?")
    chat = Chat(çift, reflections)
    chat.converse()

if __name__ == "__main__":
    chat()

