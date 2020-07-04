import sys
import os
import tqdm
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

img_directory = 'my model/data'
#ground_truth file
#{class},{x},{y},{w},{h} --> 0,1,2,3

for i in tqdm.tqdm(os.listdir(img_directory)):

    classes = pd.read_csv(f'{img_directory}/{i}/ground_truth/classes.txt', header = None).to_dict()[0]

    for j in os.listdir(f'{img_directory}/{i}/ground_truth'):
        cnt = 0
        if j == 'classes.txt':
            continue
        gt_name = j
        image_name = gt_name.split('.')[0]+'.jpg'
        box = pd.read_csv(f'{img_directory}/{i}/ground_truth/{j}', header = None).to_numpy()
        image = cv2.imread(f'{img_directory}/{i}/images/{image_name}')
        w_, h_, c_ = image.shape
        image = cv2.resize(image, (512, 512))

        for k in box:
            class_, x, y, w, h = list(map(float, k[0].split()))
            #w and h after resizing
            w = w*512
            h = h*512
            #Coordinates of top left and bottom right corners of bounding boxes after resizing
            x1 = int(x*512 - w/2)
            y1 = int(y*512 - h/2)
            x2 = int(x*512 + w/2)
            y2 = int(y*512 + h/2)
            crop = image[y1:y2, x1:x2]
            cv2.imwrite(f'my model/crops/{image_name[:-4]}-{classes[class_]}-new.jpg', crop)
