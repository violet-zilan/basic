# coding=gbk
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("square of value", fontsize=14)
#���ÿ̶ȱ�ǵĴ�С
plt.tick_params(axis='both',, labelsize=14)
plt.show()
