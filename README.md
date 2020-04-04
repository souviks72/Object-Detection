# Object-Detection
This repo has two folders, one for SSD or Single Shot Multibox Detector and another for YOLO.
The SSD project is simple. I used pretrained weights and OpenCV to perform object detection.
The YOLO project is a little more detailed.
It has files to use YOLO on images,videos and real time feed(via webcam). YOLO depends on darknet. I used the publicly available YOLO 
network from "https://github.com/thtrieu/darkflow". 
First we need to build the darkflow net . 
Use the command "python3 setup.py build_ext --inplace"
In order to train it on custom dataset:
  1. download images using the get_images file and create annotations as needed(see the draw annotations file). 
  2. follow the rest of the instructions from the original repo
   
