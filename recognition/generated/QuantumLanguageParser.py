# Generated from QuantumLanguageParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,66,248,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,4,0,40,8,0,
        11,0,12,0,41,1,0,1,0,1,1,1,1,1,1,5,1,49,8,1,10,1,12,1,52,9,1,1,1,
        3,1,55,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,68,8,
        2,1,3,1,3,1,3,1,3,1,3,1,3,4,3,76,8,3,11,3,12,3,77,1,3,1,3,5,3,82,
        8,3,10,3,12,3,85,9,3,1,3,3,3,88,8,3,1,4,1,4,1,4,1,4,1,4,1,4,4,4,
        96,8,4,11,4,12,4,97,1,4,1,4,1,5,1,5,1,5,1,5,1,5,4,5,107,8,5,11,5,
        12,5,108,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,120,8,6,11,6,12,
        6,121,1,6,1,6,1,7,1,7,1,7,1,7,1,7,4,7,131,8,7,11,7,12,7,132,1,7,
        1,7,1,8,1,8,1,8,1,8,4,8,141,8,8,11,8,12,8,142,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,9,1,9,3,9,154,8,9,1,9,1,9,5,9,158,8,9,10,9,12,9,161,
        9,9,1,9,1,9,3,9,165,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,5,10,174,
        8,10,10,10,12,10,177,9,10,3,10,179,8,10,1,10,1,10,1,11,1,11,1,11,
        1,11,1,11,1,11,5,11,189,8,11,10,11,12,11,192,9,11,3,11,194,8,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,206,8,12,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,3,14,227,8,14,1,14,1,14,1,14,1,14,
        1,14,1,14,5,14,235,8,14,10,14,12,14,238,9,14,1,15,1,15,1,16,1,16,
        1,17,1,17,1,18,1,18,1,18,0,1,28,19,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,0,4,1,0,58,60,2,0,5,18,53,54,2,0,5,6,35,35,
        1,0,55,57,267,0,39,1,0,0,0,2,45,1,0,0,0,4,67,1,0,0,0,6,69,1,0,0,
        0,8,89,1,0,0,0,10,101,1,0,0,0,12,112,1,0,0,0,14,125,1,0,0,0,16,136,
        1,0,0,0,18,147,1,0,0,0,20,168,1,0,0,0,22,182,1,0,0,0,24,201,1,0,
        0,0,26,207,1,0,0,0,28,226,1,0,0,0,30,239,1,0,0,0,32,241,1,0,0,0,
        34,243,1,0,0,0,36,245,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,41,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,43,1,0,0,0,43,44,5,0,0,1,
        44,1,1,0,0,0,45,50,3,4,2,0,46,47,5,51,0,0,47,49,3,4,2,0,48,46,1,
        0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,54,1,0,0,0,52,
        50,1,0,0,0,53,55,5,51,0,0,54,53,1,0,0,0,54,55,1,0,0,0,55,56,1,0,
        0,0,56,57,5,52,0,0,57,3,1,0,0,0,58,68,3,6,3,0,59,68,3,12,6,0,60,
        68,3,14,7,0,61,68,3,16,8,0,62,68,3,20,10,0,63,68,3,24,12,0,64,68,
        3,22,11,0,65,68,3,36,18,0,66,68,3,28,14,0,67,58,1,0,0,0,67,59,1,
        0,0,0,67,60,1,0,0,0,67,61,1,0,0,0,67,62,1,0,0,0,67,63,1,0,0,0,67,
        64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,5,1,0,0,0,69,70,5,24,0,
        0,70,71,3,28,14,0,71,72,5,50,0,0,72,73,5,52,0,0,73,75,5,1,0,0,74,
        76,3,2,1,0,75,74,1,0,0,0,76,77,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,
        0,78,79,1,0,0,0,79,83,5,2,0,0,80,82,3,8,4,0,81,80,1,0,0,0,82,85,
        1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,
        86,88,3,10,5,0,87,86,1,0,0,0,87,88,1,0,0,0,88,7,1,0,0,0,89,90,5,
        25,0,0,90,91,3,28,14,0,91,92,5,50,0,0,92,93,5,52,0,0,93,95,5,1,0,
        0,94,96,3,2,1,0,95,94,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,
        1,0,0,0,98,99,1,0,0,0,99,100,5,2,0,0,100,9,1,0,0,0,101,102,5,26,
        0,0,102,103,5,50,0,0,103,104,5,52,0,0,104,106,5,1,0,0,105,107,3,
        2,1,0,106,105,1,0,0,0,107,108,1,0,0,0,108,106,1,0,0,0,108,109,1,
        0,0,0,109,110,1,0,0,0,110,111,5,2,0,0,111,11,1,0,0,0,112,113,5,28,
        0,0,113,114,3,26,13,0,114,115,5,29,0,0,115,116,3,28,14,0,116,117,
        5,50,0,0,117,119,5,1,0,0,118,120,3,4,2,0,119,118,1,0,0,0,120,121,
        1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,124,
        5,2,0,0,124,13,1,0,0,0,125,126,5,27,0,0,126,127,3,28,14,0,127,128,
        5,50,0,0,128,130,5,1,0,0,129,131,3,4,2,0,130,129,1,0,0,0,131,132,
        1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,134,1,0,0,0,134,135,
        5,2,0,0,135,15,1,0,0,0,136,137,5,30,0,0,137,138,5,50,0,0,138,140,
        5,1,0,0,139,141,3,4,2,0,140,139,1,0,0,0,141,142,1,0,0,0,142,140,
        1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,5,2,0,0,145,146,
        3,18,9,0,146,17,1,0,0,0,147,148,5,32,0,0,148,149,3,28,14,0,149,150,
        5,50,0,0,150,159,5,1,0,0,151,153,3,4,2,0,152,154,5,51,0,0,153,152,
        1,0,0,0,153,154,1,0,0,0,154,155,1,0,0,0,155,156,5,52,0,0,156,158,
        1,0,0,0,157,151,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,
        1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,164,3,4,2,0,163,165,
        5,51,0,0,164,163,1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,167,
        5,2,0,0,167,19,1,0,0,0,168,169,3,26,13,0,169,178,5,44,0,0,170,175,
        3,28,14,0,171,172,5,49,0,0,172,174,3,28,14,0,173,171,1,0,0,0,174,
        177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,179,1,0,0,0,177,
        175,1,0,0,0,178,170,1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,
        181,5,45,0,0,181,21,1,0,0,0,182,183,5,20,0,0,183,184,3,26,13,0,184,
        193,5,44,0,0,185,190,3,26,13,0,186,187,5,49,0,0,187,189,3,26,13,
        0,188,186,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,
        0,191,194,1,0,0,0,192,190,1,0,0,0,193,185,1,0,0,0,193,194,1,0,0,
        0,194,195,1,0,0,0,195,196,5,45,0,0,196,197,5,50,0,0,197,198,5,1,
        0,0,198,199,3,4,2,0,199,200,5,2,0,0,200,23,1,0,0,0,201,202,3,26,
        13,0,202,203,5,19,0,0,203,205,3,28,14,0,204,206,5,51,0,0,205,204,
        1,0,0,0,205,206,1,0,0,0,206,25,1,0,0,0,207,208,7,0,0,0,208,27,1,
        0,0,0,209,210,6,14,-1,0,210,211,5,44,0,0,211,212,3,28,14,0,212,213,
        5,45,0,0,213,227,1,0,0,0,214,215,3,32,16,0,215,216,3,28,14,12,216,
        227,1,0,0,0,217,227,3,26,13,0,218,227,3,20,10,0,219,227,5,62,0,0,
        220,227,5,61,0,0,221,227,5,63,0,0,222,227,5,64,0,0,223,227,5,38,
        0,0,224,227,5,39,0,0,225,227,5,65,0,0,226,209,1,0,0,0,226,214,1,
        0,0,0,226,217,1,0,0,0,226,218,1,0,0,0,226,219,1,0,0,0,226,220,1,
        0,0,0,226,221,1,0,0,0,226,222,1,0,0,0,226,223,1,0,0,0,226,224,1,
        0,0,0,226,225,1,0,0,0,227,236,1,0,0,0,228,229,10,10,0,0,229,230,
        3,30,15,0,230,231,3,28,14,11,231,235,1,0,0,0,232,233,10,11,0,0,233,
        235,3,34,17,0,234,228,1,0,0,0,234,232,1,0,0,0,235,238,1,0,0,0,236,
        234,1,0,0,0,236,237,1,0,0,0,237,29,1,0,0,0,238,236,1,0,0,0,239,240,
        7,1,0,0,240,31,1,0,0,0,241,242,7,2,0,0,242,33,1,0,0,0,243,244,7,
        3,0,0,244,35,1,0,0,0,245,246,5,41,0,0,246,37,1,0,0,0,23,41,50,54,
        67,77,83,87,97,108,121,132,142,153,159,164,175,178,190,193,205,226,
        234,236
    ]

