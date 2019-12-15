import numpy as np
from plyfile import PlyData, PlyElement
a = PlyData.read("bun_zipper.ply")
print(len(a.elements[0].data))
max = 0
for i in a['face'].data['vertex_indices']:
    if np.max(i)>max:
        max = np.max(i)
print(a['face'].data['vertex_indices'][0]
      )
print(max)
