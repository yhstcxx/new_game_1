import cv2

img = cv2.imread(r"C:\Users\yhstc\Desktop\untitled3\moni\222.png")
import numpy as np

u,v,_=img.shape
for i in range(u):
    for j in range(v):
        b,g,r=img[i,j]
        # print(b,g,r)
        if ((b in range(200,254)) and (g in range(200,254)) and (r in range(200,254))):#or\
        #         ((b in range(200,215)) and (g in range(206,216)) and (r in range(200,210)))or\
        #     ((b in range(155, 165)) and (g in range(155, 165)) and (r in range(152, 162))):
            # print (1)
            img[i, j] = np.array([255,255,255])
        # print(img[i, j])
        # # else:
            #     print(b,g,r)
cv2.imwrite("3.png",img)