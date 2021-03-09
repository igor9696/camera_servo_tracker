import cv2 as cv


def process_img(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.resize(gray, (500, 300))
    return gray
