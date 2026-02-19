import numpy as np


def matrix_pattern():
    return np.arange(1, 13).reshape(3, 4)


def row_normalization(A):
    row_min = A.min(axis=1, keepdims=True)
    row_max = A.max(axis=1, keepdims=True)
    return (A - row_min) / (row_max - row_min)


def conditional_replacement():
    A = np.arange(1, 21)
    A[A % 2 == 0] = -1
    A[A > 15] = 100
    return A


def distance_metrics(x, y):
    euclidean = np.sqrt(np.sum((x - y) ** 2))
    manhattan = np.sum(np.abs(x - y))
    dot = np.dot(x, y)
    return euclidean, manhattan, dot


if __name__ == "__main__":
    print(matrix_pattern())
    A = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(row_normalization(A))
    print(conditional_replacement())
    print(distance_metrics(np.array([1,2,3]), np.array([4,5,6])))
