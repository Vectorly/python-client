import requests
import tus


class VectorlyError(Exception):
    def __init__(self, message, response=None):
        super().__init__(message)
        self.response = response
        self.message = message

    def __str__(self):
        if self.response is not None:
            text = self.response.text
            return f'VectorlyError({self.message}, response=({self.response.status_code}, {text.strip()}))'
        else:
            return f'VectorlyError({self.message})'


class Vectorly(object):

    def __init__(self):
        pass

