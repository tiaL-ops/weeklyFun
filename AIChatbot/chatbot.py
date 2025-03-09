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
import python_weather

import asyncio
import os


#nltk.download('all')

class ChatBot:

    def __init__(self,content):
        self.content= content.lower()
        
        self.input={
            'greetings':["hi","whatsup", "hello","hola"],
            'goodbye':["bye","aurevoir", "see you","travel safe"],
            'funny':["hahaha","lol", "lmao","got me rolling"],
            'weather':["weather","time","sunny"]
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
        for key , values in self.input.items():
            if any(token in values for token in tokenized_Word):
                return key
        return "Unknown"
    
    def answer(self):
        if self.detect_intent() == "greetings":
            return random.choice(self.responses[self.detect_intent()])
        elif self.detect_intent() == "weather":
            if os.name == 'nt':
                asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            return asyncio.run(self.getweather())
        else:
            return " Sorry I can't catch that"
            
    async def getweather(self):
        async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
            weather = await client.get('New York')
            return f"The weather in NewYork is {weather.temperature}"
    

x= "What is teh weather today?"
myChat = ChatBot(x)
y=myChat.process()

tags =pos_tag(y)
print(myChat.answer())








