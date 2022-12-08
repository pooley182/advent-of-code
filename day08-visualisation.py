from utils import fetch
from matplotlib import use as mpl_use
import matplotlib.pyplot as plt
import numpy as np

mpl_use('MacOSX')

input_data = fetch(8)

input_grid = []

for line in input_data:
    line = line.decode("utf-8").strip()
    tree_row = [int(x) for x in line]
    input_grid.append(tree_row)

data = np.array(input_grid)

ypos, xpos  = np.indices(data.shape)

xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(xpos.shape)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

colors = plt.cm.jet(data.flatten()/float(data.max()))
ax.bar3d(xpos,ypos,zpos, .5,.5,data.flatten(), color=colors)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
