import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri
from scipy.spatial import Delaunay

# u, v are parameterisation variables
# def aera(x,y,z):
def aera():
    u = np.random.randint(0,10,100)
    v = np.random.randint(0,10,100)
    # print(u)
    x = u
    y = v
    z = np.random.randint(0,10,100)

    u = x
    v = y
    # Triangulate parameter space to determine the triangles
    #tri = mtri.Triangulation(u, v)
    tri = Delaunay(np.array([u,v]).T)

    print('polyhedron(faces = [')
    #for vert in tri.triangles:
    for vert in tri.simplices:
        print('[%d,%d,%d],' % (vert[0],vert[1],vert[2]))
    print('], points = [')
    for i in range(x.shape[0]):
        print('[%f,%f,%f],' % (x[i], y[i], z[i]))
    print(']);')


    fig = plt.figure(2)
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    # The triangles in parameter space determine which x, y, z points are
    # connected by an edge
    # ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
    ax.plot_trisurf(x, y, z, triangles=tri.simplices, cmap=plt.cm.Spectral)


    # 设置X轴标签
    plt.xlabel('X')
    # 设置Y轴标签
    plt.ylabel('Y')

    plt.show()
    return None
# aera()