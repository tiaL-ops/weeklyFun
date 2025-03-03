### **Python Lab: Building an AI Chatbot with NLP**
#### **Objective:**  
You will create a Python-based chatbot that can recognize greetings, tell jokes, detect emotions, and (optionally) fetch real-time weather updates using an API.  

---

## **💡 Step 1: Setup Your Development Environment**  
Before starting, make sure you have the following installed:  
✅ **Python 3.8+**  
✅ **NLTK** (`pip install nltk`) or **spaCy** (`pip install spacy`)  
✅ (Optional) **Requests** (`pip install requests`) – for weather API  

---

## **🔹 Step 2: Understanding NLP Basics**  
Before coding, understand the following NLP concepts:  
📌 **Tokenization** – Splitting text into words/sentences  
📌 **Stopwords** – Ignoring common words like “is,” “the”  
📌 **Lemmatization** – Reducing words to base form (e.g., "running" → "run")  
📌 **Intent Recognition** – Detecting user intent (e.g., greeting vs. asking for weather)  

👉 **Task:** Read about **NLTK or spaCy** and their NLP capabilities.  

---

## **🔹 Step 3: Create the Chatbot Structure**  
Your chatbot will have a simple loop that:  
1️⃣ **Takes user input**  
2️⃣ **Processes it** (cleaning, tokenizing)  
3️⃣ **Understands intent**  
4️⃣ **Generates a response**  

👉 **Task:** Design the chatbot logic using a **flowchart** before coding.  

---

## **🔹 Step 4: Recognizing Greetings & Simple Responses**  
📌 Store common greetings (e.g., "hi," "hello," "hey")  
📌 Match user input with predefined responses  
📌 Implement **randomized responses** for variety  

👉 **Task:** Write a list of possible greetings and responses before implementing them.  

---

## **🔹 Step 5: Implementing Emotion Detection**  
📌 Recognize words related to emotions (e.g., "sad," "happy," "angry")  
📌 Respond with comforting or congratulatory messages  
📌 (Optional) Use sentiment analysis from `TextBlob` (`pip install textblob`)  

👉 **Task:** Make a table of **words → emotions → responses**.  

---

## **🔹 Step 6: Handling Unknown Inputs**  
📌 If input doesn’t match predefined intents, return a clever response  
📌 Example: **"I’m still learning! Can you rephrase?"**  
📌 (Bonus) Use **Markov Chains** to generate responses dynamically  

👉 **Task:** Plan a **fallback strategy** for unknown inputs.  

---

## **🔹 Step 7 (Optional): Connecting to a Weather API**  
📌 Sign up for **OpenWeatherMap API** (https://openweathermap.org/api)  
📌 Learn how to make **GET requests** with `requests`  
📌 Extract **temperature and conditions** from JSON response  

👉 **Task:** Write down the **API URL format** and expected JSON response.  

---

## **🔹 Step 8: Testing and Debugging**  
📌 Try **multiple test inputs** to check responses  
📌 Handle **edge cases** (e.g., empty input, mixed casing, misspellings)  
📌 Optimize the chatbot to respond faster  

👉 **Task:** List 5 edge cases to test.  

---

## **🔹 Step 9: Expanding & Improving**  
📌 Store conversation history to make the chatbot **more interactive**  
📌 Add **speech-to-text** (Google Speech API)  
📌 Deploy as a **Telegram or Discord bot**  

👉 **Task:** Brainstorm **3 features** you’d add if you had more time.  

---

## **📝 Deliverables (What You Should Have by the End)**  
✔ A chatbot that recognizes **greetings, emotions, and simple intents**  
✔ Ability to respond to **unknown inputs cleverly**  
✔ (Optional) Ability to fetch **live weather data**  
✔ Code is well-structured and easy to expand  

