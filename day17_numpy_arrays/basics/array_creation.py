import numpy as np

def create_basic_arrays():
    a = np.array([1, 2, 3, 4])
    b = np.array([[1, 2, 3],
                  [4, 5, 6]])

    zeros = np.zeros((2, 3))
    ones = np.ones((3, 3))
    arange_arr = np.arange(0, 10, 2)
    linspace_arr = np.linspace(0, 1, 5)

    return a, b, zeros, ones, arange_arr, linspace_arr

if __name__ == "__main__":
    arrays = create_basic_arrays()
    for arr in arrays:
        print(arr)
        print()
