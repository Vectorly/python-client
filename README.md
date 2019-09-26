# vectorly
Python library for uploading, compressing and streaming videos using Vectorly's stream product

class Vectorly(__builtin__.object)
   	https://vectorly.io/docs/api/
The API lets you perform the following operations on your videos:
    upload
    list
    video_detail
    search
    download
    analytics
    events
 
 	Methods defined here:
__init__(self, api_key, chunk_size=None)
You can get your API key in the "Settings page"
:param api_key: your API key
:param chunk_size: Chunk size
analytics(self)
Overall summary of video playback over the last 30 days
url = https://api.vectorly.io/analytics/summary
:return:
download(self, video_id, destination)
Download the compressed video to your system
url = https://api.vectorly.io/videos/download/<video-id>
:param video_id: Video ID
:param destination: Destination file
:return:
events(self, video_id=None)
Retrieve all events from the last 90 days for a particular video
url = https://api.vectorly.io/analytics/events/video/[video-id]
:param video_id: Video ID
:return:
list(self)
Listing videos in Vectorly
When videos have the status "ready", you can begin playing the video, or you can download it
url = https://api.vectorly.io/videos/list
:return: List of dictionary
search(self, search_term)
Searching videos
The search term is case insensitive.
url = https://api.vectorly.io/videos/search/<search-term>
:param search_term: Search term
:return: List of matches dictionary
upload(self, filename)
Upload videos to Vectorly
:param filename: File name
:return:
video_detail(self, video_id)
Getting video details by video_id
url = https://api.vectorly.io/videos/get/[upload-id]
:param video_id: Video ID
:return: Dictionary {'id': str, 'name': str, 'status': str, 'upload_id': str, 'original_size': int, 'private': Bool, 'size': Int}}
Data descriptors defined here:
__dict__
dictionary for instance variables (if defined)
__weakref__
list of weak references to the object (if defined)
