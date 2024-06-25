"""Defines the main module"""

# import from standard library
import os
import subprocess

# import from third-party packages
from fastapi import FastAPI
from fastapi import UploadFile
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# declare and initialize the FastAPI app
app = FastAPI()
FastAPIInstrumentor.instrument_app(app)


# define a handler for the "api" endpoint
@app.post("/api/v1/scan")
async def scan(file: UploadFile):
    """Endpoint for scanning files"""
    with open(file.filename, "wb") as tmp:
        tmp.write(await file.read())
    report = subprocess.run(
        ["clamdscan", file.filename], stdout=subprocess.PIPE, check=False
    )
    os.remove(file.filename)
    return report


# define a handler for the healthcheck endpoint
@app.get("/api/v1/ruok")
async def healthcheck():
    """Endpoint to check the health of the API server"""
    return {"status": "imok"}
