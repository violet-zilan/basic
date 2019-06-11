#coding=gbk
import matplotlib.pyplot as plt

x_value=[1, 2, 3, 4, 5]
y_value=[1, 4, 9, 16, 25]
plt.scatter(x_value, y_value, s=200)
# 设置图表标题并给坐标轴加上标签
plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("aquare of value", fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
