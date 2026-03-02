# Kubernetes – Flask & PostgreSQL Application

## Architecture Overview

- Flask application runs in multiple Pods
- PostgreSQL runs in a single Pod
- Services provide stable networking
- Kubernetes handles scaling and self-healing

---

## Kubernetes Components Explained

### Pod
A Pod is the smallest deployable unit in Kubernetes.
- It can contain one or more containers
- Each Pod has its own IP address
- Pods are ephemeral and can be recreated

Example:
- One Pod runs Flask
- One Pod runs PostgreSQL

---

### Deployment
A Deployment manages Pods declaratively.
- Ensures the desired number of Pods are running
- Handles scaling and updates
- Automatically recreates failed Pods

Example:
- Flask Deployment with 3 replicas
- PostgreSQL Deployment with 1 replica

---

### ReplicaSet
A ReplicaSet ensures the specified number of Pod replicas are running.
- Created automatically by a Deployment
- Rarely managed directly by users

Example:
- Flask ReplicaSet maintaining 3 Pods

---

### Service
A Service provides a stable network endpoint.
- Abstracts Pod IPs
- Enables service discovery using DNS
- Load-balances traffic across Pods

Types used:
- ClusterIP (PostgreSQL)
- NodePort (Flask)

---

## Application Communication

- Flask connects to PostgreSQL using:
host=postgres

- Kubernetes DNS resolves the Service name
- No hard-coded IPs required

---

## Scaling Demonstration

The Flask application was scaled using: kubectl scale deployment flask-app --replicas=3

Results:
- 3 Flask Pods running
- Service load-balances traffic automatically
- No downtime during scaling

---

## Docker Compose vs Kubernetes

| Feature | Docker Compose | Kubernetes |
|------|----------------|------------|
| Scope | Local development | Production-grade orchestration |
| Scaling | Manual | Built-in |
| Self-healing | No | Yes |
| Load balancing | Basic | Advanced |
| Networking | Simple | Advanced |
| Configuration | docker-compose.yml | Multiple YAML resources |

---

## Conclusion

Kubernetes provides:
- High availability
- Scalability
- Self-healing
- Declarative configuration

This makes Kubernetes suitable for production deployments, while Docker Compose is ideal for local development and testing.

