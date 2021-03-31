import cv2
import numpy as np

camera = cv2.VideoCapture(0)


while True:
    _, frame = camera.read()

    # define hsv frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit = np.array([11, 134, 183])
    upper_limit = np.array([93, 255, 255])
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    # get contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # draw line around contours
    for contour in contours:
        cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

    # define result frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # show window frame contain live camera video
    cv2.imshow("frame", frame)

    # wait for key every 1 millisecond
    key = cv2.waitKey(1)

    # if keyboard key "q" pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera.release()            
cv2.destroyAllWindows()
exit()
