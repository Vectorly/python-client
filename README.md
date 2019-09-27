# Vectorly

Vectorly's Python library enables provides a Python wrapper for the [Vectorly API](https://vectorly.io/docs/api/),
enabling you to:

* Upload videos
* List current videos
* Search video
* Download video
* Get detail informaition about video
* Retrieve analytics
* Retrieve events
    
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install vectorly
```

## Getting your API key

To use the library, you will need an API Key. 

You can get your API key in the "Settings page", which you can view by clicking on the user icon in the top-right hand corner. 

![APIkey](https://vectorly.io/docs/img/apikey.png) 


## Usage
```python
import vectorly

API_KEY = '**********************'

def main():
    vectorly_obj = Vectorly(API_KEY)
    vectorly_obj.upload('video_file_pathname')

    search_list = vectorly_obj.search('file_name')
    for file in search_list:
        detail = vectorly_obj.video_detail(file['id'])
        print(detail)

if __name__ == '__main__':
    main()

```

## Methods
The API lets you perform the following operations on your videos

### upload
```python
# create instance of Vectorly class
# default chank_size = 256000
vectorly_obj = Vectorly(API_KEI, chank_size)

# upload file 
vectorly.upload(filename)
```
>API_KEI - your API key  
>chank_size - chank size, default 256000  
>filename - Uploaded file name

### list
Listing videos in Vectorly.
When videos have the status "ready", you can begin playing the video, or you can download it

```python
video_list = vectorly_obj.list()

```

### video_detail
Getting video details by video_id
```python
video_detail = vectorly_obj.video_detail(video_id)
```
>video_id - Video ID

### search
Searching videos
```python
search_list = vectorly_obj.search(search_term)
```
>search_term - searching term

### download
Download the compressed video to your system
```python
vectorly_obj.download(video_id, destination)
```
>video_id - Video ID  
>destination - Destination file

### analytics
Overall summary of video playback over the last 30 days
```python
vectorly_obj.analytics()
```

### events
Retrieve all events from the last 90 days for a particular video
```python
vectorly_obj.events(video_id)
```
>video_id - Video ID, default None

## License
[MIT](https://choosealicense.com/licenses/mit/)
