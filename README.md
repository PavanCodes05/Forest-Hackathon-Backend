# Backend-Server For AI-Driven Illegal Logging and Poaching Detection System

## Project Structure
```
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── routes
│   │       ├── alerts.py
│   │       ├── authentication.py
│   │       ├── dashboard.py
│   │       ├── devices.py
│   │       └── __init__.py
│   ├── firebase_client.py
│   ├── main.py
│   ├── schemas
│   │   ├── alert.py
│   │   ├── device.py
│   │   └── user.py
│   └── services
│       ├── alert_service.py
│       ├── device_service.py
│       ├── __init__.py
│       └── notification_service.py
```
## Database Structure
```
/users
    /{user_id}
        /name
        /email
        /designation
        /contact no.
        /cases involved
        /cases resolved

/devices
    /{device_id}
        /name
        /location

/alerts
    /{alert_id}
        /device_name
        /type (gunshot, chainsaw, etc.)
        /confidence_score
        /location
        /timestamp
        /status (new, processing, resolved, false_positive)
        /resolved_by (optional)
        /notes (optional)
```
