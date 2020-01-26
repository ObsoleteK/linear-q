#!/usr/bin/env python3

import numpy as np

hadamard_1 = np.array([[1, 1],
                       [1,-1]])
hadamard_2 = np.array([[1, 1, 1, 1],
                       [1,-1, 1,-1],
                       [1, 1,-1,-1],
                       [1,-1,-1, 1]])
hadamard_3 = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1,-1,-1,-1,-1],
                       [1, 1,-1,-1,-1,-1, 1, 1],
                       [1, 1,-1,-1, 1, 1,-1,-1],
                       [1,-1,-1, 1, 1,-1,-1, 1],
                       [1,-1,-1, 1,-1, 1, 1,-1],
                       [1,-1, 1,-1,-1, 1,-1, 1],
                       [1,-1, 1,-1, 1,-1, 1,-1]])
pauli_x_1 = np.array([[0, 1],
                      [1, 0]])
pauli_x_3 = np.array([[0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0]])
cnot_1_3 = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0]])
cnot_2_3 = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0]])
qbits = np.array([[1],
                  [0],
                  [0],
                  [0],
                  [0],
                  [0],
                  [0],
                  [0]])

#deutsch jozsa algorithm assuming constant function
qbits = np.matmul(pauli_x_3, qbits)
qbits = np.matmul(hadamard_3, qbits)
qbits = np.matmul(cnot_1_3, qbits)
qbits = np.matmul(cnot_2_3, qbits)
qbits = np.array([qbits[4],
                  qbits[7]])
qbits = np.matmul(hadamard_1, qbits)
qbits = np.matmul(pauli_x_1, qbits)
print(qbits)