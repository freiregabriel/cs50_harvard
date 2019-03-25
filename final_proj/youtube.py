import pytube
import requests
import flask

def download_video(link):
    yt = pytube.YouTube(link)
    stream = yt.streams.first()
    binary = requests.get(stream.url, stream=True)
    return binary, yt.title
