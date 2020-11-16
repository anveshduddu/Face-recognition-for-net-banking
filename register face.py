import cv2
import os
import random

path = 'C:\\Users\\anves\\PycharmProjects\\flaskProject\\faces'
os.chdir(path)
print("Enter ur name")
newfolder= input()
os.makedirs(newfolder)

print("[LOG] Opening webcam ...")
path = 'C:\\Users\\anves\\PycharmProjects\\flaskProject\\faces\\'+newfolder
cam = cv2.VideoCapture(0)

value= random.randint(111,999)
img_counter = value

while True:
    ret, frame = cam.read()
    if not ret:
        break
    cv2.imshow('frame', frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        break
    elif k % 256 == 32:
        img_name =  newfolder  + "_{}.jpg".format(img_counter)
        cv2.imwrite(os.path.join(path,img_name), frame)
        img_counter += 1

cam.release()
cv2.destroyAllWindows()