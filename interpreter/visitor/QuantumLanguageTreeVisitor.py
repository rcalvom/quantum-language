"""Quantum Language Tree Visitor"""

# Quantum Language
from recognition.generated.QuantumLanguageParser import QuantumLanguageParser
from recognition.generated.QuantumLanguageParserVisitor import QuantumLanguageParserVisitor

# NumPy
import numpy as np
# Qiskit
import qiskit


# Qiskit
import qiskit

# regex
import re


def __print__(*args):
    return print(*args)


def __range__(*args):
    return range(*args)


class QuantumLanguageTreeVisitor(QuantumLanguageParserVisitor):
    functions = {}
    variables = {}

    def __init__(self):
        self.createFunctions()
        self.functions = {}
        self.variables = {} #TODO: CONSTANTES (COMPUERTAS)
        circuit = qiskit.QuantumCircuit()

    def createFunctions(self):
        self.functions["print"] = __print__
        self.functions["range"] = __range__

    def visitStart(self, ctx: QuantumLanguageParser.StartContext):
        for statement in ctx.statement():
            self.visitStatement(statement)

    def visitStatement(self, ctx: QuantumLanguageParser.StatementContext):
        for sentence in ctx.sentence():
            self.visitSentence(sentence)

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
        elif ctx.function_declaration() is not None:
            self.visitFunction_declaration(ctx.function_declaration())
        elif ctx.pass_() is not None:
            self.visitPass(ctx.pass_())
        elif ctx.expression() is not None:
            self.visitExpression(ctx.expression())


    def visitAssign(self, ctx: QuantumLanguageParser.AssignContext):
        id = ctx.identifier.text
        self.variables[id] = self.visitExpression(ctx.expression())

    def visitExpression(self, ctx: QuantumLanguageParser.ExpressionContext):
        if ctx.OPEN_PAR_EN():
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
        if type(expression) != bool:
            raise Exception("no boolean expression")
        if expression:
            for statement in ctx.statement():
                self.visitStatement(statement)
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
        if type(expression) != bool:
            raise Exception("no boolean expression")
        if not expression:
            return False
        else:
            for statement in ctx.statement():
                self.visitStatement(statement)
            return True

    def visitElse(self, ctx: QuantumLanguageParser.ElseContext):
        for statement in ctx.statement():
            self.visitStatement(statement)

    def visitFor(self, ctx: QuantumLanguageParser.ForContext):
        iterable = self.visitExpression(ctx.expression())
        if not hasattr(iterable, '__iter__'):
            raise Exception("No iterable")
        for variable in iterable:
            self.variables[ctx.identifier().getText()] = variable
            for statement in ctx.statement():
                self.visitStatement(statement)
                # TODO: break and continue statement

    def visitWhile(self, ctx: QuantumLanguageParser.WhileContext):
        expression = self.visitExpression(ctx.expression())
        if type(expression) != bool:
            raise Exception("no boolean expression")
        while self.visitExpression(ctx.expression()):
            for statement in ctx.statement():
                self.visitStatement(statement)
            # TODO: break and continue statement

    def visitTry(self, ctx: QuantumLanguageParser.TryContext):
        try:
            for statement in ctx.statement():
                self.visitStatement(statement)
        except Exception:
            self.visitExcept(ctx.except_())

    def visitExcept(self, ctx: QuantumLanguageParser.ExceptContext):
        for statement in ctx.statement():
            self.visitStatement(statement)

    def visitFunction_execution(self, ctx: QuantumLanguageParser.Function_executionContext):
        f = self.functions[ctx.identifier().getText()]
        args = []
        for expression in ctx.expression():
            args.append(self.visitExpression(expression))
        return f(*args)

    def visitFunction_declaration(self, ctx: QuantumLanguageParser.Function_declarationContext):
        return super().visitFunction_declaration(ctx)

    def visitAssign(self, ctx: QuantumLanguageParser.AssignContext):
        if ctx.identifier().IDENTIFIER():
            #assert
            self.variables[ctx.identifier().getText()] = self.visitExpression(ctx.expression())
        if ctx.identifier().QUBIT_IDENTIFIER():
            #assert
            self.variables[ctx.identifier().getText()[1: -1]] = self.visitExpression(ctx.expression())
        if ctx.identifier().QUBIT_TRANSPOSE_IDENTIFIER():
            #assert
            self.variables[ctx.identifier().getText()[1: -1]] = self.visitExpression(ctx.expression())


    def visitExpression(self, ctx: QuantumLanguageParser.ExpressionContext):
        if ctx.OPEN_PAREN() and ctx.CLOSE_PAREN():
            return self.visitExpression(ctx.expression())
        if ctx.prefix_unitary_operator():
            if ctx.prefix_unitary_operator().ADD():
                return +self.visitExpression(ctx.expression())
            if ctx.prefix_unitary_operator().MINUS():
                return -self.visitExpression(ctx.expression())
            if ctx.prefix_unitary_operator().MINUS():
                return not self.visitExpression(ctx.expression())
        if ctx.suffix_unitary_operator():
            if ctx.suffix_unitary_operator().HERMITIAN():
                return np.transpose(np.conjugate(self.visitExpression(ctx.expression())))
            if ctx.suffix_unitary_operator().CONJUGATE():
                return np.conjugate(self.visitExpression(ctx.expression()))
            if ctx.suffix_unitary_operator().TRANSPOSE():
                return np.transpose(self.visitExpression(ctx.expression()))
        if ctx.single_qubit_gate():
            if ctx.single_qubit_gate().X():
                return qiskit.QuantumCircuit.x(self.visitExpression(ctx.expression()))
            if ctx.single_qubit_gate().Y():
                return qiskit.QuantumCircuit.y(self.visitExpression(ctx.expression()))
            if ctx.single_qubit_gate().Z():
                return qiskit.QuantumCircuit.z(self.visitExpression(ctx.expression()))
            if ctx.single_qubit_gate().H():
                return qiskit.QuantumCircuit.h(self.visitExpression(ctx.expression()))
            if ctx.single_qubit_gate().S():
                return qiskit.QuantumCircuit.s(self.visitExpression(ctx.expression()))
            if ctx.single_qubit_gate().SDG():
                return qiskit.QuantumCircuit.sdg(self.visitExpression(ctx.expression()))
            if ctx.single_qubit_gate().T():
                return qiskit.QuantumCircuit.t(self.visitExpression(ctx.expression()))
            if ctx.single_qubit_gate().TDG():
                return qiskit.QuantumCircuit.tdg(self.visitExpression(ctx.expression()))
        if ctx.qubit_gate():
            if ctx.qubit_gate().CX():
                return qiskit.QuantumCircuit.cx(self.visitExpression(ctx.expression(0)), self.visitExpression(ctx.expression(1)))
            if ctx.qubit_gate().RX():
                return qiskit.QuantumCircuit.rx(self.visitExpression(ctx.expression(0)), self.visitExpression(ctx.expression(1)))
            if ctx.qubit_gate().RY():
                return qiskit.QuantumCircuit.ry(self.visitExpression(ctx.expression(0)), self.visitExpression(ctx.expression(1)))
            if ctx.qubit_gate().RZ():
                return qiskit.QuantumCircuit.rz(self.visitExpression(ctx.expression(0)), self.visitExpression(ctx.expression(1)))
            if ctx.qubit_gate().P():
                return qiskit.QuantumCircuit.p(self.visitExpression(ctx.expression(0)), self.visitExpression(ctx.expression(1)))

        if ctx.binary_operator():
            left = self.visitExpression(ctx.expression(0))
            right = self.visitExpression(ctx.expression(1))
            if ctx.binary_operator().ADD():
                return left + right
            if ctx.binary_operator().MINUS():
                return left - right
            if ctx.binary_operator().STAR():
                return left * right
            if ctx.binary_operator().DIV():
                return left / right
            if ctx.binary_operator().IDIV():
                return left // right
            if ctx.binary_operator().MOD():
                return left % right
            if ctx.binary_operator().POWER():
                return left ** right
            if ctx.binary_operator().MATMUL():
                return left @ right
            if ctx.binary_operator().KRONECKER():
                return np.kron(left, right)
            if ctx.binary_operator().LESS_THAN():
                return left < right
            if ctx.binary_operator().GREATER_THAN():
                return left > right
            if ctx.binary_operator().EQUALS():
                return left == right
            if ctx.binary_operator().GT_EQ():
                return left >= right
            if ctx.binary_operator().LT_EQ():
                return left <= right
            if ctx.binary_operator().NOT_EQ_1() or ctx.binary_operator().NOT_EQ_2():
                return left != right
        if ctx.identifier():
            return self.variables[ctx.identifier().getText()]
        if ctx.function_execution():
            return self.visitFunction_execution(ctx.function_execution())
        if ctx.INTEGER_LITERAL():
            return int(ctx.INTEGER_LITERAL().getText())
        if ctx.STRING_LITERAL():
            return ctx.STRING_LITERAL().getText()[1: -1]
        if ctx.IMAGINARY_LITERAL():
            return complex(ctx.IMAGINARY_LITERAL().getText())
        #TODO Revisar numeros complejos
        if ctx.FLOAT_LITERAL():
            return float(ctx.FLOAT_LITERAL().getText())
        if ctx.TRUE():
            return True
        if ctx.FALSE():
            return False
        if ctx.QUBIT_STATE_LITERAL().getText():
            return ctx.QUBIT_STATE_LITERAL().getText()
