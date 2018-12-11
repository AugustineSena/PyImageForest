from __future__ import print_function

import argparse

import cv2
from rgbhistogram import RGBHistogram
from sklearn.externals import joblib

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the flower image that ready to classify")
ap.add_argument("-m", "--mask", required=True, help="path to the flower image mask")
args = vars(ap.parse_args())

model = joblib.load("model.pyc")
label = joblib.load("label.pyc")
desc = RGBHistogram([8, 8, 8])
imagePath = args["image"]
image = cv2.imread(imagePath)
mask = cv2.imread(args["mask"])

mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

features = desc.describe(image, mask)
flowerindex = model.predict([features])
flower = label.inverse_transform(flowerindex)[0]
print(imagePath)
decisiontext = "I think this flower is a {}".format(flower.upper())
print(decisiontext)
height, width, channels = image.shape
cv2.putText(image,decisiontext,(10,height-20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv2.imshow("image", image)
cv2.waitKey(0)

