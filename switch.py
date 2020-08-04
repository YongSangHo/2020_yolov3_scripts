import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

#src_file = sys.argv[1]
src_label = sys.argv[1]
#src_file = "23.jpg"
#src_label = "23.txt"
#src = cv2.imread(src_file,cv2.IMREAD_COLOR)
#src = cv2.cvtColor(src,cv2.COLOR_RGB2BGR)
f = open(src_label,'r')

lines = f.readlines()
#f1 = open("ratio_"+sys.argv[1],'w')
f1 = open(src_label,'w')
#f2 = open("resized_"+sys.argv[1],'w')
#f2 = open("resized_"+src_label,'w')
for i in range(len(lines)):
        if lines[i][0] != '9':
            parse = lines[i].split(" ")
            idx = (lines[i][0])
            x = float(parse[1])
            y = float(parse[2])
            wid = float(parse[3])
            parse[4].rstrip("\n")
            hei = float(parse[4])
            f1.write("%d %f %f %f %f\n"%(int(idx),x,y,hei,wid))
           
f1.close()


