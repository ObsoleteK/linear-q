#!/usr/bin/env python3

import random
import numpy as np

# Hadamard on 1 bit
hadamard_1 = np.array([[1, 1],
                       [1, -1]])
# Hadamard on 2 bits
hadamard_2 = np.array([[1, 1, 1, 1],
                       [1, -1, 1, -1],
                       [1, 1, -1, -1],
                       [1, -1, -1, 1]])
# Hadamard on 3 bits
hadamard_3 = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
                       [1, 1, 1, 1, -1, -1, -1, -1],
                       [1, 1, -1, -1, -1, -1, 1, 1],
                       [1, 1, -1, -1, 1, 1, -1, -1],
                       [1, -1, -1, 1, 1, -1, -1, 1],
                       [1, -1, -1, 1, -1, 1, 1, -1],
                       [1, -1, 1, -1, -1, 1, -1, 1],
                       [1, -1, 1, -1, 1, -1, 1, -1]])
# Pauli X gate on one bit
pauli_x_1 = np.array([[0, 1],
                      [1, 0]])
# Pauli X gate on a 3 bit system, affecting the first bit
pauli_x_3 = np.array([[0, 0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0, 0]])
# Pauli X gate on a 3 bit system, affecting the third bit
pauli_x_3_1 = np.array([[0, 1, 0, 0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 1, 0]])
# CNOT on a 3 bit system with bit 1 controlling and the third being controlled
cnot_1_3 = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0]])
# CNOT on a 3 bit system with bit 1 controlling and the third being controlled
cnot_2_3 = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0]])

# Initialization state
qbits = np.array([[0],  # 000
                  [0],  # 001
                  [0],  # 010
                  [0],  # 011
                  [0],  # 100
                  [0],  # 101
                  [0],  # 110
                  [0]])  # 111

# for i in range(8):
#     qbits = np.array([[0],   #000
#                       [0],   #001
#                       [0],   #010
#                       [0],   #011
#                       [0],   #100
#                       [0],   #101
#                       [0],   #110
#                       [0]])  #111
#     qbits[i][0] = 1
#     qbits = np.matmul(pauli_x_3, qbits)
#     qbits = np.matmul(hadamard_3, qbits)
#     qbits = np.matmul(cnot_1_3, qbits)
#     qbits = np.matmul(cnot_2_3, qbits)
#     qbits = np.matmul(hadamard_3, qbits)
#     qbits = np.matmul(pauli_x_3, qbits)
#     qbits = qbits/8
#     print(qbits, bin(i))


# deutsch jozsa algorithm assuming constant function
function = random.randint(0, 3)
qbits[function][0] = 1

qbits = np.matmul(pauli_x_3, qbits)
qbits = np.matmul(hadamard_3, qbits)
qbits = np.matmul(cnot_1_3, qbits)
qbits = np.matmul(cnot_2_3, qbits)
qbits = np.matmul(hadamard_3, qbits)
qbits = np.matmul(pauli_x_3, qbits)
qbits = qbits/8

value = [index for index in range(8) if qbits[index][0] == 1][0]
formatted_function = str(bin(function)).strip("0b")
if value in [0, 1, 2, 3]:
    print(f'Function {formatted_function.zfill(2)} is Constant')
elif value in [4, 5, 6, 7]:
    print(f'Function {formatted_function.zfill(2)} is Balanced')
else:
    print(f'Error, Input most likely doesn\'t exist.')
