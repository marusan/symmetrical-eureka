'''
Created on 2018/01/03

@author: maruyama
'''
import numpy as np
# @UnresolvedImport
import matplotlib.pyplot as plt

# xとyの値は先ほどと共通
xmin, xmax = -np.pi, np.pi
x = np.arange(xmin, xmax, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# sinのプロット
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title(r"$\sin x$")
plt.xlim(xmin, xmax)
plt.ylim(-1.3, 1.3)

# cosのプロット
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title(r"$\cos x$")
plt.xlim(xmin, xmax)
plt.ylim(-1.3, 1.3)

plt.tight_layout()  # タイトルの被りを防ぐ

plt.show()