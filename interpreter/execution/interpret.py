"""Quantum Language Interpreter"""
# ANTLR4
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.FileStream import FileStream
from antlr4.tree.Tree import ParseTree
from antlr4.error.ErrorListener import ErrorListener

# Quantum Language
from recognition.generated.QuantumLanguageLexer import QuantumLanguageLexer
from recognition.generated.QuantumLanguageParser import QuantumLanguageParser
from ..visitor.QuantumLanguageTreeVisitor import QuantumLanguageTreeVisitor


def interpret(path):
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
# TODO implement in code the execution in quantum computer


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))
