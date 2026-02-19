import numpy as np

def arithmetic_operations():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    return {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b
    }

def aggregate_operations():
    A = np.array([[1, 2, 3],
                  [4, 5, 6]])

    return {
        "sum": np.sum(A),
        "row_sum": np.sum(A, axis=1),
        "col_sum": np.sum(A, axis=0),
        "mean": np.mean(A)
    }


if __name__ == "__main__":
    print(arithmetic_operations())
    print(aggregate_operations())
