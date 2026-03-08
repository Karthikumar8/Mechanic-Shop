# 🚗 Velocity Motors – Workshop Management System

A **Django-based Workshop Management System** designed to manage **vehicles, mechanics, and work orders** in an automobile service center.

The system allows workshop managers to **assign mechanics to vehicles**, track service progress, and monitor work order statuses using a **dashboard and REST APIs**.

---

# 📌 Features

- Workshop Dashboard with statistics
- Work Order Management (CRUD operations)
- Mechanic and Vehicle tracking
- Admin panel for managing data
- REST API using Django REST Framework
- Postman API testing
- Status tracking (Planned, In Progress, Completed)

---

# 🏗 Project Structure
# 🚗 Velocity Motors – Workshop Management System

A **Django-based Workshop Management System** designed to manage **vehicles, mechanics, and work orders** in an automobile service center.

The system allows workshop managers to **assign mechanics to vehicles**, track service progress, and monitor work order statuses using a **dashboard and REST APIs**.

---

# 📌 Features

- Workshop Dashboard with statistics
- Work Order Management (CRUD operations)
- Mechanic and Vehicle tracking
- Admin panel for managing data
- REST API using Django REST Framework
- Postman API testing
- Status tracking (Planned, In Progress, Completed)

---

# 🏗 Project Structure
velocity_motors/
│
├── workshop_project/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── workshop_app/
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── api_views.py
│ ├── urls.py
│ └── admin.py
│
├── templates/
│ ├── dashboard.html
│ ├── workorders.html
│ └── create_workorder.html
│
├── static/
│ ├── css/
│ ├── js/
│ └── images/
│
├── db.sqlite3
└── manage.py


---

# 🗄 Database Models

The system uses three main models.

## Vehicle

Stores vehicle information.

Fields:

- Vehicle Number
- Model
- Owner Name

---

## Mechanic

Stores details about mechanics working in the workshop.

Fields:

- Mechanic Name
- Specialization
- Phone Number

---

## Work Order

Represents a service request assigned to a mechanic.

Fields:

- Vehicle (Foreign Key)
- Mechanic (Foreign Key)
- Issue Description
- Status (Planned / In Progress / Completed)
- Created Date

---

# 🔧 How the System Tracks Mechanics and Vehicles

The system monitors **which mechanic is handling which vehicle** using **Foreign Key relationships** in the WorkOrder model.

This allows the system to:

Assign a mechanic to a vehicle

Track the progress of repairs

View work orders assigned to each mechanic

Monitor job completion status

📊 Dashboard

The dashboard displays workshop statistics including:

Total Work Orders

Planned Work Orders

In Progress Work Orders

Completed Work Orders

A chart visualization is also included to display work order status distribution.

🖥 Web Pages

The web interface provides the following pages:

Dashboard

Displays workshop statistics and charts.

Work Orders Page

Displays all work orders with details such as:

Vehicle

Assigned Mechanic

Issue Description

Status

Create Work Order

Allows users to create a new work order and assign a mechanic to a vehicle.

🔐 Admin Panel

Django Admin allows administrators to manage:

Vehicles

Mechanics

Work Orders

Admin panel URL:

http://127.0.0.1:8000/admin
🌐 REST API Endpoints

The system provides REST APIs using Django REST Framework.

Method	Endpoint	Description
GET	/api/workorders/	Get all work orders
POST	/api/workorders/	Create new work order
GET	/api/workorders/{id}/	Get single work order
PUT	/api/workorders/{id}/	Update work order
DELETE	/api/workorders/{id}/	Delete work order
📡 Postman API Testing

The APIs were tested using Postman.

Example operations tested:

Create Work Order

POST /api/workorders/

{
  "vehicle": 1,
  "mechanic": 2,
  "issue_description": "Brake repair",
  "status": "Planned"
}
Get All Work Orders

GET

/api/workorders/
Update Work Order Status

PUT

/api/workorders/1/
Delete Work Order

DELETE

/api/workorders/1/
⚙ Setup Instructions

Follow these steps to run the project locally.

1️⃣ Clone the Repository
git clone https://github.com/yourusername/velocity-motors.git
2️⃣ Navigate to the Project
cd velocity-motors
3️⃣ Create Virtual Environment
python -m venv venv

Activate environment.

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
4️⃣ Install Dependencies
pip install django
pip install djangorestframework
5️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate
6️⃣ Create Admin User
python manage.py createsuperuser
7️⃣ Run Server
python manage.py runserver

Open in browser:

http://127.0.0.1:8000

Admin panel:

http://127.0.0.1:8000/admin


# API Testing in Postman
<img width="1081" height="878" alt="image" src="https://github.com/user-attachments/assets/c8f26d1c-fc5e-45f7-9919-88116263dd6d" />

# Admin Panel in Browser
<img width="1529" height="886" alt="image" src="https://github.com/user-attachments/assets/a4f9bd9b-61db-41b0-8242-1b11ee38de07" />

# Dashboard webpage in browser
<img width="1884" height="867" alt="image" src="https://github.com/user-attachments/assets/1f2ab7f8-e6bf-4ef1-98c6-a253ac654e2c" />

# Work Orders Webpage in Browser
<img width="1909" height="782" alt="image" src="https://github.com/user-attachments/assets/ce1068af-36c6-4a33-a1f2-9a1f386e215a" />

🛠 Technologies Used

Python

Django

Django REST Framework

HTML

CSS

JavaScript

Chart.js

SQLite

Postman

👨‍💻 Author

Karthikumar Bharatmoorthy

This project was developed as part of a Django backend and API development training program to demonstrate CRUD operations, REST APIs, and dashboard visualization.







