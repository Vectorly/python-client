"""
Vectorly Python Client
Vectorly's Python library enables provides a Python wrapper for the API, enabling you to:

    Upload videos in bulk
    List current videos
    Search video
    Download video
    Retrieve analytics

"""

import requests
from io import StringIO
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
    """
    https://vectorly.io/docs/api/
    """
    def __init__(self, api_key, chunk_size=None):
        """
        You can get your API key in the "Settings page"
        :param api_key: your API key
        :param chunk_size: Chunk size
        """

        self.api_key = api_key

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.5',
            'cache-control': 'no-cache',
            'Connection': 'keep-alive',
            'DNT': '1',
            'X-Api-Key': self.api_key,
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
            'upgrade-insecure-requests': '1',
        }

        if chunk_size is None:
            self.chunk_size = 256000
        else:
            self.chunk_size = chunk_size


    def upload(self, filename):
        """
        Upload videos to Vectorly
        :param filename: File name
        :return:
        """
        url = 'https://tus.vectorly.io/files/'
        with open(filename, 'rb') as f:
            tus.upload(f, url, chunk_size=self.chunk_size, metadata={'api_key': self.api_key})
        pass

    def list(self):
        """
        Listing videos in Vectorly
        When videos have the status "ready", you can begin playing the video, or you can download it
        url = https://api.vectorly.io/videos/list
        :return: List of dictionary
        """
        url = 'https://api.vectorly.io/videos/list'
        r = None
        try:
            with requests.session() as s:
                r = s.get(url, headers=self.headers)
                js = r.json()
        except Exception as e:
            raise VectorlyError('Error list video files', r)
        else:
            return js

    def video_detail(self, video_id):
        """
        Getting video details by video_id
        url = https://api.vectorly.io/videos/get/[upload-id]
        :param video_id: Video ID
        :return: Dictionary {'id': str, 'name': str, 'status': str, 'upload_id': str, 'original_size': int, 'private': Bool, 'size': Int}}
        """
        url = f'https://api.vectorly.io/videos/get/{video_id}'
        try:
            with requests.session() as s:
                r = s.get(url, headers=self.headers)
                js = r.json()
        except Exception as e:
            raise VectorlyError('Error get video details', r)
        else:
            return js

    def search(self, search_term):
        """
        Searching videos
        The search term is case insensitive.
        url = https://api.vectorly.io/videos/search/<search-term>
        :param search_term: Search term
        :return: List of matches dictionary
        """

        url = f'https://api.vectorly.io/videos/search/{search_term}'
        try:
            with requests.session() as s:
                r = s.get(url, headers=self.headers)
                js = r.json()
        except Exception as e:
            raise VectorlyError('Error search term', r)
        else:
            return js

    def download(self, video_id, destination):
        """
        url = https://api.vectorly.io/videos/download/<video-id>
        :param video_id: Video ID
        :param destination: Destination file
        :return:
        """

        url = f'https://api.vectorly.io/videos/download/{video_id}'
        try:
            with requests.session() as s:
                with s.get(url, headers=self.headers, stream=True) as r:
                    r.raise_for_status()
                    with open(destination, 'wb') as f:
                        for chunk in r.iter_content(self.chunk_size):
                            f.write(chunk)
        except Exception as e:
            raise VectorlyError('Error download file', r)

    def analytics(self):
        """
        Overall summary of video playback over the last 30 days
        url = https://api.vectorly.io/analytics/summary
        :param video_id: Video ID
        :return:
        """
        pass

    def events(self, video_id=None):
        """
        Retrieve all events from the last 90 days for a particular video
        url = https://api.vectorly.io/analytics/events/video/[video-id]
        :param video_id: Video ID
        :return:
        """