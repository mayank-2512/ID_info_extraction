import sys
import os
import tqdm
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

img_directory = '/home/anshul/Downloads/data'
#ground_truth file
#{class},{x},{y},{w},{h} --> 0,1,2,3

colors = {0:(255,0,0), 1:(255,255,0), 2:(255,128,0), 3:(255,102,255), 4:(51,255,255), 5:(51,51,255), 6:(153,76,0), 7:(0,102,51), 8:(153, 0, 76)}

for i in tqdm.tqdm(os.listdir(img_directory)):
#   print(i)
    classes = pd.read_csv(f'{img_directory}/{i}/ground_truth/classes.txt', header = None).to_dict()[0]

    for j in os.listdir(f'{img_directory}/{i}/ground_truth'):        
        if j == 'classes.txt':
            continue
            
#       print(j)
        gt_name = j
        image_name = gt_name.split('.')[0]+'.jpg'
#       print(f'{img_directory}/{i}/{j}')
        box = pd.read_csv(f'{img_directory}/{i}/ground_truth/{j}', header = None).to_numpy()
#       print('box', box)
        image = cv2.imread(f'{img_directory}/{i}/images/{image_name}')
        w_, h_, c_ = image.shape
        image = cv2.resize(image, (512, 512))

        for k in box:
#           print(list(map(float, k[0].split())))
            class_, x, y, w, h = list(map(float, k[0].split()))
            #w and h after resizing
            w = w*512
            h = h*512
            #Coordinates of top left and bottom right corners of bounding boxes after resizing
            x1 = int(x*512 - w/2)
            y1 = int(y*512 - h/2)
            x2 = int(x*512 + w/2)
            y2 = int(y*512 + h/2)
            new_img = cv2.rectangle(image, (x1,y1), (x2,y2), colors[class_], 2)
            new_img = cv2.putText(new_img, classes[class_], (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1.0, colors[class_], 1, cv2.LINE_AA)
            cv2.imwrite(f'/home/anshul/Downloads/new/{image_name[:-4]}_new.jpg', new_img)
