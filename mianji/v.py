def vol(points,y_deta,z_deta,points_numb):
    volum = 0
    final_z=0
    for i in points:
        if i[3]==1:
            volum+=1
            final_z = i[2]
        # index += 1
    # print("体积是+", volum*w_deta*h_deta*h_deta)
    return volum * (points[1,0]-points[0,0]) * (points[-1,1]-points[0,1])/(y_deta-1) * (points[-1,2]-points[0,2])/(z_deta-1),final_z  #,W