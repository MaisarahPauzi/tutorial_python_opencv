import cv2
import numpy as np

def nothing(x):
    pass

camera = cv2.VideoCapture(0)

# define trackbars
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L – H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L – S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L – V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U – H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U – S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U – V", "Trackbars", 255, 255, nothing)

while True:
    _, frame = camera.read()

    # define hsv frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get trackbars value
    l_h = cv2.getTrackbarPos("L – H", "Trackbars")
    l_s = cv2.getTrackbarPos("L – S", "Trackbars")
    l_v = cv2.getTrackbarPos("L – V", "Trackbars")
    u_h = cv2.getTrackbarPos("U – H", "Trackbars")
    u_s = cv2.getTrackbarPos("U – S", "Trackbars")
    u_v = cv2.getTrackbarPos("U – V", "Trackbars")

    # append trackbars value to the mask
    # 11, 134, 183, 
    lower_limit = np.array([l_h, l_s, l_v])
    # 93, 255, 255
    upper_limit = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    # define result frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # show window frame contain live camera video
    cv2.imshow("frame", frame)
    # show mask frame
    cv2.imshow("mask", mask)
    # show result frame
    cv2.imshow("result", result)

    # wait for key every 1 millisecond
    key = cv2.waitKey(1)

    # if keyboard key "q" pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
exit()

