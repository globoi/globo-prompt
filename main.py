import uvicorn
from src.core.config import settings

def run_api():
    from src.presentation.api.main import app
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)

if __name__ == "__main__":
    run_api()


