#coding=gbk
import matplotlib.pyplot as plt

x_value=[1, 2, 3, 4, 5]
y_value=[1, 4, 9, 16, 25]
plt.scatter(x_value, y_value, s=200)
# ����ͼ����Ⲣ����������ϱ�ǩ
plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("aquare of value", fontsize=14)
#���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
