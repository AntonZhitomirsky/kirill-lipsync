import os
import subprocess
from urllib import parse as urlparse

# Step 1: Install yt-dlp
subprocess.run(['pip', 'install', 'yt-dlp'])

# Step 2: Define YouTube URL and Video ID
YOUTUBE_URL = "https://www.youtube.com/watch?v=aYwDs9LTN50"
url_data = urlparse.urlparse(YOUTUBE_URL)
query = urlparse.parse_qs(url_data.query)
YOUTUBE_ID = query["v"][0]

# Step 3: Download and trim the YouTube video
subprocess.run(['yt-dlp', '-f', 'bestaudio', '-x', '--audio-format', 'mp3', '--audio-quality', '0', '--output', "reference_voice.%(ext)s", f'https://www.youtube.com/watch?v={YOUTUBE_ID}'])

subprocess.run(['ffmpeg', '-y', '-i', 'reference_voice.mp3', '-ss', str(4 * 60 + 30), '-t', str(55), '-async', '1', 'reference_voice_cropped.mp3'])