# DevSolutions Ltd - DevOps Challenge

## Project Overview

This project containerizes a Flask Web Application connected to a Redis Database. It utilizes Docker for containerization, Docker Compose for multi-service orchestration, Kubernetes for production-grade deployment, and Jenkins for CI/CD automation.

## Tech Stack

- **Language:** Python 3.9 (Flask)
- **Database:** Redis
- **Container:** Docker
- **Orchestration:** Kubernetes
- **CI/CD:** Jenkins

## How to Run

### Phase 1 & 3: Docker Compose

1. `docker-compose up --build`
2. Access app at `http://localhost:5000` (Counter works)

### Phase 2: Kubernetes

1. `kubectl apply -f kubernetes/`
2. Access app via NodePort at `http://localhost:30005`

### Phase 4: Jenkins

1. Trigger the "DevSolutions-Pipeline" job.
2. Deployment is automatically updated on K8s cluster.
