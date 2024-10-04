# detection.py
import os
from pubsub import pub

def detect_file():
    user_home = os.path.expanduser('~')
    music_dir = os.path.join(user_home, 'Downloads', 'Music')
    
    for file_name in os.listdir(music_dir):
        if file_name.endswith('.zip'):
            file_path = os.path.join(music_dir, file_name)
            print(f"File detected: {file_path}")
            pub.sendMessage("file_detected", file_path=file_path)
            break
