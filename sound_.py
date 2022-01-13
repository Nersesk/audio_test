import os
import time
from mutagen.mp3 import MP3
import json
audio_s={}
folder_path=os.path.join(os.getcwd(),'audio')
folder=os.listdir(folder_path)
folder_dir=os.getcwd()
os.chdir('audio')
for files in folder:
    if files.endswith('mp3'):
        audio=MP3(files)
        os.startfile(files)
        audio_duration=audio.info.length
        time.sleep(audio_duration)
        rate=input('How you rate this audio (n/c)?: ')
        if rate=='n' or rate=='c':
            audio_s[files]=rate
        else:
            raise Exception('Wrong input')

audio_json=json.dumps(audio_s,indent=2)
json_path=os.path.join(folder_dir,'audio_ratings.json')
with open(json_path,'a+') as json_file:
    json_file.write(audio_json)
print(audio_s)

