def vol(points,y_deta,z_deta,points_numb):
    volum = 0
    final_z=0
    for i in points:
        if i[3]==1:
            volum+=1
            #x,y,z,y才是火焰高度
            if i[1]>final_z:
                final_z = i[1]
                print(final_z)
        # index += 1
    # print("体积是+", volum*w_deta*h_deta*h_deta)
    return volum * (points[1,0]-points[0,0]) * (points[-1,1]-points[0,1])/(y_deta-1) * (points[-1,2]-points[0,2])/(z_deta-1),final_z  #,W
if __name__ == '__main__':
    import numpy as np
    signal_begin = ['6', '8', '11', '1600', '800', '50', '210', '50', '-10', '10', '-4', '30', '-10', '10']
    signal_begin_int = list(map(eval, signal_begin))
    drc,w,h,lenth,wedth,x_deta,y_deta,z_deta,x0,x1,y0,y1,z0,z1 = signal_begin_int

    points_numb = \
    np.mgrid[x0:x1:eval(str(x_deta) + "j"), y0:y1:eval(str(y_deta) + "j"), z0:z1:eval(str(z_deta) + "j")].T.reshape(-1,
                                                                                                                    3).shape[
        0]
    path =r"C:\Users\yhstc\Desktop\ceshi\222\kw"
    poinst_3d = np.load(path+"\\" +'point'+"\\" +"point_3d_1.npy")
    volum, final_z=vol(poinst_3d, y_deta, z_deta, points_numb)
    print(volum,final_z)