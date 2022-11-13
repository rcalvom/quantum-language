# Generated from QuantumLanguageParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .QuantumLanguageParser import QuantumLanguageParser
else:
    from QuantumLanguageParser import QuantumLanguageParser

# This class defines a complete generic visitor for a parse tree produced by QuantumLanguageParser.

class QuantumLanguageParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by QuantumLanguageParser#start.
    def visitStart(self, ctx:QuantumLanguageParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#sentence.
    def visitSentence(self, ctx:QuantumLanguageParser.SentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#if.
    def visitIf(self, ctx:QuantumLanguageParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#assign.
    def visitAssign(self, ctx:QuantumLanguageParser.AssignContext):
        return self.visitChildren(ctx)



del QuantumLanguageParser