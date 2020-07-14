import cv2
import os 
import face_recognition

frames_directory = './frames'
MODEL = 'cnn'
color = [255,255,255]

for filename in os.listdir(frames_directory):
    # Load image
    print(f'Filename {filename}', end='')
    image = face_recognition.load_image_file(f'{frames_directory}/{filename}')
    # This time we first grab face locations - we'll need them to draw boxes
    locations = face_recognition.face_locations(image, model=MODEL)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    for face_location in locations:
        top_left = (face_location[3], face_location[0])
        bottom_right = (face_location[1], face_location[2])

        cv2.rectangle(image, top_left, bottom_right, color)
    
    cv2.imshow(filename, image)
    cv2.waitKey(0)
    cv2.destroyWindow(filename)