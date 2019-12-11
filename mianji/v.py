import numpy as np
def vol(points,w_deta,h_deta,points_numb):
    volum = 0

    for i in points:
        if i[3]==1:
            volum+=1
        # index += 1
    # print("体积是+", volum*w_deta*h_deta*h_deta)
    return volum*w_deta*w_deta*h_deta  #,W