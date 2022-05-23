import os
import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('/home/faisal/Documents/git_project_72/git_project/Basic_images/elon_musk.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgBill = face_recognition.load_image_file('Basic_images/bill_gates.jpg')
imgBill = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

cv2.imshow('Elon_musk',imgElon)
cv2.waitKey(0)