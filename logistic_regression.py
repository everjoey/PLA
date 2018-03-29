#!/usr/bin/env python3
import numpy as np
from scipy.special import expit
from sklearn import linear_model

def logistic_regression(x, y):
	N, d = x.shape
	w = np.zeros(d)

	for i in range(100000):
#		grad = np.array([sum([expit(-y[i]*w.dot(x[i]))*(-y[i]*x[i][j]) for i in range(N)])/N for j in range(d)])
		grad = np.dot(-y*expit(-y*np.dot(w, x.T)), x)/N
		norm = np.linalg.norm(grad)
		print(norm)
                if norm < 0.0001:
			break
		else:
			w = w - 0.1*grad
	print(i)

	return w
