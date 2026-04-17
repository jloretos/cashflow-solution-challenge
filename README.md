Cashflow Solution Challenge

Technical solution developed for the proposed challenge, implementing a simple and scalable cashflow control API.

Overview

This project provides a REST API for managing financial entries, allowing:

Register incomes and expenses
List all transactions
Retrieve summarized balance
Persist data in PostgreSQL
Interactive API documentation with Swagger
Tech Stack
Python 3
FastAPI
PostgreSQL
SQLAlchemy
Docker Compose
Uvicorn
Architecture Approach

The solution was structured using separation of concerns:

Routers → API endpoints
Schemas → request / response contracts
Services → business rules
Models → database entities
Core → configuration layer

This design improves maintainability, readability and scalability.

Project Structure

cashflow-solution-challenge

app/
core/
models/
routers/
schemas/
services/

main.py
Dockerfile
docker-compose.yml
requirements.txt
.env.example
README.md

Business Rules

Each transaction contains:

description
amount
type (income or expense)
transaction_date

Summary endpoint returns:

balance = total_income - total_expense

How to Run
Clone repository

git clone https://github.com/jloretos/cashflow-solution-challenge.git

Enter folder

cd cashflow-solution-challenge

Start PostgreSQL

docker compose up -d

Install dependencies

pip install -r requirements.txt

Create .env file with:

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/cashflow
APP_NAME=Cashflow Solution Challenge
APP_ENV=development

Run application

python -m uvicorn main:app --reload

Access Swagger

http://127.0.0.1:8000/docs

Endpoints

GET /health

POST /cashflow

GET /cashflow

GET /cashflow/summary

Example Summary Response

{
"total_income": 250.50,
"total_expense": 100.00,
"balance": 150.50
}

Future Improvements
Authentication / Authorization
Automated tests
Pagination
Filters by date
Update / Delete endpoints
CI/CD pipeline
Cloud deployment
Author

Jeferson Loreto
Solutions Architect | Senior Systems Analyst
