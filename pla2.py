#!/usr/bin/env python3
import numpy as np
import random
import cProfile

def perceptron2(x_list, y_list):
	w = np.zeros(4)
	print(w)
	while True:
		err_count = 0
		for i in range(len(x_list)):
			if np.sign(w.dot(x_list[i])) != y_list[i] and y_list[i] != 0:
		
