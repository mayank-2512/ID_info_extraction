import json
import os
import cv2
import pytesseract
import numpy as np
import tqdm
from img_to_text import get_string
str = '''
{
  "Document":null,
  "Document_number":null,
  "Name":null,
  "Father_name":null,
  "Address":null,
  "Issue_date":null,
  "State":null,
  "DOB":null,
  "Blood_gp":null
}'''

list_id = [] # total number of id cards but it is empty initially
img_path = 'crops'
# print(os.path.exists('crops'))
for i in tqdm.tqdm(os.listdir(img_path)):
    count = 0
    if i.split('-')[0] not in list_id:
        list_id.append(i.split('-')[0])
# print(len(list_id))
for i in list_id:
    data = json.loads(str) #it is a python dictionary
    for j in os.listdir(img_path):
        if j.split('-')[0] == i:
            result, class_ = get_string(img_path +'/'+ j)
            data[class_] = result
    temp = data.copy()
    # print(data)
    for k in temp:
        if temp[k]==None:
            del data[k]
    # print(data)
    with open(f"{i}_output", 'w') as f:
        json.dump(data, f, indent = 2)
