#!/usr/bin/python3

"""module to return a pascal's triangle"""


def pascal_triangle(n):
	"""
	Pascal's trianglr
	Arges:
		n (int): The Number of rows of the triangle
	Returns:
		List of integers reprepresenting the Pascal's triangle
	"""
	lists = []
	if n == 0:
		return lists
	for i in range(n):
		lists.append([])
		lists[i].append(1)
		if (i > 0):
			for j in range(1, i):
				lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j])
			lists[i].append(1)
	return lists
