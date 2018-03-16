#!/usr/bin/env python3
import numpy as np
import random
import cProfile

def perceptron3(x_list, y_list, limit):
	wp = np.zeros(4)
	print(wp)
	wp_err_count = sum([np.sign(wp.dot(x_list[i])) != y_list[i] for i in range(len(x_list))])
	print(wp_err_count)
	for i in range(limit):
		j = random.randrange(len(x_list))
		x = x_list[j]
		y = y_list[j]
