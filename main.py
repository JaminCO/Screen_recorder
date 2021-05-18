import numpy as np
import pyautogui
import cv2 as cv
import datetime
from PIL import ImageGrab

# codec = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
# output = cv.VideoWriter('Recorded.mp4', codec, 60.0, (1920,1080))

# cv.namedWindow("Recording",cv.WINDOW_NORMAL)
# cv.resizeWindow("Recording",1920, 1080)

# while True:
#     img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
#     frame = np.array(img)
#     frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
#     output.write(frame)
#     cv.imshow("Recording", frame)

#     if cv.waitKey(1) == ord("q"):
#         break
# output.release()
# cv.destroyAllWindows()


from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
# print(time_stamp)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

cv.namedWindow("Secret Capture",cv.WINDOW_NORMAL)
cv.resizeWindow("Secret Capture",920, 950)

webcam = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()
    fr_height, fr_width, _ = frame.shape
    # print(fr_height, fr_width)
    img_final[0:fr_height, 0:fr_width, :] = frame[0: fr_height, 0: fr_width, :]
    cv2.imshow("Secret Capture", img_final)

    # cv2.imshow('webcam', frame)

    captured_video.write(img_final)
    if cv2.waitKey(10) == ord("q"):
        break
