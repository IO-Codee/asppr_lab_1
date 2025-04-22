import numpy as np

def jordan_elimination_inverse(A):
    n = len(A)
    A = A.astype(float)
    I = np.eye(n)
    AI = np.hstack((A, I))

    for i in range(n):
        # Діагональний елемент має бути ≠ 0
        if AI[i, i] == 0:
            for j in range(i+1, n):
                if AI[j, i] != 0:
                    AI[[i, j]] = AI[[j, i]]
                    break

        AI[i] = AI[i] / AI[i, i]

        for j in range(n):
            if i != j:
                AI[j] -= AI[i] * AI[j, i]

    return AI[:, n:]

A = np.array([
    [-1, -2, 1],
    [2, -3, 4],
    [-1, 3, 5]
])

A_inv = jordan_elimination_inverse(A)
print("Обернена матриця A⁻¹:")
print(np.round(A_inv, 3))
