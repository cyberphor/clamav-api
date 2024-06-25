"""Defines the API for ClamD"""

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
    upload_file_path = f"/tmp/{file.filename}"
    with open(upload_file_path, "wb") as upload_file:
        upload_file.write(await file.read())
    report = subprocess.run(
        ["clamdscan", upload_file_path], stdout=subprocess.PIPE, check=False
    )
    os.remove(upload_file_path)
    match report.returncode:
        case 0:
            return "benign"
        case 1:
            return "malicious"
        case 2:
            return "error"

# define a handler for the healthcheck endpoint
@app.get("/api/v1/ruok")
async def healthcheck():
    """Endpoint to check the health of the API server"""
    return "imok"
