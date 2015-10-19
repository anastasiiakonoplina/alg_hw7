numbers = [2, 1, 2, 1, 1, 3, 6, 10, 1, 2, 2, 1, 6, 1, 2, 2, 1, 7, 2, 1, 8, 2, 1, 1, 4, 7, 8, 10, 7, 3, 1, 4, 4, 5, 2, 1, 2, 2, 2, 1, 1, 1, 2, 3]

def maxValue(numbers):
	matrix = {} 
	n = len(numbers)
	for i in range(n):
		matrix[i, i] = numbers[i]
		for j in range(n):
			if i > j:
				matrix[i, j] = 0
	print matrix

	for i in range(n - 2, 0, -1):
		for j in range(i + 1, n - 1):
			for k in range(i, j - 1):
				matrix[i, j] = max(matrix[i, j], max(matrix[i, k] + matrix[k + 1, j], matrix[i, k] * matrix[k + 1, j]))
	return matrix


print maxValue(numbers)

