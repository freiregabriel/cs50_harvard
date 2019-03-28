from pytube import YouTube
import requests
import flask
from typing import Tuple, Any, Optional
from .exceptions import YoutubeError
def download_video(link: Optional[str]) -> Tuple[ Optional[Any], Optional[str] ]:
    """
        Download video from youtube
    """
    # validate
    if not link:
        return None, None

    try:
        # get youtube object for video with details
        yt = YouTube(link)

        # get first stream
        stream = yt.streams.first()

        # get binary from youtube video stream
        binary = requests.get(stream.url, stream=True)

        return binary, yt.title
    except YoutubeError as e:
        raise e
