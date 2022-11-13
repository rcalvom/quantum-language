"""Quantum Language Tree Visitor"""

# Quantum Language
from recognition.generated.QuantumLanguageParser import QuantumLanguageParser
from recognition.generated.QuantumLanguageParserVisitor import QuantumLanguageParserVisitor


class QuantumLanguageTreeVisitor(QuantumLanguageParserVisitor):


    def __init__(self):

        pass

    """
    Tree Visitor, to implement a Quantum Language Interpreter
    """
    def visitStart(self, ctx: QuantumLanguageParser.StartContext):
        print("Hello Quantum World!")
        return self.visitChildren(ctx)

    # def visitSentence(self, ctx: QuantumLanguageParser.SentenceContext):
    #     return super.visitSentence(ctx)

    def visitIf(self, ctx: QuantumLanguageParser.IfContext):
        if bool(ctx.expresion()):
            for sentence in ctx.sentence():
                self.visitSentence(sentence)

    def visitFor(self, ctx: QuantumLanguageParser.ForContext):

        pass
