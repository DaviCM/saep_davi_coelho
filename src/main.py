from fastapi import FastAPI
from fastapi.responses import JSONResponse

from errors.app_errors import AppError

app = FastAPI()

@app.exception_handler(AppError)
async def app_exception_handler(exception: AppError):
    return JSONResponse(
        status_code=exception.status_code,
        headers=exception.error,
        content=exception.detail,
    )