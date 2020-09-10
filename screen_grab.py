import time
from datetime import datetime
import pyscreenshot as ImageGrab
import numpy as np
import cv2

frame_directory = "frames/"

while True:
    now = datetime.now()
    img = ImageGrab.grab()
    file_name = now.strftime("%d_%m_%Y_%H_%M_%s.jpg")
    img.save(frame_directory + file_name)
    print('Capturing...')
    print(time)
    time.sleep(10) 


