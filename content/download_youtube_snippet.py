import os
import subprocess
from urllib import parse as urlparse

# Step 1: Install yt-dlp
subprocess.run(['pip', 'install', 'yt-dlp'])

# Step 2: Define YouTube URL and Video ID
YOUTUBE_URL = 'https://www.youtube.com/watch?v=YSacEOigwDc&t=25s'
url_data = urlparse.urlparse(YOUTUBE_URL)
query = urlparse.parse_qs(url_data.query)
YOUTUBE_ID = query["v"][0]

# Trim video (start, end) seconds
start = 6
interval = 11 #  end - start
end = start + interval

# Step 3: Download and trim the YouTube video
subprocess.run(['yt-dlp', '--output', "youtube.%(ext)s", f'https://www.youtube.com/watch?v={YOUTUBE_ID}'])

# Cut the video using FFmpeg
subprocess.run(['ffmpeg', '-y', '-i', 'youtube.mp4', '-ss', str(start), '-t', str(interval), '-async', '1', 'input_vid.mp4'])