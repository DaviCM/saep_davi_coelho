from fastapi import status

from errors import AppError

class UserAlreadyExistsError(AppError):
    status_code = status.HTTP_400_BAD_REQUEST
    error = "USER_ALREADY_EXISTS"
    detail = "The provided information is already associated with an user. Please, log in or try again."



class UserNotFoundError(AppError):
    status_code = status.HTTP_404_NOT_FOUND
    error = "USER_NOT_FOUND"
    detail = "The requested user cannot be found. Please, try again."



class WrongUserInfoError(AppError):
    status_code = status.HTTP_400_BAD_REQUEST
    error = "WRONG_USER_INFO"
    detail = "The requested user cannot be found. Please, try again."