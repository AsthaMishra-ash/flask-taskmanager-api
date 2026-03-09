# Flask Task Manager API

A simple RESTful API built using Flask that allows users to manage tasks.  
The API supports creating, retrieving, updating, completing, and deleting tasks.

## Live API
https://flask-taskmanager-api-1.onrender.com

## Features
- Create tasks
- View all tasks
- Update tasks
- Mark tasks as completed
- Delete tasks

## Tech Stack
- Python
- Flask
- SQLite
- SQLAlchemy
- Gunicorn

## API Endpoints

### 1. Get All Tasks
GET /tasks

Returns all tasks stored in the database.

Example Response:
[
 {
  "id": 1,
  "title": "Finish project",
  "completed": false
 }
]

---

### 2. Create a New Task
POST /tasks

Example Request Body:
{
 "title": "Prepare internship application"
}

Example Response:
{
 "message": "Task added"
}

---

### 3. Update a Task
PUT /tasks/<id>

Example Request Body:
{
 "title": "Complete API project",
 "completed": true
}

Example Response:
{
 "message": "Task updated"
}

---

### 4. Mark Task as Completed
PATCH /tasks/<id>/complete

Example Response:
{
 "message": "Task marked as completed"
}

---

### 5. Delete a Task
DELETE /tasks/<id>

Example Response:
{
 "message": "Task deleted"
}

## Project Structure
flask-taskmanager-api
│
├── app.py
├── requirements.txt
├── tasks.db
└── README.md

## Deployment
The API is deployed on Render.

## Author
Astha Mishra
