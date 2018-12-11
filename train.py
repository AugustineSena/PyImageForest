from __future__ import print_function
from rgbhistogram import RGBHistogram
from flowerdictionary import FlowerDictionary
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.externals import joblib
from sklearn.tree import export_graphviz
import graphviz
from graphviz import Source
import os
from sklearn import tree
import numpy as np
import argparse
import glob
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to the image dataset")
ap.add_argument("-m", "--masks", required=True, help="path to the image masks")
args = vars(ap.parse_args())

imagePaths = sorted(glob.glob(args["images"] + "/*.jpg"))
maskPaths = sorted(glob.glob(args["masks"] + "/*.png"))

data = []
target = []

desc = RGBHistogram([8, 8, 8])
labels = FlowerDictionary()

for (imagePath, maskPath) in zip(imagePaths, maskPaths):
    image = cv2.imread(imagePath)
    mask = cv2.imread(maskPath)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    features = desc.describe(image, mask, imagePath)

    # if cv2.waitKey(100) & 0xFF == ord('q'):
    #     break
    # cv2.waitKey(0)
    data.append(features)
    target.append(labels.getlabel(imagePath))

targetNames = np.unique(target)
le = LabelEncoder()
target = le.fit_transform(target)

(trainData, testData, trainTarget, testTarget) = train_test_split(data, target, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=25, random_state=84)
fit = model.fit(trainData, trainTarget)

print(classification_report(testTarget, model.predict(testData), target_names=targetNames))

# i_tree = 0
# for tree_in_forest in model.estimators_:
#     with open('tree_' + str(i_tree) + '.dot', 'w') as my_file:
#         my_file = tree.export_graphviz(tree_in_forest, out_file=my_file)
#     i_tree = i_tree + 1
# print('please visit http://www.webgraphviz.com/ to read dot file')

# joblib.dump(fit, "model.pyc")
# joblib.dump(le, "label.pyc")
