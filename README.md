# Retail Store — Cloud-Native Microservices Platform

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)](https://kubernetes.io)
[![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=white)](https://aws.amazon.com)

A cloud-native retail platform built as a microservices demo. Designed to demonstrate real-world container platform patterns — service decomposition, Docker Compose for local development, Kubernetes manifests for production, horizontal scaling, and NGINX API gateway routing.

## Services

| Service | Port | Description | Stack |
|---------|------|-------------|-------|
| Catalog | 8080 | Product inventory API | FastAPI, Python |
| Cart | 8081 | Shopping cart management | FastAPI, Python |
| Gateway | 80 | API routing and load balancing | NGINX |

## Architecture

```
                    ┌──────────────────┐
                    │   NGINX Gateway  │ :80
                    └────────┬─────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
    ┌──────────────────┐         ┌──────────────────┐
    │  Catalog Service │ :8080   │   Cart Service   │ :8081
    │  (products API)  │         │  (cart API)      │
    └──────────────────┘         └──────────────────┘
```

## Quick Start — Local (Docker Compose)

```bash
git clone https://github.com/Harishmaranthirumaran/retail-store-sample-app.git
cd retail-store-sample-app
docker compose up --build
```

**API endpoints:**

```bash
# Catalog
curl http://localhost/catalog/products
curl http://localhost/catalog/products/P001

# Cart
curl -X POST "http://localhost/cart/carts?customer_id=user123"
curl http://localhost/cart/carts/{cart_id}

# Health checks
curl http://localhost/health
curl http://localhost/catalog/health
curl http://localhost/cart/health
```

Or use the interactive API docs:
- Catalog: http://localhost:8080/docs
- Cart: http://localhost:8081/docs

## Kubernetes Deployment

```bash
# Create namespace
kubectl apply -f k8s/namespace.yaml

# Deploy services
kubectl apply -f k8s/catalog-deployment.yaml
kubectl apply -f k8s/cart-deployment.yaml
kubectl apply -f k8s/ingress.yaml
kubectl apply -f k8s/hpa.yaml

# Verify
kubectl get pods -n retail-store
kubectl get svc -n retail-store
```

## Project Structure

```
retail-store-sample-app/
├── catalog/
│   ├── main.py            # FastAPI product catalog service
│   ├── Dockerfile
│   └── requirements.txt
├── cart/
│   ├── main.py            # FastAPI cart service
│   ├── Dockerfile
│   └── requirements.txt
├── nginx/
│   └── nginx.conf         # API gateway routing
├── k8s/
│   ├── namespace.yaml
│   ├── catalog-deployment.yaml
│   ├── cart-deployment.yaml
│   ├── ingress.yaml
│   └── hpa.yaml           # Horizontal Pod Autoscaler
├── docker-compose.yml     # Local development stack
└── README.md
```

## Scaling

Both services include Horizontal Pod Autoscalers configured to scale from 2 to 10 replicas at 70% CPU utilisation.

```bash
# Watch pods scale under load
kubectl get hpa -n retail-store -w
```

## Author

**Harishmaran Subbaiah Thirumaran** — DevOps & Platform Engineer, Amsterdam

[linkedin.com/in/harishmaran](https://linkedin.com/in/harishmaran) · [harryportfolio-gamma.vercel.app](https://harryportfolio-gamma.vercel.app)
