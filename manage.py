"""Manage File"""

# Python
import sys

# Quantum Language
from interpreter.execution.interpret import interpret

if __name__ == '__main__':
    interpret(sys.argv[1], False)
