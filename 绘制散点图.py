#coding=gbk
import matplotlib.pyplot as plt
plt.scatter(2, 4, s=200)
# 设置图表标题并给坐标轴加上标签
plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("aquare of value", fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
