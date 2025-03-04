
## **March Coding Challenge Plan (System Design Focus)**
Each challenge will help you improve your ability to **design scalable, efficient systems** while also practicing coding.  

---

### **Week 1 (Python) – AI Chatbot 🤖** *(Kept the same)*
💡 **Goal:** Build a chatbot with basic NLP capabilities.  
*(Good for working with APIs and text processing.)*  

---

### **Week 2 (Java) – Scalable URL Shortener 🔗**
💡 **Goal:** Design and implement a **URL shortener like Bitly** that can handle millions of requests efficiently.  

#### **System Design Focus:**
- **Database choice:** Use **MySQL/PostgreSQL** (for relational mapping) or **Redis** (for caching frequently used URLs).  
- **Hashing strategy:** Implement **Base62 encoding** (to generate short links).  
- **Read vs Write optimization:** Design for **quick redirection** and **efficient URL lookups**.  
- **Rate Limiting:** Prevent abuse using techniques like **Token Buckets**.  

🔧 **Extra Challenge:** Add **custom short URLs** (e.g., `short.ly/mycustomlink`).  

---

### **Week 3 (JavaScript) – Scalable Real-Time Stock Price Tracker 📈**
💡 **Goal:** Build a **scalable real-time stock price tracker** that can handle a large number of concurrent users.  

#### **System Design Focus:**
- **Frontend:** Use **React.js** with WebSockets for real-time updates.  
- **Backend:** Use **Node.js + WebSockets** to push live stock prices to users.  
- **Database:** Store historical stock data using **TimescaleDB** (optimized for time-series data).  
- **Load Handling:** Use **Redis Pub/Sub** for scaling WebSocket connections.  
- **API Choice:** Fetch data from a service like Alpha Vantage or Yahoo Finance.  

🔧 **Extra Challenge:** Implement a **trading bot simulation** that makes automated stock trades based on price patterns.  

---

### **Week 4 (C++) – Distributed Maze Solver (Pathfinding with Microservices) 🔍**
💡 **Goal:** Design a **distributed system** to solve a **large-scale maze** efficiently using microservices.  

#### **System Design Focus:**
- **Break the maze into smaller sections** and assign each to a **separate worker service**.  
- Use **gRPC** or **REST APIs** for communication between services.  
- Implement **message queues (RabbitMQ/Kafka)** to distribute tasks.  
- Use **Redis** or **a shared database** to track the progress of different maze sections.  
- Combine results to display the final shortest path.  

🔧 **Extra Challenge:** Visualize the distributed computation using **a simple dashboard (React/C++)**.  

