from flask import Blueprint, render_template, jsonify, request, Response
from .settings import VERSION
from pytube import YouTube
import requests
import flask
from typing import Tuple, Any, Optional
from .exceptions import YoutubeError, InvalidUsage

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

# Blueprint
youtube_blueprint = Blueprint('youtube_blueprint', __name__, template_folder='templates')

# PAGE
@youtube_blueprint.route("/youtube_video_downloader")
def youtube_page() -> Any:
    """
    youtube page
    """
    return render_template("youtube.html", version=VERSION)

# API
@youtube_blueprint.route('/download', methods=["GET"])
def download_by_id() -> Any:
    """
    Download an youtube video
    """
    try:
        url: Optional[str] = request.args.get('url')

        # validate
        if not url:
            raise InvalidUsage("No URL was passed", 400)

        # get video binary and video title from youtube api
        binary, title = download_video(url)

        # validate
        if not binary or not title:
            raise YoutubeError()

        return Response(binary, headers={'Content-Disposition': 'attachment; '
                                        'filename=' + f"{title}.mp4"})
    except YoutubeError as e:
        raise e
