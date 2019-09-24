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
    def __init__(self, api_key):
        """
        You can get your API key in the "Settings page"
        :param api_key - your API key:
        """
        self.api_key = api_key
        pass

    def upload(self, filename):
        """
        Upload videos to Vectorly
        :param filename:
        :return:
        """
        pass

    def list(self):
        pass

    def search(self, search_term):
        pass

    def download(self, video_id, destination):
        pass

    def analytics(self, video_id=None):
        pass
