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
        self.input={
            'greetings':["hi","whatsup", "hello","hola"],
            'goodbye':["bye","aurevoir", "see you","travel safe"],
            'funny':["hahaha","lol", "lmao","got me rolling"]
        }
        self.responses={
            'greetings':["hi","hiii", "how are youu","helloooo"],
            'goodbye':["been nice talking to you","can't wait to see you ", "see you","travel safe"],
            'funny':["hahahahaa","you are so funnyy", "so coooll","LLLLOOOOOLLLL"]
        }
    
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








