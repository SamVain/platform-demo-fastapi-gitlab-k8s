import os
from datetime import datetime, timezone

from fastapi import FastAPI
from fastapi.responses import JSONResponse

APP_NAME = "platform-demo"
GIT_COMMIT = os.getenv("GIT_COMMIT", "dev")
BUILD_TIME = os.getenv("BUILD_TIME", "dev")
ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

app = FastAPI(title=APP_NAME, version="1.0.0")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/readyz")
def readyz():
    # For demo purposes we just return OK.
    # In a real service you might test downstream dependencies here.
    return {"ready": True}


@app.get("/version")
def version():
    return JSONResponse(
        {
            "app": APP_NAME,
            "environment": ENVIRONMENT,
            "git_commit": GIT_COMMIT,
            "build_time": BUILD_TIME,
            "server_time_utc": datetime.now(timezone.utc).isoformat(),
        }
    )