"""
1️⃣ Takes user input
2️⃣ Processes it (cleaning, tokenizing)
3️⃣ Understands intent
4️⃣ Generates a response
"""
import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import random

#nltk.download('all')

class ChatBot:

    def __init__(self,content):
        self.content= content
        self.greetings=["hi","whatsup", "hello","hola"]
        self.responses=["greetings", " how are you", " how can i help you", "hiiii"]
    
    def process(self):
        tokens=nltk.word_tokenize(self.content)
        stopWords=stopwords.words('english')
        res=[]
        for token in tokens:
            if token not in stopWords:
                res.append(token)

        return res
    
    def detect_intent(self):
        tokenized_Word=self.process()
        for token in tokenized_Word:
            if token in self.greetings:
                return "greetings"
        return "Unknown"
    
    def answer(self):
        if self.detect_intent() == "greetings":
            return random.choice(self.responses)
        else:
            return " Sorry I can't catch that"
    

x= "We need to save the world,hi."
myChat = ChatBot(x)
y=myChat.process()

tags =pos_tag(y)
print(myChat.answer())








