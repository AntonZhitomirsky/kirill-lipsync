import os
import subprocess
from urllib import parse as urlparse

# Step 1: Install yt-dlp
subprocess.run(['pip', 'install', 'yt-dlp'])

# Step 2: Define YouTube URL and Video ID
YOUTUBE_URL = "https://www.youtube.com/watch?v=ce11vBjNWGs"
url_data = urlparse.urlparse(YOUTUBE_URL)
query = urlparse.parse_qs(url_data.query)
YOUTUBE_ID = query["v"][0]

# Step 3: Download and trim the YouTube video
subprocess.run(['yt-dlp', '-f', 'bestaudio', '-x', '--audio-format', 'mp3', '--audio-quality', '0', '--output', "reference_voice.%(ext)s", f'https://www.youtube.com/watch?v={YOUTUBE_ID}'])

# Step 4: Crop to be at most 5 minutes (this video url is 7 minutes, assume 5 minutes can fit. (if it ain't broke, don't fix it))
subprocess.run(['ffmpeg', '-y', '-i', 'reference_voice.mp3', '-ss', str(0), '-t', str(5*60), '-async', '1', 'reference_voice_cropped.mp3'])