#coding=gbk
import matplotlib.pyplot as plt
x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=4)
# ����ͼ����Ⲣ����������ϱ�ǩ
plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("aquare of value", fontsize=14)
#���ÿ̶ȱ�ǵĴ�С
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')
