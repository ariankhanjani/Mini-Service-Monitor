import time
import httpx


SERVICES = {
    "user-service": "http://127.0.0.1:8000/mock/user/health",
    "payment-service": "http://127.0.0.1:9999/mock/payment/health",
    "notification-service": "http://127.0.0.1:8000/mock/notification/health",
}


def check_service(name: str, url: str):
    start = time.perf_counter()

    try:
        response = httpx.get(url, timeout=3)

        response_time = round(
            (time.perf_counter() - start) * 1000,
            2
        )

        return {
            "service": name,
            "status": "healthy" if response.is_success else "unhealthy",
            "http_status": response.status_code,
            "response_time_ms": response_time
        }

    except httpx.RequestError as e:
        return {
            "service": name,
            "status": "down",
            "error": str(e)
        }