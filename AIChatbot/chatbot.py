"""
1️⃣ Takes user input
2️⃣ Processes it (cleaning, tokenizing)
3️⃣ Understands intent
4️⃣ Generates a response
"""
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

class ChatBot:

    def __init__(self,content):
        self.content= content
    
    def process(self):
        tokens=nltk.word_tokenize(self.content)
        return tokens

print("Enter your message")
x= input()
myChat = ChatBot(x)
y=myChat.process()
print(y)


