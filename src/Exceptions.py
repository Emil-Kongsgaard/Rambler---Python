class TextEventError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

class UIError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)