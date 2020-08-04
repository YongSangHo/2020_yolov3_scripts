import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

src_file = sys.argv[1]
src_label = sys.argv[2]

src = cv2.imread(src_file,cv2.IMREAD_COLOR)
src_file2 = "holo.jpg"
src2 = cv2.imread(src_file2,cv2.IMREAD_COLOR)
f = open(src_label,'r')

lines = f.readlines()
for i in range(len(lines)):
	if lines[i][0] != '0':
		parse = lines[i].split(" ")
		idx = float(parse[i][0])
		x = float(parse[1])
		y = float(parse[2])
		wid = float(parse[3])
		parse[4].rstrip("\n")
		hei = float(parse[4])
		break;

x1 = int(x*src.shape[1])
y1 = int(y*src.shape[0])
h = int(wid*src.shape[1])
w = int(hei*src.shape[0])

x2 = int(x1 + h)
y2 = int(y1 + w)

a = x1 - int(h/2)
b = y1 - int(w/2)

c = x2 - int(h/2)
d = y2 - int(w/2)

patch = np.zeros((src.shape),dtype = np.uint8)*255
src2 = cv2.resize(src2,dsize=(c-a+350,d-b+350))
patch[b-175:d+175,a-175:c+175] = src2[0:d-b+350,0:c-a+350]
patch = np.where(patch==0,np.uint8(src*0.4),patch)
dst = cv2.addWeighted(src,0.5,patch,0.5,50)

cv2.imwrite("reflection_"+src_file,dst)



