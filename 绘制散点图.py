#coding=gbk
import matplotlib.pyplot as plt
plt.scatter(2, 4, s=200)
# ����ͼ����Ⲣ����������ϱ�ǩ
plt.title("square numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("aquare of value", fontsize=14)
#���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
