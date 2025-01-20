# 

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from constants import ENV
from apps.calculator.route import router as calculator_router

# Use Render-provided PORT or default to 8900 for local development
SERVER_URL = "0.0.0.0"  # Bind to all interfaces for deployment
PORT = int(os.getenv("PORT", "8900"))  # Convert to int for uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

# Initialize FastAPI app with lifespan event
app = FastAPI(lifespan=lifespan)

# Enable CORS for all origins (update for production security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def health():
    return {"message": "Server is running"}

# Include calculator routes
app.include_router(calculator_router, prefix="/calculate", tags=["calculate"])

if __name__ == "__main__":
    uvicorn.run("main:app", host=SERVER_URL, port=PORT, reload=(ENV == "dev"))
