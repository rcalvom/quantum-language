"""Quantum Language Tree Visitor"""

# Quantum Language
from recognition.generated.QuantumLanguageParser import QuantumLanguageParser
from recognition.generated.QuantumLanguageParserVisitor import QuantumLanguageParserVisitor


class QuantumLanguageTreeVisitor(QuantumLanguageParserVisitor):
    """
    Tree Visitor, to implement a Quantum Language Interpreter
    """
    def visitStart(self, ctx: QuantumLanguageParser.StartContext):
        return self.visitChildren(ctx)
