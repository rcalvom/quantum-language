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


    # Visit a parse tree produced by QuantumLanguageParser#complex_sentence.
    def visitComplex_sentence(self, ctx:QuantumLanguageParser.Complex_sentenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#if.
    def visitIf(self, ctx:QuantumLanguageParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#elif.
    def visitElif(self, ctx:QuantumLanguageParser.ElifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#else.
    def visitElse(self, ctx:QuantumLanguageParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#for.
    def visitFor(self, ctx:QuantumLanguageParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#while.
    def visitWhile(self, ctx:QuantumLanguageParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#try.
    def visitTry(self, ctx:QuantumLanguageParser.TryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#except.
    def visitExcept(self, ctx:QuantumLanguageParser.ExceptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#function_execution.
    def visitFunction_execution(self, ctx:QuantumLanguageParser.Function_executionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#function_declaration.
    def visitFunction_declaration(self, ctx:QuantumLanguageParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#assign.
    def visitAssign(self, ctx:QuantumLanguageParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#identifier.
    def visitIdentifier(self, ctx:QuantumLanguageParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#expression.
    def visitExpression(self, ctx:QuantumLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#binary_operator.
    def visitBinary_operator(self, ctx:QuantumLanguageParser.Binary_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by QuantumLanguageParser#unitary_operator.
    def visitUnitary_operator(self, ctx:QuantumLanguageParser.Unitary_operatorContext):
        return self.visitChildren(ctx)



del QuantumLanguageParser