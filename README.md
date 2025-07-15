# FastAPI with PostgreSQL

This is a containerized FastAPI project with PostgreSQL using Docker.

## 🚀 How to run

### Prerequisites
- Docker
- Docker Compose

### Running with Docker Compose

1. **Clone the repository and navigate to the folder:**
```bash
cd globo-prompt
```

2. **Run the project:**
```bash
docker-compose up --build
```

3. **Access the application:**
- API: http://localhost:8000
- Swagger Documentation: http://localhost:8000/docs
- ReDoc Documentation: http://localhost:8000/redoc

### Useful commands

**Stop containers:**
```bash
docker-compose down
```

**Stop and remove volumes (deletes database data):**
```bash
docker-compose down -v
```

**View logs:**
```bash
docker-compose logs -f app
```

**Run only the database:**
```bash
docker-compose up db
```

## 📊 Available endpoints

- `GET /` - Home page
- `GET /health` - Application health check
- `GET /items/{item_id}` - Example endpoint with parameters
- `GET /docs` - Swagger documentation
- `GET /redoc` - ReDoc documentation

## 🗄️ Database

- **PostgreSQL 15**
- **Port:** 5432
- **Database:** fastapi_db
- **User:** postgres
- **Password:** postgres

## 🔧 Development

For local development without Docker:

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Configure environment variables:**
```bash
cp .env.example .env
```

3. **Run the application:**
```bash
uvicorn main:app --reload
```

## 📁 Project structure

```
globo-prompt/
├── main.py              # FastAPI application
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
├── docker-compose.yml   # Service orchestration
├── .dockerignore        # Files ignored in build
└── README.md           # This file
```

## 🐛 Troubleshooting

**Problem:** Database connection error
- **Solution:** Wait a few seconds for PostgreSQL to fully initialize

**Problem:** Port 8000 already in use
- **Solution:** Change the port in `docker-compose.yml` or stop other services

**Problem:** Docker permission error
- **Solution:** Run with `sudo` or add your user to the docker group 