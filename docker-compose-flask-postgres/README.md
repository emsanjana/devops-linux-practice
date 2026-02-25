# Docker Compose – Flask & PostgreSQL Multi-Container Application

## Objective
This project demonstrates how to build and run a multi-container application using Docker Compose.
It consists of a Flask web application and a PostgreSQL database running in separate containers.

---

## Project Structure
devops-linux-practice/docker-compose-flask-postgres/

						├── app/
						│ ├── app.py
						│ ├── requirements.txt
						├── Dockerfile
						├── docker-compose.yml
						├── .env
						└── README.md
---

## Application Overview

- Flask application connects to PostgreSQL
- Creates a simple `users` table
- Inserts one sample record
- Displays database records on the homepage (`/`)
- Uses Docker Compose for orchestration

---
## QUIRES

---
## Why Docker Compose Is Needed

Docker Compose is needed to:
- Run **multiple containers together**
- Define services, networks, and volumes in a single file
- Manage application dependencies easily
- Start the entire application using **one command**

Without Docker Compose, managing multiple containers manually would be complex and error-prone.

---

## Single Container vs Multi-Container Setup

### Single Container Setup
- Application and database run in the same container
- Not scalable
- Hard to maintain
- Violates separation of concerns
- Not suitable for production

### Multi-Container Setup (Using Docker Compose)
- Each service runs in its own container
- Better isolation and maintainability
- Easier scaling
- Services can be updated independently
- Industry best practice

---
## Problems Docker Compose Solves

Docker Compose solves:
- Manual container startup complexity
- Networking issues between containers
- Environment variable management
- Persistent storage configuration
- Service dependency handling
- Reproducibility across environments
