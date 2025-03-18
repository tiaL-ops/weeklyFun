🚀 Exercise: Build a Mini User Management API
Goal:
Create a Flask REST API that allows users to:
✅ Add users to a SQLite database
✅ Retrieve all users
✅ Get a specific user by ID
✅ Update a user’s info
✅ Delete a user

Requirements:
Set up Flask and SQLite (use sqlite3 as the database).
Create a users table with fields:
id (Primary Key, Auto-increment)
name (Text)
age (Integer)
email (Unique Text)
Implement these API routes:
POST /users → Create a new user
GET /users → Fetch all users
GET /users/<id> → Get a single user by ID
PUT /users/<id> → Update user details
DELETE /users/<id> → Remove a user
Bonus Challenges:
Add error handling (e.g., return 404 if a user is not found).
Implement pagination (GET /users?page=1&limit=10).
Use Postman or cURL to test your API.