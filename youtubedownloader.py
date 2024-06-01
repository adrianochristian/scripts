#A simple YouTube Downloader using pytube to download videos and audio
from pytube import YouTube
from pathlib import Path
from pytube.innertube import _default_clients

_default_clients['ANDROID_MUSIC'] = _default_clients['WEB']

def download(url, type='video'):
    try:
        yt = YouTube(url)

        if type == 'video' or type == 'v':
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        elif type == 'audio' or type == 'a':
            stream = yt.streams.filter(only_audio=True).first()
        else:
            print("Invalid Type")
            return
        
        stream.download(output_path=str(Path.home()) + "/Downloads")
        print(f"Download completed: {stream.default_filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = input("Video URL: ")
    type = input("Video or Audio: ").strip().lower()
    download(url, type)

main()
