import numpy as np

def scalar_broadcast():
    a = np.array([1, 2, 3])
    return a + 10

def vector_broadcast():
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    b = np.array([10, 20, 30])
    return A + b

if __name__ == "__main__":
    print(scalar_broadcast())
    print(vector_broadcast())
