class HTTPNotFoundError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = "NotFoundError"
        self.status_code = 404
