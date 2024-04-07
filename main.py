""""
created on Feb 03 2024 20:15 2023
@author: caiorabello for_code 

"""

from mpl_toolkits import mplot3d
import numpy as np 
import matplotlib.pyplot as plt 

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

ax = plt.axes(projection='3d')

def funcao_z(x,y):
    return np.sin(np.sqrt(x**2+y**2))
x = np.linspace(-6,6,30)
y = np.linspace(-6,6,30)

x, y = np.meshgrid(x, y)
z = funcao_z(x,y)

## Criando uma matriz de cores  
cores_verdes = (0.5,0,0.5,1) 

 
ax.plot_wireframe(x,y,z, color='green')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel ('z')

ax.plot_surface(x, y, z, cmap= 'viridis', edgecolor='none')

ax.set_title( 'grafico de superficies')

plt.show()
