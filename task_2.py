import numpy as np

def matrix_rank(A, tol=1e-10):
    A = A.astype(float)
    rows, cols = A.shape
    rank = 0

    for col in range(cols):
        for row in range(rank, rows):
            if abs(A[row, col]) > tol:
                A[[rank, row]] = A[[row, rank]]
                break
        else:
            continue

        A[rank] = A[rank] / A[rank, col]
        for r in range(rows):
            if r != rank:
                A[r] -= A[rank] * A[r, col]
        rank += 1

    return rank

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 0, 1]
])

print("Ранг матриці:", matrix_rank(A))
