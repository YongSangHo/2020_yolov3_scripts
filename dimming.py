import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

file_name = sys.argv[1]
label = file_name[:-4]+".txt"

src_file = file_name
label_data = open(label,'r')
src = cv2.imread(src_file,cv2.IMREAD_COLOR)
src = np.uint8(src*0.4)
cv2.imwrite('dim40_'+ file_name,src)
