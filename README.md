# Cashflow Solution Challenge

## **Overview**

Technical solution developed for the proposed challenge, implementing a **simple, scalable and maintainable Cashflow Control API**.

The application allows registering incomes and expenses, listing transactions, calculating balances and exposing endpoints through an interactive Swagger interface.

---

## **Main Features**

- Register **income** and **expense** transactions
- List all financial entries
- Generate summarized balance
- Persist data in PostgreSQL
- Interactive API documentation via Swagger
- Organized layered architecture

---

## **Tech Stack**

- **Python 3**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Docker Compose**
- **Uvicorn**

---

## **Architecture Approach**

The solution was structured using **separation of concerns**, improving maintainability, readability and scalability:

- **Routers** → API endpoints  
- **Schemas** → request / response contracts  
- **Services** → business logic  
- **Models** → database entities  
- **Core** → configuration layer  

---

## **Application Flow**

```text
┌───────────────┐
│ Client Request│
└───────┬───────┘
        ▼
┌───────────────┐
│ FastAPI Router│
└───────┬───────┘
        ▼
┌───────────────┐
│ Service Layer │
└───────┬───────┘
        ▼
┌───────────────┐
│ SQLAlchemy ORM│
└───────┬───────┘
        ▼
┌────────────────────┐
│ PostgreSQL Database│
└───────┬────────────┘
        ▼
┌───────────────┐
│ JSON Response │
└───────────────┘
```
---

## **Project Structure**

cashflow-solution-challenge/

```text
app/
├── core/        # Settings and configuration
├── models/      # Database entities
├── routers/     # API endpoints
├── schemas/     # Request / response models
├── services/    # Business rules
└── database.py  # Database connection
```

main.py  
Dockerfile  
docker-compose.yml  
requirements.txt  
.env.example  
README.md  

---

## **Business Rules**

Each transaction contains:

- **description**
- **amount**
- **type** (`income` or `expense`)
- **transaction_date**

Balance formula:

balance = total_income - total_expense

---

## **How to Run**

### **1. Clone repository**

git clone https://github.com/jloretos/cashflow-solution-challenge.git

cd cashflow-solution-challenge

### **2. Start PostgreSQL**

docker compose up -d

### **3. Install dependencies**

pip install -r requirements.txt

### **4. Create .env file**

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/cashflow

APP_NAME=Cashflow Solution Challenge

APP_ENV=development

### **5. Run application**

python -m uvicorn main:app --reload

### **6. Access Swagger**

http://127.0.0.1:8000/docs

---

## **Available Endpoints**

- **GET** `/health`
- **POST** `/cashflow`
- **GET** `/cashflow`
- **GET** `/cashflow/summary`

---

## **Example Summary Response**

{
  "total_income": 250.50,
  "total_expense": 100.00,
  "balance": 150.50
}

---

## **Design Decisions**

- Lightweight and fast framework using FastAPI
- PostgreSQL chosen for reliability and relational consistency
- Layered architecture to support future growth
- Docker Compose used for local reproducibility
- Swagger chosen to simplify evaluator testing

---

## **Future Improvements**

- Authentication / Authorization
- Automated unit tests
- Integration tests
- Pagination
- Filters by date range
- Update / Delete endpoints
- CI/CD pipeline
- Cloud deployment
- Monitoring / Observability

---

## **Author**

**Jeferson Loreto**  
Solutions Architect | Senior Systems Analyst
