from fastapi import status

from errors import AppError

class InvalidQuantityError(AppError):
    status_code = status.HTTP_400_BAD_REQUEST
    error = "INVALID_QUANTITY"
    detail = "The provided quantity cannot be used. Please, try again."



class InvalidDateError(AppError):
    status_code = status.HTTP_400_BAD_REQUEST
    error = "INVALID_DATE"
    detail = "The provided date cannot be used. Please, try again."



class ProductNotFoundError(AppError):
    status_code = status.HTTP_404_NOT_FOUND
    error = "PRODUCT_NOT_FOUND"
    detail = "The requested product cannot be found. Please, try again."