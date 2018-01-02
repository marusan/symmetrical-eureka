'''
Created on 2018/01/03

@author: maruyama
'''
import numpy as np
# @UnresolvedImport
import matplotlib.pyplot as plt

x = np.arange(-3, 3, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()
