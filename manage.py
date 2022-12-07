"""Manage File"""
import qiskit

# Python
import os
import sys

# Quantum Language
from interpreter.execution.interpret import interpret

import sys

if __name__ == '__main__':
    file = sys.argv[0]
    ibm = sys.argv[1]
    executedInQuantumComputer = False

    if ibm == 'ibm':
        executedInQuantumComputer = True
    interpret(file)

