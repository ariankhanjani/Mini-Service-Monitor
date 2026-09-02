# Mini Service Monitor

A lightweight service monitoring API built with **FastAPI**.

The project checks the health and availability of multiple services, measures response time, and provides basic service statistics.

## Features

* Service health checks
* Detect `healthy`, `unhealthy`, and `down` services
* Response time monitoring
* Check individual services
* Overall service statistics
* REST API testing with Postman
* Dockerized application

## Tech Stack

* Python 3.10
* FastAPI
* Uvicorn
* HTTPX
* Docker
* Postman

## Project Structure

```text
mini-service-monitor/
├── app/
│   ├── main.py
│   └── services.py
├── Dockerfile
└── requirements.txt
```

## API Endpoints

| Method | Endpoint                   | Description              |
| ------ | -------------------------- | ------------------------ |
| GET    | `/health`                  | Monitor health check     |
| GET    | `/services`                | Check all services       |
| GET    | `/services/{service_name}` | Check a specific service |
| GET    | `/stats`                   | Get service statistics   |

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m uvicorn app.main:app --reload --port 8000
```

API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Run with Docker

Build the image:

```bash
docker build -t mini-service-monitor .
```

Run the container:

```bash
docker run -p 8000:8000 mini-service-monitor
```

## Example

Request:

```http
GET /services
```

Example response:

```json
{
  "services": [
    {
      "service": "user-service",
      "status": "healthy",
      "http_status": 200,
      "response_time_ms": 12.4
    }
  ]
}
```

## Project Goal

This project is a small practical exercise focused on:

* API development
* Service monitoring
* Troubleshooting
* HTTP communication
* Basic infrastructure concepts
* Containerization
