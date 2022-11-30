"""Quantum Language Tree Visitor"""

# Quantum Language
from recognition.generated.QuantumLanguageParser import QuantumLanguageParser
from recognition.generated.QuantumLanguageParserVisitor import QuantumLanguageParserVisitor


class QuantumLanguageTreeVisitor(QuantumLanguageParserVisitor):

    functions = {}

    def __init__(self):
        self.createFunctionPrint()
        self.variables = {}

    def createFunctionPrint(self):
        self.functions["print"] = print

    def visitStart(self, ctx: QuantumLanguageParser.StartContext):
        for sentence in ctx.sentence():
            self.visit(sentence)
        # if ctx.sentence():
        #     self.visitSentence(ctx.sentence())
        # else:
        #     self.visitComplex_sentence(ctx.complex_sentence())

    def visitSentence(self, ctx: QuantumLanguageParser.SentenceContext):
        if ctx.if_() is not None:
            self.visitIf(ctx.if_())
        elif ctx.for_() is not None:
            self.visitFor(ctx.for_())
        elif ctx.while_() is not None:
            self.visitWhile(ctx.while_())
        elif ctx.try_() is not None:
            self.visitTry(ctx.try_())
        elif ctx.function_execution() is not None:
            self.visitFunction_execution(ctx.function_execution())
        elif ctx.assign() is not None:
            self.visitAssign(ctx.assign())

    def visitComplex_sentence(self, ctx:QuantumLanguageParser.Complex_sentenceContext):
        return self.visitChildren(ctx)
    
    def visitAssign(self, ctx: QuantumLanguageParser.AssignContext):
        id = ctx.identifier.text
        self.variables[id] = self.visitExpression(ctx.expression())

    def visitExpression(self, ctx: QuantumLanguageParser.ExpressionContext):
        if ctx.OPEN_PAREN():
            return self.visitExpression(ctx.expression())
        if ctx.binary_operator():
            left = self.visitExpression(ctx.expression(0))
            right = self.visitExpression(ctx.expression(1))
            bin_operator = ctx.binary_operator().getText()
            if bin_operator == '+':
                return left + right
            if bin_operator == '-':
                return left - right
            if bin_operator == '*':
                return left * right
            if bin_operator == '/':
                return left / right
            if bin_operator == '//':
                return left // right
            if bin_operator == '%':
                return left % right
            if bin_operator == '**':
                return left ** right
            if bin_operator == '<':
                return left < right
            if bin_operator == '>':
                return left > right
            if bin_operator == '==':
                return left == right
            if bin_operator == '>=':
                return left >= right
            if bin_operator == '<=':
                return left <= right
            if bin_operator == '<>' or bin_operator == '!=':
                return left != right
        if ctx.unitary_operator():
            u_operator = ctx.unitary_operator().getText()
            operand = self.visitExpression(ctx.expression())
            if u_operator == '+':
                return +operand
            if u_operator == '-':
                return -operand
            if u_operator == 'not':
                return not u_operator
        if ctx.identifier():
            return self.variables[ctx.identifier().getText()]
        if ctx.function_execution():
            return self.visitFunction_execution(ctx.function_execution())
        if ctx.INTEGER_LITERAL():
            return int(ctx.INTEGER_LITERAL().getText())
        if ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()
        if ctx.IMAGINARY_LITERAL():
            return complex(ctx.IMAGINARY_LITERAL().getText())
        if ctx.FLOAT_LITERAL():
            return float(ctx.FLOAT_LITERAL().getText())
        if ctx.TRUE():
            return True
        if ctx.FALSE():
            return False
        return ctx.QUBIT_STATE_LITERAL().getText()
        return None

    def visitIf(self, ctx: QuantumLanguageParser.IfContext):
        expression = self.visitExpression(ctx.expression())
        if expression is not bool:
            raise Exception("no boolean expression")
        if expression:
            for sentence in ctx.sentence():
                self.visitSentence(sentence)
        else_statement = False
        if not expression and ctx.elif_() is not None:
            for elif_ in ctx.elif_():
                if self.visitElif(elif_):
                    else_statement = True
                    break
        if not expression and ctx.else_() is not None and not else_statement:
            self.visitElse(ctx.else_())

    def visitElif(self, ctx: QuantumLanguageParser.ElifContext):
        expression = self.visitExpression(ctx.expression())
        if expression is not bool:
            raise Exception("no boolean expression")
        if not expression:
            return False
        else:
            for sentence in ctx.sentence():
                self.visitSentence(sentence)
            return True

    def visitElse(self, ctx: QuantumLanguageParser.ElseContext):
        for sentence in ctx.sentence():
            self.visitSentence(sentence)

    def visitFor(self, ctx: QuantumLanguageParser.ForContext):
        iterable = self.visitExpression(ctx.expression())
        if not hasattr(iterable, '__iter__'):
            raise Exception("No iterable")
        for variable in iterable:
            # TODO: add variable to runtime vars
            # variableName = ctx.identifier().getText()
            for sentence in ctx.sentence():
                self.visitSentence(sentence)
                # TODO: break and continue statement
        # TODO: remove variable from runtime vars

    def visitWhile(self, ctx: QuantumLanguageParser.WhileContext):
        expression = self.visitExpression(ctx.expression())
        if expression is not bool:
            raise Exception("no boolean expression")
        while self.visitExpression(ctx.expression()):
            for sentence in ctx.sentence():
                # TODO: break and continue statement
                self.visitSentence(sentence)

    def visitTry(self, ctx: QuantumLanguageParser.TryContext):
        try:
            for sentence in ctx.sentence():
                self.visitSentence(sentence)
        except Exception:
            self.visitExcept(ctx.except_())

    def visitExcept(self, ctx: QuantumLanguageParser.ExceptContext):
        for sentence in ctx.sentence():
            self.visitSentence(sentence)

    def visitFunction_execution(self, ctx: QuantumLanguageParser.Function_executionContext):
        return super().visitFunction_execution(ctx)

    def visitFunction_declaration(self, ctx:QuantumLanguageParser.Function_declarationContext):
        return super().visitFunction_execution(ctx)
