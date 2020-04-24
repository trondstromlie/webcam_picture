"""
    A simple python program to display the webcam.
    Press q to exit press space to take a picture.
    Author Trond Strøm Lie
"""

import cv2

images = 0
#function to  capture a picture
#stores two jpg files, grayscale and color in folder
def take_picture(color,gray):
    global images
    cv2.imwrite("gray_output{}.jpg".format(images), gray)
    cv2.imwrite("color_output{}.jpg".format(images), color)
    cv2.imshow("captured image",color)
    cv2.waitKey(100)
    images += 1

#start the camera OBJECT
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#while loop to show the video stream

while True:

    #open camera
    check, frame = video.read()

    #convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #opens two windows to display grayscale and color video stream
    cv2.imshow("capturing gray", gray)
    cv2.imshow("capturing color", frame)

    key = cv2.waitKey(1)
    #if q is pressed quit
    if key == ord("q"):
        break
    #if spacebar is pressed take picture with take_picture function
    if key == 32: #32 == spacebar
        take_picture(frame,gray)
        print("capturing photos")



#exit
video.release()
cv2.destroyAllWindows()
