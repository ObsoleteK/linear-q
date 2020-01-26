#!/usr/bin/env python3

import numpy as np

hadamard = np.array([[1, 1],
                     [1, -1]])
pauli_x = np.array([[0, 1],
                    [1, 0]])
cnot = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])
qbits = [np.array([[1], [0]]), np.array([[1], [0]]), np.array([[1], [0]])]
qbits[2] = np.matmul(pauli_x, qbits[2])

for index in range(3):
    qbits[index] = np.matmul(hadamard, qbits[index])

if qbits[0][0][0] == 1:
    qbits[2] = np.matmul(pauli_x, qbits[2])

if qbits[1][0][0] == 1:
    qbits[2] = np.matmul(pauli_x, qbits[2])

for index in range(2):
    qbits[index] = np.matmul(hadamard, qbits[index])

print(qbits[0], qbits[1])