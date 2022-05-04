import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 1 基础绘图
# 第1步：定义x和y坐标轴上的点   x坐标轴上点的数值
x = np.arange(0, 2 * np.pi, 0.01)
# y坐标轴上点的数值
y = [math.sin(m) for m in x]
# 第2步：使用plot绘制线条第1个参数是x的坐标值，第2个参数是y的坐标值
plt.plot(x, y)
# 第3步：显示图形
plt.show()

plt.show()
