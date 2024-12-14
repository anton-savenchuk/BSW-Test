from src.core.exception import BaseHTTPException, status


class BetCannotBePlace(BaseHTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Event cannot be place"
