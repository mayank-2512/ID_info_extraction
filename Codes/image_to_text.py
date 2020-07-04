import cv2
import os
import pytesseract
import numpy as np
def get_string(img_path):
    # Read image using opencv
    img_name = img_path.split("/")[-1]
    class_ = img_name.split('-')[1]
    img = cv2.imread(img_path)

    #otsu algorithm
    img2 = cv2.resize(img, None, fx=6, fy=6, interpolation=cv2.INTER_CUBIC)
    img3 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img4 = cv2.threshold(img3, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

    result = pytesseract.image_to_string(img4)

    return result, class_
