def vol(points, x_deta, y_deta, z_deta, points_numb):
    volum = 0

    for i in points:
        if i[3]==1:
            volum+=1
        # index += 1
    # print("体积是+", volum*w_deta*h_deta*h_deta)
    return volum * x_deta * y_deta* z_deta  #,W