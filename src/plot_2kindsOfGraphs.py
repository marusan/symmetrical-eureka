'''
Created on 2018/01/03

@author: maruyama
'''
import numpy as np
# @UnresolvedImport
import matplotlib.pyplot as plt

n = 300
x = np.random.randn(n)
y = np.sin(x) + np.random.randn(n) * 0.3

fig = plt.figure()

# サブプロットを8:2で分割
ax1 = fig.add_axes((0, 0.2, 1, 0.8))
ax2 = fig.add_axes((0, 0, 1, 0.2), sharex=ax1)

# 散布図のx軸のラベルとヒストグラムのy軸のラベルを非表示
ax1.tick_params(labelbottom="off")
ax2.tick_params(labelleft="off")

ax1.plot(x, y, "x")
ax2.hist(x, bins=20)

plt.show()