class DomainError(Exception):
    def __init__(self, message: str, *args: object) -> None:
        self.message = message
        super().__init__(message, *args)


class DomainValidationError(DomainError):
    pass


class UnprocessableEntityError(DomainError):
    def __init__(self, message: str):
        super().__init__(message)