class QuantumLanguageParser ( Parser ):

    grammarFileName = "QuantumLanguageParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'//'", "'%'", 
                     "'**'", "'<'", "'>'", "'=='", "'>='", "'<='", "'<>'", 
                     "'!='", "'='", "'def'", "'return'", "'raise'", "'assert'", 
                     "'if'", "'elif'", "'else'", "'while'", "'for'", "'in'", 
                     "'try'", "'finally'", "'except'", "'or'", "'and'", 
                     "'not'", "'is'", "'None'", "'True'", "'False'", "'class'", 
                     "'pass'", "'continue'", "'break'", "'('", "')'", "'['", 
                     "']'", "'.'", "','", "':'", "';'", "<INVALID>", "'@'", 
                     "'(X)'", "'T'", "'''", "'t'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "SPACES", "COMMENTS", 
                      "ADD", "MINUS", "STAR", "DIV", "IDIV", "MOD", "POWER", 
                      "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", 
                      "NOT_EQ_1", "NOT_EQ_2", "ASSIGN", "DEF", "RETURN", 
                      "RAISE", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", 
                      "FOR", "IN", "TRY", "FINALLY", "EXCEPT", "OR", "AND", 
                      "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", "PASS", 
                      "CONTINUE", "BREAK", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACK", "CLOSE_BRACK", "DOT", "COMMA", "COLON", 
                      "SEMI_COLON", "NEWLINE", "MATMUL", "KRONECKER", "HERMITIAN", 
                      "CONJUGATE", "TRANSPOSE", "IDENTIFIER", "QUBIT_IDENTIFIER", 
                      "QUBIT_TRANSPOSE_IDENTIFIER", "STRING_LITERAL", "INTEGER_LITERAL", 
                      "IMAGINARY_LITERAL", "FLOAT_LITERAL", "QUBIT_STATE_LITERAL", 
                      "QUBIT_TRANSPOSE_STATE_LITERAL" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_sentence = 2
    RULE_if = 3
    RULE_elif = 4
    RULE_else = 5
    RULE_for = 6
    RULE_while = 7
    RULE_try = 8
    RULE_except = 9
    RULE_function_execution = 10
    RULE_function_declaration = 11
    RULE_assign = 12
    RULE_identifier = 13
    RULE_expression = 14
    RULE_binary_operator = 15
    RULE_prefix_unitary_operator = 16
    RULE_suffix_unitary_operator = 17
    RULE_pass = 18

    ruleNames =  [ "start", "statement", "sentence", "if", "elif", "else", 
                   "for", "while", "try", "except", "function_execution", 
                   "function_declaration", "assign", "identifier", "expression", 
                   "binary_operator", "prefix_unitary_operator", "suffix_unitary_operator", 
                   "pass" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    SPACES=3
    COMMENTS=4
    ADD=5
    MINUS=6
    STAR=7
    DIV=8
    IDIV=9
    MOD=10
    POWER=11
    LESS_THAN=12
    GREATER_THAN=13
    EQUALS=14
    GT_EQ=15
    LT_EQ=16
    NOT_EQ_1=17
    NOT_EQ_2=18
    ASSIGN=19
    DEF=20
    RETURN=21
    RAISE=22
    ASSERT=23
    IF=24
    ELIF=25
    ELSE=26
    WHILE=27
    FOR=28
    IN=29
    TRY=30
    FINALLY=31
    EXCEPT=32
    OR=33
    AND=34
    NOT=35
    IS=36
    NONE=37
    TRUE=38
    FALSE=39
    CLASS=40
    PASS=41
    CONTINUE=42
    BREAK=43
    OPEN_PAREN=44
    CLOSE_PAREN=45
    OPEN_BRACK=46
    CLOSE_BRACK=47
    DOT=48
    COMMA=49
    COLON=50
    SEMI_COLON=51
    NEWLINE=52
    MATMUL=53
    KRONECKER=54
    HERMITIAN=55
    CONJUGATE=56
    TRANSPOSE=57
    IDENTIFIER=58
    QUBIT_IDENTIFIER=59
    QUBIT_TRANSPOSE_IDENTIFIER=60
    STRING_LITERAL=61
    INTEGER_LITERAL=62
    IMAGINARY_LITERAL=63
    FLOAT_LITERAL=64
    QUBIT_STATE_LITERAL=65
    QUBIT_TRANSPOSE_STATE_LITERAL=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(QuantumLanguageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = QuantumLanguageParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.statement()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 2296836455324483587) != 0):
                    break

            self.state = 43
            self.match(QuantumLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.SentenceContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,i)


        def NEWLINE(self):
            return self.getToken(QuantumLanguageParser.NEWLINE, 0)

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.SEMI_COLON)
            else:
                return self.getToken(QuantumLanguageParser.SEMI_COLON, i)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = QuantumLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.sentence()
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 46
                    self.match(QuantumLanguageParser.SEMI_COLON)
                    self.state = 47
                    self.sentence() 
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 53
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 56
            self.match(QuantumLanguageParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IfContext,0)


        def for_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ForContext,0)


        def while_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.WhileContext,0)


        def try_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.TryContext,0)


        def function_execution(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Function_executionContext,0)


        def assign(self):
            return self.getTypedRuleContext(QuantumLanguageParser.AssignContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Function_declarationContext,0)


        def pass_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.PassContext,0)


        def expression(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_sentence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = QuantumLanguageParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentence)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.if_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.for_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.while_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.try_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.function_execution()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.assign()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 64
                self.function_declaration()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 65
                self.pass_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 66
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(QuantumLanguageParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(QuantumLanguageParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(QuantumLanguageParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.StatementContext,i)


        def elif_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.ElifContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.ElifContext,i)


        def else_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ElseContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = QuantumLanguageParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(QuantumLanguageParser.IF)
            self.state = 70
            self.expression(0)
            self.state = 71
            self.match(QuantumLanguageParser.COLON)
            self.state = 72
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 73
            self.match(QuantumLanguageParser.INDENT)
            self.state = 75 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 74
                self.statement()
                self.state = 77 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 2296836455324483587) != 0):
                    break

            self.state = 79
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 80
                self.elif_()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 86
                self.else_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(QuantumLanguageParser.ELIF, 0)

        def expression(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(QuantumLanguageParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(QuantumLanguageParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif" ):
                return visitor.visitElif(self)
            else:
                return visitor.visitChildren(self)




    def elif_(self):

        localctx = QuantumLanguageParser.ElifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_elif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(QuantumLanguageParser.ELIF)
            self.state = 90
            self.expression(0)
            self.state = 91
            self.match(QuantumLanguageParser.COLON)
            self.state = 92
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 93
            self.match(QuantumLanguageParser.INDENT)
            self.state = 95 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 94
                self.statement()
                self.state = 97 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 2296836455324483587) != 0):
                    break

            self.state = 99
            self.match(QuantumLanguageParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(QuantumLanguageParser.ELSE, 0)

        def COLON(self):
            return self.getToken(QuantumLanguageParser.COLON, 0)

        def NEWLINE(self):
            return self.getToken(QuantumLanguageParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = QuantumLanguageParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(QuantumLanguageParser.ELSE)
            self.state = 102
            self.match(QuantumLanguageParser.COLON)
            self.state = 103
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 104
            self.match(QuantumLanguageParser.INDENT)
            self.state = 106 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 105
                self.statement()
                self.state = 108 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 2296836455324483587) != 0):
                    break

            self.state = 110
            self.match(QuantumLanguageParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(QuantumLanguageParser.FOR, 0)

        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def IN(self):
            return self.getToken(QuantumLanguageParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(QuantumLanguageParser.COLON, 0)

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.SentenceContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,i)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)




    def for_(self):

        localctx = QuantumLanguageParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(QuantumLanguageParser.FOR)
            self.state = 113
            self.identifier()
            self.state = 114
            self.match(QuantumLanguageParser.IN)
            self.state = 115
            self.expression(0)
            self.state = 116
            self.match(QuantumLanguageParser.COLON)
            self.state = 117
            self.match(QuantumLanguageParser.INDENT)
            self.state = 119 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 118
                self.sentence()
                self.state = 121 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 2296836455324483587) != 0):
                    break

            self.state = 123
            self.match(QuantumLanguageParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(QuantumLanguageParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(QuantumLanguageParser.COLON, 0)

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.SentenceContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,i)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = QuantumLanguageParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(QuantumLanguageParser.WHILE)
            self.state = 126
            self.expression(0)
            self.state = 127
            self.match(QuantumLanguageParser.COLON)
            self.state = 128
            self.match(QuantumLanguageParser.INDENT)
            self.state = 130 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 129
                self.sentence()
                self.state = 132 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 2296836455324483587) != 0):
                    break

            self.state = 134
            self.match(QuantumLanguageParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(QuantumLanguageParser.TRY, 0)

        def COLON(self):
            return self.getToken(QuantumLanguageParser.COLON, 0)

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def except_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExceptContext,0)


        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.SentenceContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,i)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_try

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTry" ):
                return visitor.visitTry(self)
            else:
                return visitor.visitChildren(self)




    def try_(self):

        localctx = QuantumLanguageParser.TryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_try)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(QuantumLanguageParser.TRY)
            self.state = 137
            self.match(QuantumLanguageParser.COLON)
            self.state = 138
            self.match(QuantumLanguageParser.INDENT)
            self.state = 140 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 139
                self.sentence()
                self.state = 142 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 2296836455324483587) != 0):
                    break

            self.state = 144
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 145
            self.except_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExceptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXCEPT(self):
            return self.getToken(QuantumLanguageParser.EXCEPT, 0)

        def expression(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(QuantumLanguageParser.COLON, 0)

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.SentenceContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.NEWLINE)
            else:
                return self.getToken(QuantumLanguageParser.NEWLINE, i)

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.SEMI_COLON)
            else:
                return self.getToken(QuantumLanguageParser.SEMI_COLON, i)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_except

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExcept" ):
                return visitor.visitExcept(self)
            else:
                return visitor.visitChildren(self)




    def except_(self):

        localctx = QuantumLanguageParser.ExceptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_except)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(QuantumLanguageParser.EXCEPT)
            self.state = 148
            self.expression(0)
            self.state = 149
            self.match(QuantumLanguageParser.COLON)
            self.state = 150
            self.match(QuantumLanguageParser.INDENT)
            self.state = 159
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 151
                    self.sentence()

                    self.state = 153
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==51:
                        self.state = 152
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 155
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 162
            self.sentence()
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 163
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 166
            self.match(QuantumLanguageParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_executionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def OPEN_PAREN(self):
            return self.getToken(QuantumLanguageParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(QuantumLanguageParser.CLOSE_PAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.COMMA)
            else:
                return self.getToken(QuantumLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_function_execution

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_execution" ):
                return visitor.visitFunction_execution(self)
            else:
                return visitor.visitChildren(self)




    def function_execution(self):

        localctx = QuantumLanguageParser.Function_executionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_function_execution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.identifier()
            self.state = 169
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & 2296836386558312451) != 0:
                self.state = 170
                self.expression(0)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 171
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 172
                    self.expression(0)
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 180
            self.match(QuantumLanguageParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(QuantumLanguageParser.DEF, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,i)


        def OPEN_PAREN(self):
            return self.getToken(QuantumLanguageParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(QuantumLanguageParser.CLOSE_PAREN, 0)

        def COLON(self):
            return self.getToken(QuantumLanguageParser.COLON, 0)

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def sentence(self):
            return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,0)


        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.COMMA)
            else:
                return self.getToken(QuantumLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = QuantumLanguageParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(QuantumLanguageParser.DEF)
            self.state = 183
            self.identifier()
            self.state = 184
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 2017612633061982208) != 0:
                self.state = 185
                self.identifier()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 186
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 187
                    self.identifier()
                    self.state = 192
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 195
            self.match(QuantumLanguageParser.CLOSE_PAREN)
            self.state = 196
            self.match(QuantumLanguageParser.COLON)
            self.state = 197
            self.match(QuantumLanguageParser.INDENT)
            self.state = 198
            self.sentence()
            self.state = 199
            self.match(QuantumLanguageParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(QuantumLanguageParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,0)


        def SEMI_COLON(self):
            return self.getToken(QuantumLanguageParser.SEMI_COLON, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = QuantumLanguageParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.identifier()
            self.state = 202
            self.match(QuantumLanguageParser.ASSIGN)
            self.state = 203
            self.expression(0)
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 204
                self.match(QuantumLanguageParser.SEMI_COLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(QuantumLanguageParser.IDENTIFIER, 0)

        def QUBIT_IDENTIFIER(self):
            return self.getToken(QuantumLanguageParser.QUBIT_IDENTIFIER, 0)

        def QUBIT_TRANSPOSE_IDENTIFIER(self):
            return self.getToken(QuantumLanguageParser.QUBIT_TRANSPOSE_IDENTIFIER, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = QuantumLanguageParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 2017612633061982208) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(QuantumLanguageParser.OPEN_PAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,i)


        def CLOSE_PAREN(self):
            return self.getToken(QuantumLanguageParser.CLOSE_PAREN, 0)

        def prefix_unitary_operator(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Prefix_unitary_operatorContext,0)


        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def function_execution(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Function_executionContext,0)


        def INTEGER_LITERAL(self):
            return self.getToken(QuantumLanguageParser.INTEGER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(QuantumLanguageParser.STRING_LITERAL, 0)

        def IMAGINARY_LITERAL(self):
            return self.getToken(QuantumLanguageParser.IMAGINARY_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(QuantumLanguageParser.FLOAT_LITERAL, 0)

        def TRUE(self):
            return self.getToken(QuantumLanguageParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(QuantumLanguageParser.FALSE, 0)

        def QUBIT_STATE_LITERAL(self):
            return self.getToken(QuantumLanguageParser.QUBIT_STATE_LITERAL, 0)

        def binary_operator(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Binary_operatorContext,0)


        def suffix_unitary_operator(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Suffix_unitary_operatorContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = QuantumLanguageParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 210
                self.match(QuantumLanguageParser.OPEN_PAREN)
                self.state = 211
                self.expression(0)
                self.state = 212
                self.match(QuantumLanguageParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 214
                self.prefix_unitary_operator()
                self.state = 215
                self.expression(12)
                pass

            elif la_ == 3:
                self.state = 217
                self.identifier()
                pass

            elif la_ == 4:
                self.state = 218
                self.function_execution()
                pass

            elif la_ == 5:
                self.state = 219
                self.match(QuantumLanguageParser.INTEGER_LITERAL)
                pass

            elif la_ == 6:
                self.state = 220
                self.match(QuantumLanguageParser.STRING_LITERAL)
                pass

            elif la_ == 7:
                self.state = 221
                self.match(QuantumLanguageParser.IMAGINARY_LITERAL)
                pass

            elif la_ == 8:
                self.state = 222
                self.match(QuantumLanguageParser.FLOAT_LITERAL)
                pass

            elif la_ == 9:
                self.state = 223
                self.match(QuantumLanguageParser.TRUE)
                pass

            elif la_ == 10:
                self.state = 224
                self.match(QuantumLanguageParser.FALSE)
                pass

            elif la_ == 11:
                self.state = 225
                self.match(QuantumLanguageParser.QUBIT_STATE_LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 234
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = QuantumLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 228
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 229
                        self.binary_operator()
                        self.state = 230
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = QuantumLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 232
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 233
                        self.suffix_unitary_operator()
                        pass

             
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Binary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(QuantumLanguageParser.ADD, 0)

        def MINUS(self):
            return self.getToken(QuantumLanguageParser.MINUS, 0)

        def STAR(self):
            return self.getToken(QuantumLanguageParser.STAR, 0)

        def DIV(self):
            return self.getToken(QuantumLanguageParser.DIV, 0)

        def IDIV(self):
            return self.getToken(QuantumLanguageParser.IDIV, 0)

        def MOD(self):
            return self.getToken(QuantumLanguageParser.MOD, 0)

        def POWER(self):
            return self.getToken(QuantumLanguageParser.POWER, 0)

        def MATMUL(self):
            return self.getToken(QuantumLanguageParser.MATMUL, 0)

        def KRONECKER(self):
            return self.getToken(QuantumLanguageParser.KRONECKER, 0)

        def LESS_THAN(self):
            return self.getToken(QuantumLanguageParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(QuantumLanguageParser.GREATER_THAN, 0)

        def EQUALS(self):
            return self.getToken(QuantumLanguageParser.EQUALS, 0)

        def GT_EQ(self):
            return self.getToken(QuantumLanguageParser.GT_EQ, 0)

        def LT_EQ(self):
            return self.getToken(QuantumLanguageParser.LT_EQ, 0)

        def NOT_EQ_1(self):
            return self.getToken(QuantumLanguageParser.NOT_EQ_1, 0)

        def NOT_EQ_2(self):
            return self.getToken(QuantumLanguageParser.NOT_EQ_2, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_binary_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_operator" ):
                return visitor.visitBinary_operator(self)
            else:
                return visitor.visitChildren(self)




    def binary_operator(self):

        localctx = QuantumLanguageParser.Binary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_binary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 27021597764747232) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prefix_unitary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(QuantumLanguageParser.ADD, 0)

        def MINUS(self):
            return self.getToken(QuantumLanguageParser.MINUS, 0)

        def NOT(self):
            return self.getToken(QuantumLanguageParser.NOT, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_prefix_unitary_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrefix_unitary_operator" ):
                return visitor.visitPrefix_unitary_operator(self)
            else:
                return visitor.visitChildren(self)




    def prefix_unitary_operator(self):

        localctx = QuantumLanguageParser.Prefix_unitary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_prefix_unitary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 34359738464) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Suffix_unitary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HERMITIAN(self):
            return self.getToken(QuantumLanguageParser.HERMITIAN, 0)

        def CONJUGATE(self):
            return self.getToken(QuantumLanguageParser.CONJUGATE, 0)

        def TRANSPOSE(self):
            return self.getToken(QuantumLanguageParser.TRANSPOSE, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_suffix_unitary_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuffix_unitary_operator" ):
                return visitor.visitSuffix_unitary_operator(self)
            else:
                return visitor.visitChildren(self)




    def suffix_unitary_operator(self):

        localctx = QuantumLanguageParser.Suffix_unitary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_suffix_unitary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 252201579132747776) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PASS(self):
            return self.getToken(QuantumLanguageParser.PASS, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_pass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPass" ):
                return visitor.visitPass(self)
            else:
                return visitor.visitChildren(self)




    def pass_(self):

        localctx = QuantumLanguageParser.PassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_pass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(QuantumLanguageParser.PASS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         




