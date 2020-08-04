import cv2
import matplotlib.pyplot as plt
import numpy as np
import sys

src_file = sys.argv[1]
src_label = sys.argv[2]
src = cv2.imread(src_file,cv2.IMREAD_COLOR)
src = cv2.cvtColor(src,cv2.COLOR_RGB2BGR)
f = open(src_label,'r')

lines = f.readlines()
f1 = open("ratio_"+sys.argv[2],'w')
f2 = open("resized_"+sys.argv[2],'w')
for i in range(len(lines)):
        if lines[i][0] != '9':
            parse = lines[i].split(" ")
            idx = (lines[i][0])
            x = float(parse[1])
            y = float(parse[2])
            wid = float(parse[3])
            parse[4].rstrip("\n")
            hei = float(parse[4])
            print(idx)
                
                
            if src.shape[0] >= src.shape[1]:
                pad_size = src.shape[0]
                x1 = int(x*src.shape[1]) + int((src.shape[0]-src.shape[1])/2)
                y1 = int(y*src.shape[0]) 
                h = int(wid*src.shape[1])
                w = int(hei*src.shape[0])
            else:
                pad_size = src.shape[1]
                x1 = int(x*src.shape[1]) 
                y1 = int(y*src.shape[0]) + int((src.shape[1]-src.shape[0])/2)
                h = int(wid*src.shape[1])
                w = int(hei*src.shape[0])

            
            height = src.shape[0]
            width = src.shape[1]
            if i == 0:
                pad = np.zeros((pad_size,pad_size,3),dtype='uint8')
                pad[int(pad_size/2-height/2):int(pad_size/2+height/2),int(pad_size/2-width/2):int(pad_size/2+width/2)] =np.uint8(src[0:height,0:width])



            x2 = int(x1 + h)
            y2 = int(y1 +w)

            a = x1 - int(h/2)
            b = y1 - int(w/2)

            c = x2 - int(h/2)
            d = y2 - int(w/2)

            #pad = cv2.rectangle(pad,(a,b),(c,d),(255,0,0),3)

            sv_x = ((a + c) /2)/pad.shape[1]
            sv_y = ((b + d) /2)/pad.shape[0]
            hh = ((c-a))/pad.shape[0]
            ww = ((d-b))/pad.shape[1]
            #plt.imshow(pad)
          #  src = cv2.cvtColor(pad,cv2.COLOR_RGB2BGR)
            #cv2.imwrite("resized_"+sys.argc[1],pad)
            
            #cv2.imwrite("resized.jpg",pad)
        

            f1.write("%d %f %f %f %f\n"%(int(idx),sv_x,sv_y,ww,hh))
            f2.write("%d %f %f %f %f\n"%(int(idx),sv_x,sv_y,ww,hh))
            

pad = cv2.cvtColor(pad,cv2.COLOR_BGR2RGB)
cv2.imwrite("ratio_"+sys.argv[1],pad)
pad = cv2.resize(pad,dsize= (608,608),interpolation=cv2.INTER_LINEAR);
cv2.imwrite("resized_"+sys.argv[1],pad)
f.close()
