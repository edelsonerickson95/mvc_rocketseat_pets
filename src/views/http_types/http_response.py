class HttpResponse:
    def __init__(self, satus_code: int, body: dict = None) -> None:
        self.status_code = satus_code
        self.body = body
