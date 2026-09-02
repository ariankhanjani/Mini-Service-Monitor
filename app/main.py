from fastapi import FastAPI, HTTPException
from app.services import SERVICES, check_service

app = FastAPI(title="Mini Service Monitor")


@app.get("/mock/user/health")
def user_health():
    return {
        "service": "user-service",
        "status": "healthy"
    }


@app.get("/mock/payment/health")
def payment_health():
    return {
        "service": "payment-service",
        "status": "healthy"
    }


@app.get("/mock/notification/health")
def notification_health():
    return {
        "service": "notification-service",
        "status": "healthy"
    }
    

# check services

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/services")
def get_services():
    results = []

    for name, url in SERVICES.items():
        results.append(
            check_service(name, url)
        )

    return {
        "services": results
    }
    
    
# endpoint for services

@app.get("/services/{service_name}")
def get_service(service_name: str):

    if service_name not in SERVICES:
        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    return check_service(
        service_name,
        SERVICES[service_name]
    )


# services stats

@app.get("/stats")
def get_stats():

    results = []

    for name, url in SERVICES.items():
        results.append(
            check_service(name, url)
        )

    total = len(results)

    healthy = sum(
        1 for service in results
        if service["status"] == "healthy"
    )

    down = sum(
        1 for service in results
        if service["status"] == "down"
    )

    unhealthy = sum(
        1 for service in results
        if service["status"] == "unhealthy"
    )

    availability = round(
        (healthy / total) * 100,
        2
    ) if total > 0 else 0

    return {
        "total_services": total,
        "healthy": healthy,
        "unhealthy": unhealthy,
        "down": down,
        "availability_percent": availability,
        "services": results
    }