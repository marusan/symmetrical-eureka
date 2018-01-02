'''
Created on 2018/01/03

@author: maruyama
'''
import numpy as np
# @UnresolvedImport
import matplotlib.pyplot as plt

x = np.random.randn(30)
y = np.sin(x) + np.random.randn(30)
# plt.plot(x, y, "o")  # "o"は小さい円(circle marker)
plt.plot(x, y, "ro")  # "r"はredの省略
plt.show()
