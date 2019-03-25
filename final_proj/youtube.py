from pytube import YouTube
import requests
import flask
from typing import Tuple, Any, Optional

def download_video(link: Optional[Any]) -> Tuple[Any,str]:
    yt = YouTube(link)
    stream = yt.streams.first()
    binary = requests.get(stream.url, stream=True)
    return binary, yt.title
