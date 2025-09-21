# app/main.py

from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI(
    title="Super-Gemini Tool Server",
    description="A backend server to provide agentic tools for the Super-Gemini project.",
    version="0.1.0",
)

@app.get("/", tags=["Root"])
async def read_root():
    """
    Root endpoint to check if the server is running.
    """
    return {"status": "ok", "message": "Welcome to the Super-Gemini Tool Server!"}
