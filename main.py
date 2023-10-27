import cv2
import os

path = './videos'

def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)
    count = 0
    sucess = 1

    while sucess:
        sucess, image = vidObj.read()

        cv2.imwrite("frame%d.jpg" % count, image)

        count += 1
    
    
if __name__ == '__main__':
    for filename in os.listdir(path):
        FrameCapture(f'{path}/{filename}')