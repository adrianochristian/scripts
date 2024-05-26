#Organize all the files in the Downloads folder into Images, Videos and Audios folders
import os
from pathlib import Path

home = str(Path.home())

def create_folders():
    if not os.path.exists(home + '/Downloads/Images'):
        os.mkdir(home + '/Downloads/Images')

    if not os.path.exists(home + '/Downloads/Videos'):
        os.mkdir(home + '/Downloads/Videos')

    if not os.path.exists(home + '/Downloads/Audios'):
        os.mkdir(home + '/Downloads/Audios')

    if not os.path.exists(home + '/Downloads/Compacted'):
        os.mkdir(home + '/Downloads/Compacted')
    

def organize():
    files = os.listdir(os.path.dirname(home + '/Downloads/'))

    create_folders()
    
    for file in files:
        if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            os.rename(home + '/Downloads/' + file, home + '/Downloads/Images/' + file)
        elif file.endswith(('.MP4', '.avi', '.flv', '.wmv', '.mov')):
            os.rename(home + '/Downloads/' + file, home + '/Downloads/Videos/' + file)
        elif file.endswith(('.mp3', '.wav', '.flac', '.aac')):
            os.rename(home + '/Downloads/' + file, home + '/Downloads/Audios/' + file)
        elif file.endswith(('.zip', '.rar', '.tar', '.gz', '.7z')):
            os.rename(home + '/Downloads/' + file, home + '/Downloads/Compacted/' + file)
organize()