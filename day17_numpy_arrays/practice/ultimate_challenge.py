import numpy as np

def triangle_matrix(n=5):
    A = np.zeros((n, n))
    A[np.triu_indices(n, 1)] = 1
    A[np.tril_indices(n, -1)] = -1
    return A

if __name__ == "__main__":
    print(triangle_matrix())
