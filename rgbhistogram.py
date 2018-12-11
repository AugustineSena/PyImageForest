import cv2
from matplotlib import pyplot as plt
import numpy as np


class RGBHistogram:
    def __init__(self, bins):
        self.bins = bins

    def describe(self, image, mask=None, imageName=None):
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
                            [0, 256, 0, 256, 0, 256])
        # normalize histogram
        cv2.normalize(hist, hist)
        # draw histogram before flatten()
        # color = ('b', 'g', 'r')
        # for i, col in enumerate(color):
        #     plt.plot(hist[i], color=col)
        #     plt.xlim([0, self.bins[i] - 1])
        #     plt.title(imageName)
        # plt.show()
        # end draw
        # flatten to one array descriptor
        return hist.flatten()
