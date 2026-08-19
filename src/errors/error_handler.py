from src.views.http_types.http_response import HttpResponse
from .erros_types.http_bad_request import HttpBadRequestError
from .erros_types.http_not_found import HttpNotFoundError
from .erros_types.http_unprocessable_entity import HttpUnprocessableEntityError


def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(
        error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)
    ):
        return HttpResponse(
            satus_code=error.status_code,
            body={"erros": [{"title": error.name, "detail": error.message}]},
        )

    return HttpResponse(
        satus_code=500,
        body={"erros": [{"title": "Server Error", "detail": str(error)}]},
    )
