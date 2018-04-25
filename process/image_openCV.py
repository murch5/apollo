from process.process import Process
import cv2
import numpy as np

class AdaptiveThreshold(Process):

    def do(self,data):
        out = data

        out = cv2.adaptiveThreshold(data,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,21,4)

        return out

class Threshold(Process):

    def do(self, data):
        out = data

        thresh = self.get("thresh")

        out = cv2.threshold(data,thresh,1,cv2.THRESH_BINARY)

        return out[1]


class Open(Process):

    def do(self,data):
        out = data

        kernel = np.ones((5,5),np.uint8)
        out = cv2.morphologyEx(data,cv2.MORPH_OPEN,kernel)

        return out

class Convert(Process):

    def do(self,data):
        out = data

        out = cv2.cvtColor(data,cv2.COLOR_BGR2GRAY)
        return out

class GaussianBlur(Process):

    def do(self,data):
        out = data

        out = cv2.GaussianBlur(data, (3,3),0)

        return out

class BlobDetection(Process):

    def do(self, data):
        out = data

        params = cv2.SimpleBlobDetector_Params()

        params.thresholdStep = 0
        params.minThreshold = 1
        params.maxThreshold = 2
        params.minRepeatability = 1
        params.minDistBetweenBlobs = 10

        params.filterByColor = 0
        params.blobColor = 1

        params.filterByArea = False

        params.filterByConvexity = 0
        params.minConvexity = 0.87

        params.filterByInertia = 0
        params.minInertiaRatio = 0.08

        detector = cv2.SimpleBlobDetector_create(params)

        blobs = detector.detect(data)

        out = blobs



        return out