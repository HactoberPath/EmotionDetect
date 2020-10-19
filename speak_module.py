from gtts import gTTS
import random
import os
import numpy as np
import cv2
import time
import datetime

from utils import CFEVideoConf, image_resize
import glob

def speek(rand,n,mixer):
    tts = gTTS(text=random.choice(rand), lang='en')                 
    tts.save('jarvis'+str(n)+'.mp3')
    mixer.init()
    mixer.music.load('jarvis'+str(n)+'.mp3')
    mixer.music.play()

def wifi():
    REMOTE_SERVER = "www.google.com"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False



if not os.path.exists(timelapse_img_dir):
    os.mkdir(timelapse_img_dir)

now = datetime.datetime.now()
finish_time = now + datetime.timedelta(seconds=seconds_duration)
i = 0
while datetime.datetime.now() < finish_time:
    '''
    Ensure that the current time is still less
    than the preset finish time
    '''
    ret, frame      = cap.read()
    filename        = f"{timelapse_img_dir}/{i}.jpg"
    i               += 1
    cv2.imwrite(filename, frame)
    time.sleep(seconds_between_shots)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


def images_to_video(out, image_dir, clear_images=True):
    image_list = glob.glob(f"{image_dir}/*.jpg")
    sorted_images = sorted(image_list, key=os.path.getmtime)
    for file in sorted_images:
        image_frame  = cv2.imread(file)
        out.write(image_frame)
    if clear_images:
        '''
        Remove stored timelapse images
        '''
        for file in image_list:
            os.remove(file)

images_to_video(out, timelapse_img_dir)
# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
