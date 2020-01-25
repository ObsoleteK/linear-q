import numpy as np
import math
import secrets

secretnumber = secrets.randbelow(4)
functions = [[0,1],[1,0],[1,1],[0,0]]
function = functions[secretnumber]
print(function)

qbit = [0,1]


def deutschJozsaOracle(qubit, secretfunction):
    q0sign = str((-1)**function[0]).replace('1', '').replace('0', '')
    q1 = qubit[0][3]*((-1)**function[1])
    if q1 < 0 and qubit[0][2] == '-':
        sign = '+'
        q1 = abs(q1)
    elif q1 < 0 and qubit[0][1] == '+':
        sign = '-'
        q1 = abs(q1)
    else: sign = qubit[0][2]

    return[[q0sign, qubit[0][1], sign, q1], qubit[1]]

def hadamard(qubit):
    if qubit == 1:
        return([['', 0,'-',1],[(1/math.sqrt(2))]])
    elif qubit == 0:
        return([['', 0,'+',1],[(1/math.sqrt(2))]])

qbit[0] = hadamard(qbit[0])
qbit[1] = hadamard(qbit[1])

qbit[0] = deutschJozsaOracle(qbit[0], function)

calc = (f'({qbit[0][0][0]}({qbit[0][0][1]}{qbit[0][0][2]}{qbit[0][0][3]}))*{qbit[0][1][0]}')
calc_eval = eval(calc)

print(calc_eval)
if calc_eval >= 0:
    print(f'Secret Function {function} is constant.')
else: print(f'Secret Function {function} is balanced.')