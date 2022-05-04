import math
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
colors = ['green', 'red', 'blue']
plt.figure(figsize=(15, 4.5))

plt.gca().set_prop_cycle(color=colors)
# 1 基础绘图
# 第1步：定义x和y坐标轴上的点   x坐标轴上点的数值
x1 = np.arange(0, 0.05, 0.0001)
# y坐标轴上点的数值
y1 = [math.sin(2 * np.pi * m) for m in x1]
y2 = [math.sin(2 * np.pi * 261.6 * m) for m in x1]
y3 = [math.sin(2 * np.pi * 293.6 * m) for m in x1]
# 第2步：使用plot绘制线条第1个参数是x的坐标值，第2个参数是y的坐标值
plt.plot(x1, y1, label="y=sin(2πx)")
plt.plot(x1, y2, label="y=sin(2π*261.6x)")
plt.plot(x1, y3, label="y=sin(2π*293.6x)")
plt.legend()
plt.title('sin(2πx) 和  do sin(2π*261.6x)  和 re sin(2π*293.6x) 的波形图像')
# 第3步：显示图形
plt.show()
