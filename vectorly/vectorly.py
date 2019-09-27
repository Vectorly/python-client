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
import tus


class VectorlyError(Exception):

    def __init__(self, message, response=None):
        super().__init__(message)
        self.response = response
        self.message = message

    def __str__(self):
        if self.response is not None:
            return 'VectorlyError({message}, response={status_code}, {text})'.format(message=self.message,
                                                                                   status_code=self.response.status_code,
                                                                                   text=self.response.text.strip())
        else:
            return 'VectorlyError({message})'.format(message=self.message)


class Vectorly(object):
    """
    https://vectorly.io/docs/api/
    The API lets you perform the following operations on your videos:
        - upload
        - list
        video_detail
        search
        download
        analytics
        events
    """
    def __init__(self, api_key, chunk_size=None):
        """
        Getting your API key
        To use the library, you will need an API Key.
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
        try:
            with requests.session() as s:
                with s.get(url, headers=self.headers) as r:
                    r.raise_for_status()
                    js = r.json()
                    return js
        except Exception as e:
            raise VectorlyError('Error list video files', r)

    def video_detail(self, video_id):
        """
        Getting video details by video_id
        url = https://api.vectorly.io/videos/get/[upload-id]
        :param video_id: Video ID
        :return: Dictionary {'id': str, 'name': str, 'status': str, 'upload_id': str, 'original_size': int, 'private': Bool, 'size': Int}}
        """
        url = 'https://api.vectorly.io/videos/get/{video_id}'.format(video_id=video_id)
        try:
            with requests.session() as s:
                with s.get(url, headers=self.headers) as r:
                    r.raise_for_status()
                    js = r.json()
                    return js
        except Exception as e:
            raise VectorlyError('Error get video details', r)

    def search(self, search_term):
        """
        Searching videos
        The search term is case insensitive.
        url = https://api.vectorly.io/videos/search/<search-term>
        :param search_term: Search term
        :return: List of matches dictionary
        """

        url = 'https://api.vectorly.io/videos/search/{search_term}'.format(search_term=search_term)
        try:
            with requests.session() as s:
                with s.get(url, headers=self.headers) as r:
                    r.raise_for_status()
                    js = r.json()
                    return js
        except Exception as e:
            raise VectorlyError('Error search term', r)

    def download(self, video_id, destination):
        """
        Download the compressed video to your system
        url = https://api.vectorly.io/videos/download/<video-id>
        :param video_id: Video ID
        :param destination: Destination file
        :return:
        """

        url = 'https://api.vectorly.io/videos/download/{video_id}'.format(video_id=video_id)
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
        :return:
        """

        url = 'https://api.vectorly.io/analytics/summary/'
        try:
            with requests.session() as s:
                with s.get(url, headers=self.headers) as r:
                    r.raise_for_status()
                    js = r.json()
                    return js
        except Exception as e:
            raise VectorlyError('Error get analytics', r)

    def events(self, video_id=None):
        """
        Retrieve all events from the last 90 days for a particular video
        url = https://api.vectorly.io/analytics/events/video/[video-id]
        :param video_id: Video ID
        :return:
        """
        if video_id is not None:
            url = 'https://api.vectorly.io/analytics/events/video/{video_id}'.format(video_id=video_id)
        else:
            url = 'https://api.vectorly.io/analytics/events/video/'
        try:
            with requests.session() as s:
                with s.get(url, headers=self.headers) as r:
                    r.raise_for_status()
                    js = r.json()
                    return js
        except Exception as e:
            raise VectorlyError('Error get events', r)