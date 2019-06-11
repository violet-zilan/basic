import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
	rw = RandomWalk(50000)

	rw.fill_walk()
	
	plt.figure(figsize=(100,50))
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values,c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=5)
	plt.scatter(0, 0, c='green', edgecolor='none', s=30)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=30)
	plt.show()
	keep_running = input("Make anothe walk? (y/n): ")
	if keep_running == 'n':
		break		
		
