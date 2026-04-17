# Cashflow Solution Challenge

## Contexto

Este repositório contém a implementação funcional da proposta arquitetural descrita no repositório complementar:

[desafio-arquiteto-solucoes](https://github.com/jloretos/desafio-arquiteto-solucoes)

## Visão Geral

Solução técnica desenvolvida para o desafio proposto, implementando uma **API de controle de fluxo de caixa simples, escalável e de fácil manutenção**.

A aplicação permite registrar receitas e despesas, listar lançamentos, calcular saldo consolidado e disponibilizar endpoints através de interface Swagger.

---

## **Principais Funcionalidades**

- Registrar transações de **receita** e **despesa**
- Listar todos os lançamentos financeiros
- Gerar resumo consolidado do saldo
- Persistir dados em PostgreSQL
- Documentação interativa via Swagger
- Arquitetura organizada em camadas

---

## **Stack Tecnológica**

- **Python 3**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Docker Compose**
- **Uvicorn**

---

## **Abordagem Arquitetural**

A solução foi estruturada utilizando **separação de responsabilidades**, melhorando manutenção, legibilidade e escalabilidade:

- **Routers** → Endpoints da API
- **Schemas** → Contratos de entrada e saída
- **Services** → Regras de negócio
- **Models** → Entidades de banco de dados
- **Core** → Configurações da aplicação

---

## **Fluxo da Aplicação**

```text
┌──────────────────┐
│ Requisição Cliente│
└────────┬─────────┘
         ▼
┌──────────────────┐
│ FastAPI Router   │
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Camada Service   │
└────────┬─────────┘
         ▼
┌──────────────────┐
│ SQLAlchemy ORM   │
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Banco PostgreSQL │
└────────┬─────────┘
         ▼
┌──────────────────┐
│ Resposta JSON    │
└──────────────────┘
```

---

## **Estrutura do Projeto**

```text
cashflow-solution-challenge/

app/
├── core/        # Configurações da aplicação
├── models/      # Entidades do banco
├── routers/     # Endpoints REST
├── schemas/     # Modelos de entrada/saída
├── services/    # Regras de negócio
└── database.py  # Conexão com banco

main.py
Dockerfile
docker-compose.yml
requirements.txt
.env.example
README.md
```

---

## **Regras de Negócio**

Cada lançamento contém:

- **description**
- **amount**
- **type** (`income` ou `expense`)
- **transaction_date**

Fórmula do saldo:

```text
saldo = total_receitas - total_despesas
```

---

## **Como Executar**

### **1. Clonar o repositório**

```bash
git clone https://github.com/jloretos/cashflow-solution-challenge.git
cd cashflow-solution-challenge
```

### **2. Subir PostgreSQL**

```bash
docker compose up -d
```

### **3. Instalar dependências**

```bash
pip install -r requirements.txt
```

### **4. Criar arquivo .env**

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/cashflow
APP_NAME=Cashflow Solution Challenge
APP_ENV=development
```

### **5. Executar aplicação**

```bash
python -m uvicorn main:app --reload
```

### **6. Acessar Swagger**

```text
http://127.0.0.1:8000/docs
```

---

## **Endpoints Disponíveis**

- **GET** `/health`
- **POST** `/cashflow`
- **GET** `/cashflow`
- **GET** `/cashflow/summary`

---

## **Exemplo de Resumo**

```json
{
  "total_income": 250.50,
  "total_expense": 100.00,
  "balance": 150.50
}
```

---

## **Decisões Técnicas**

- Utilização do FastAPI pela performance e simplicidade
- PostgreSQL pela robustez e consistência relacional
- Arquitetura em camadas visando crescimento futuro
- Docker Compose para reprodutibilidade local
- Swagger para facilitar testes do avaliador

---

## **Melhorias Futuras**

- Autenticação / Autorização
- Testes automatizados
- Testes de integração
- Paginação
- Filtros por período
- Endpoints de atualização e exclusão
- Pipeline CI/CD
- Deploy em nuvem
- Monitoramento / Observabilidade

---

## **Autor**

**Jeferson Loreto**  
Arquiteto de Soluções | Analista de Sistemas Sênior
