import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

src_file = sys.argv[1]
src = cv2.imread(src_file,cv2.IMREAD_COLOR)

src = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
cv2.imwrite(src_file,src)
