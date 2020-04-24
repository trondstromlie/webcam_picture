"""
    A simple python program to display the webcam.
    press q to exit press p to take a picture
    author Trond Strøm Lie
"""

import cv2

#function to take capture a picture from the webcam
#stores grayscale and color picture in folder
def take_picture(color,gray):
    cv2.imwrite("gray_output.jpg", gray)
    cv2.imwrite("rgb_output.jpg", color)
    cv2.imshow("captured image",color)
    cv2.waitKey(0)


video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #opens two windows to display blac&white and rgb video stream
    cv2.imshow("capturing gray", gray)
    cv2.imshow("capturing color", frame)

    key = cv2.waitKey(1)

    #if q is pressed quit
    if key == ord("q"):
        break

    if key == ord("p"):
        take_picture(frame,gray)
        print("capturing photos")



video.release()
cv2.destroyAllWindows()
