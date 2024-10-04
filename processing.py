# processing.py
import os
import zipfile
from pubsub import pub

def process_file(file_path):
    user_home = os.path.expanduser('~')
    music_dir = os.path.join(user_home, 'Downloads', 'Music')
    
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(music_dir)
        print(f"Extracted {file_path} to {music_dir}")

def listener(file_path):
    process_file(file_path)

pub.subscribe(listener, "file_detected")
