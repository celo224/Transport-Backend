# TransitFlow+ Backend Starter

This is a multi-service backend for TransitFlow+.

## Services
- gateway_service (8000)
- location_service (8001)
- real_time_api_service (8002)
- safety_threat_detection_service (8003)
- analytics_service (8004)
- user_reports_service (8005)

## Running
```bash
cp .env.example .env
docker compose build
docker compose up
```
