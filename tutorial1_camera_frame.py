import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    _, frame = camera.read()

    # show window frame contain live camera video
    cv2.imshow("frame", frame)

    # wait for key every 1 millisecond
    key = cv2.waitKey(1)

    # if keyboard key "q" pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
exit()

