import numpy as np

def solve_by_inverse(A, B):
    A_inv = np.linalg.inv(A)
    X = np.dot(A_inv, B)
    return X

A = np.array([
    [-1, -2, 1],
    [2, -3, 4],
    [-1, 3, 5]
])

B = np.array([4, 5, 3])
X = solve_by_inverse(A, B)

print("Розв\'язки системи (X):")
print(np.round(X, 3))
