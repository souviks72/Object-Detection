# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:32:16 2020

@author: Souvik M
"""


import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt

options = {
    'model' : 'cfg/yolo.cfg',
    'load': 'bin/yolov2.weights',
    'threshold': 0.3,
    'gpu': 1.0
}

tfnet = TFNet(options)

import numpy as np
img = cv2.imread('dog.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
result = tfnet.return_predict(img)
print(result)

tl = (result[0]['topleft']['x'], result[0]['topleft']['y'])
br = (result[0]['bottomright']['x'], result[0]['bottomright']['y'])
label = result[0]['label']

img = cv2.rectangle(img,tl,br,(0,255,0),7)
img = cv2.putText(img,label,tl,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
plt.imshow(img)
plt.show()

print(tl)
print(br)
print(label)
