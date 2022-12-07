"""Quantum Language Interpreter"""
import qiskit.providers.ibmq
# ANTLR4
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.FileStream import FileStream
from antlr4.tree.Tree import ParseTree
from antlr4.error.ErrorListener import ErrorListener

# Quantum Language
from recognition.generated.QuantumLanguageLexer import QuantumLanguageLexer
from recognition.generated.QuantumLanguageParser import QuantumLanguageParser
from ..visitor.QuantumLanguageTreeVisitor import QuantumLanguageTreeVisitor

from qiskit import IBMQ


def interpret(path, ibm):
    tokens: CommonTokenStream = CommonTokenStream(QuantumLanguageLexer(FileStream(path)))
    # TODO: receive a file content
    parser: QuantumLanguageParser = QuantumLanguageParser(tokens)
    # TODO: Add Syntax Error Listener
    syntax_error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_error_listener)
    tree: ParseTree = parser.start()
    visitor: QuantumLanguageTreeVisitor = QuantumLanguageTreeVisitor()
    visitor.visit(tree)
    # TODO: How to show results
    if ibm == True:
        provider = IBMQ.enable_account(
            '99a7870ee5479c947060f96fd8cfcacc607ea7dec50189f1736f016b0be985c4ffd08c2a265580e54d27f9c6e1d2e53647d1bbc72488efce07e2df18d76ab337')
        backends = provider.backends()
        ibm_backend = qiskit.providers.ibmq.least_busy(backends)
        # Configure backend
        backend = qiskit.Aer.get_backend('aer_simulator')
        quantum_instance = qiskit.QuantumInstance(backend, shots=1024)
# TODO implement in code the execution in quantum computer

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))
