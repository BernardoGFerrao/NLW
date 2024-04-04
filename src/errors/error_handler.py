
from RocketSeat.NLW.src.http_types.http_response import HttpResponse
from .error_types.http_conflict import HTTPConflictError
from .error_types.http_not_found import HTTPNotFoundError
def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HTTPConflictError, HTTPNotFoundError)):
        return HttpResponse(
            body={
                "error": [{
                    "title": error.name,
                    "details": error.message
                }]
            },
            status_code=error.status_code
        )

    return HttpResponse(
        body={
            "errors":[{
                "title": error,
                "details": str(error)
            }]
        }
    )