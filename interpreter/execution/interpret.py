"""Quantum Language Interpreter"""

# ANTLR4
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.tree.Tree import ParseTree

# Quantum Language
from recognition.generated.QuantumLanguageLexer import QuantumLanguageLexer
from recognition.generated.QuantumLanguageParser import QuantumLanguageParser
from interpreter.visitor.QuantumLanguageTreeVisitor import QuantumLanguageTreeVisitor


def interpret():
    tokens: CommonTokenStream = CommonTokenStream(QuantumLanguageLexer(InputStream("a = 0")))
    # TODO: receive a file content
    parser: QuantumLanguageParser = QuantumLanguageParser(tokens)
    # TODO: Add Syntax Error Listener
    tree: ParseTree = parser.start()
    visitor: QuantumLanguageTreeVisitor = QuantumLanguageTreeVisitor()
    visitor.visit(tree)
    # TODO: How to show results
