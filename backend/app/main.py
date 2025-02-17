from typing import Any, Awaitable, Callable

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.responses import Response

from .config import get_settings
from .database import Base, engine
from .utils.error_handlers import (
    generic_exception_handler,
    sqlalchemy_exception_handler,
    validation_exception_handler,
)
from .utils.logger import logger

settings = get_settings()

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="D&D Character Builder API",
    description="API for managing D&D 5E characters and sourcebooks",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(SQLAlchemyError, sqlalchemy_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)


MiddlewareCallable = Callable[[Request], Awaitable[Response]]


@app.middleware("http")  # type: ignore
async def log_requests(request: Request, call_next: MiddlewareCallable) -> Response:
    """Log all incoming requests."""
    logger.info(f"Incoming {request.method} request to {request.url}")
    response = await call_next(request)
    logger.info(f"Returning {response.status_code} response")
    return response


@app.get("/")  # type: ignore
async def root() -> JSONResponse:
    """Root endpoint.

    Returns:
        JSONResponse: Basic API information.
    """
    return JSONResponse({"message": "D&D Character Builder API", "version": "1.0.0"})


@app.get("/health")  # type: ignore
async def health_check() -> JSONResponse:
    """Health check endpoint.

    Returns:
        JSONResponse: Health status of the API.
    """
    logger.info("Health check endpoint called")
    return JSONResponse({"status": "healthy", "message": "API is running"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
