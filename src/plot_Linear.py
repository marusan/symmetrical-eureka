'''
Created on 2018/01/02

@author: maruyama
'''
# https://qiita.com/namitop/items/31326293c92522cf11c1
# 本当はパッケージのパスをきちんと通す必要があるが、面倒くさいのでコメント文で回避
# http://d.hatena.ne.jp/sauerteig/20100728/1280315508

import numpy as np
# @UnresolvedImport
import matplotlib.pyplot as plt

# 描画範囲の指定
# x = np.arange(x軸の最小値, x軸の最大値, 刻み)
x = np.arange(0, 6, 0.1)

# 計算式
y = 2 * x

# 横軸の変数。縦軸の変数。
plt.plot(x, y)

# 描画実行
plt.show()