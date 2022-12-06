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
        4,1,81,258,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,4,0,44,8,0,11,0,12,0,45,1,0,1,0,1,1,1,1,1,1,5,1,53,8,1,
        10,1,12,1,56,9,1,1,1,3,1,59,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,72,8,2,1,3,1,3,1,3,1,3,1,3,1,3,4,3,80,8,3,11,3,12,
        3,81,1,3,1,3,5,3,86,8,3,10,3,12,3,89,9,3,1,3,3,3,92,8,3,1,4,1,4,
        1,4,1,4,1,4,1,4,4,4,100,8,4,11,4,12,4,101,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,4,5,111,8,5,11,5,12,5,112,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,4,6,125,8,6,11,6,12,6,126,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,4,7,137,8,7,11,7,12,7,138,1,7,1,7,1,8,1,8,1,8,1,8,1,8,4,8,148,
        8,8,11,8,12,8,149,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,4,9,161,8,
        9,11,9,12,9,162,1,9,1,9,1,10,1,10,1,10,1,10,1,10,5,10,172,8,10,10,
        10,12,10,175,9,10,3,10,177,8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,
        11,1,11,5,11,187,8,11,10,11,12,11,190,9,11,3,11,192,8,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,3,12,204,8,12,1,13,1,
        13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,3,14,235,8,14,1,14,1,14,1,14,1,14,5,14,241,8,14,10,14,12,
        14,244,9,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,
        20,1,20,1,20,0,1,28,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,0,6,1,0,73,75,2,0,5,18,68,69,2,0,5,6,35,35,1,0,70,
        72,1,0,44,51,1,0,52,56,275,0,43,1,0,0,0,2,49,1,0,0,0,4,71,1,0,0,
        0,6,73,1,0,0,0,8,93,1,0,0,0,10,105,1,0,0,0,12,116,1,0,0,0,14,130,
        1,0,0,0,16,142,1,0,0,0,18,154,1,0,0,0,20,166,1,0,0,0,22,180,1,0,
        0,0,24,199,1,0,0,0,26,205,1,0,0,0,28,234,1,0,0,0,30,245,1,0,0,0,
        32,247,1,0,0,0,34,249,1,0,0,0,36,251,1,0,0,0,38,253,1,0,0,0,40,255,
        1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,
        45,46,1,0,0,0,46,47,1,0,0,0,47,48,5,0,0,1,48,1,1,0,0,0,49,54,3,4,
        2,0,50,51,5,66,0,0,51,53,3,4,2,0,52,50,1,0,0,0,53,56,1,0,0,0,54,
        52,1,0,0,0,54,55,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,57,59,5,66,
        0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,5,67,0,0,61,
        3,1,0,0,0,62,72,3,6,3,0,63,72,3,12,6,0,64,72,3,14,7,0,65,72,3,16,
        8,0,66,72,3,20,10,0,67,72,3,24,12,0,68,72,3,22,11,0,69,72,3,40,20,
        0,70,72,3,28,14,0,71,62,1,0,0,0,71,63,1,0,0,0,71,64,1,0,0,0,71,65,
        1,0,0,0,71,66,1,0,0,0,71,67,1,0,0,0,71,68,1,0,0,0,71,69,1,0,0,0,
        71,70,1,0,0,0,72,5,1,0,0,0,73,74,5,24,0,0,74,75,3,28,14,0,75,76,
        5,65,0,0,76,77,5,67,0,0,77,79,5,1,0,0,78,80,3,2,1,0,79,78,1,0,0,
        0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,87,
        5,2,0,0,84,86,3,8,4,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,
        87,88,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,90,92,3,10,5,0,91,90,1,
        0,0,0,91,92,1,0,0,0,92,7,1,0,0,0,93,94,5,25,0,0,94,95,3,28,14,0,
        95,96,5,65,0,0,96,97,5,67,0,0,97,99,5,1,0,0,98,100,3,2,1,0,99,98,
        1,0,0,0,100,101,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,103,1,
        0,0,0,103,104,5,2,0,0,104,9,1,0,0,0,105,106,5,26,0,0,106,107,5,65,
        0,0,107,108,5,67,0,0,108,110,5,1,0,0,109,111,3,2,1,0,110,109,1,0,
        0,0,111,112,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,114,1,0,
        0,0,114,115,5,2,0,0,115,11,1,0,0,0,116,117,5,28,0,0,117,118,3,26,
        13,0,118,119,5,29,0,0,119,120,3,28,14,0,120,121,5,65,0,0,121,122,
        5,67,0,0,122,124,5,1,0,0,123,125,3,2,1,0,124,123,1,0,0,0,125,126,
        1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,129,
        5,2,0,0,129,13,1,0,0,0,130,131,5,27,0,0,131,132,3,28,14,0,132,133,
        5,65,0,0,133,134,5,67,0,0,134,136,5,1,0,0,135,137,3,2,1,0,136,135,
        1,0,0,0,137,138,1,0,0,0,138,136,1,0,0,0,138,139,1,0,0,0,139,140,
        1,0,0,0,140,141,5,2,0,0,141,15,1,0,0,0,142,143,5,30,0,0,143,144,
        5,65,0,0,144,145,5,67,0,0,145,147,5,1,0,0,146,148,3,2,1,0,147,146,
        1,0,0,0,148,149,1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,151,
        1,0,0,0,151,152,5,2,0,0,152,153,3,18,9,0,153,17,1,0,0,0,154,155,
        5,32,0,0,155,156,3,28,14,0,156,157,5,65,0,0,157,158,5,67,0,0,158,
        160,5,1,0,0,159,161,3,2,1,0,160,159,1,0,0,0,161,162,1,0,0,0,162,
        160,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,165,5,2,0,0,165,
        19,1,0,0,0,166,167,3,26,13,0,167,176,5,57,0,0,168,173,3,28,14,0,
        169,170,5,64,0,0,170,172,3,28,14,0,171,169,1,0,0,0,172,175,1,0,0,
        0,173,171,1,0,0,0,173,174,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,
        0,176,168,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,179,5,58,0,
        0,179,21,1,0,0,0,180,181,5,20,0,0,181,182,3,26,13,0,182,191,5,57,
        0,0,183,188,3,26,13,0,184,185,5,64,0,0,185,187,3,26,13,0,186,184,
        1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,192,
        1,0,0,0,190,188,1,0,0,0,191,183,1,0,0,0,191,192,1,0,0,0,192,193,
        1,0,0,0,193,194,5,58,0,0,194,195,5,65,0,0,195,196,5,1,0,0,196,197,
        3,4,2,0,197,198,5,2,0,0,198,23,1,0,0,0,199,200,3,26,13,0,200,201,
        5,19,0,0,201,203,3,28,14,0,202,204,5,66,0,0,203,202,1,0,0,0,203,
        204,1,0,0,0,204,25,1,0,0,0,205,206,7,0,0,0,206,27,1,0,0,0,207,208,
        6,14,-1,0,208,209,5,57,0,0,209,210,3,28,14,0,210,211,5,58,0,0,211,
        235,1,0,0,0,212,213,3,32,16,0,213,214,3,28,14,14,214,235,1,0,0,0,
        215,216,3,34,17,0,216,217,3,28,14,13,217,235,1,0,0,0,218,219,3,36,
        18,0,219,220,3,28,14,12,220,235,1,0,0,0,221,222,3,38,19,0,222,223,
        3,28,14,0,223,224,3,28,14,11,224,235,1,0,0,0,225,235,3,26,13,0,226,
        235,3,20,10,0,227,235,5,77,0,0,228,235,5,76,0,0,229,235,5,78,0,0,
        230,235,5,79,0,0,231,235,5,38,0,0,232,235,5,39,0,0,233,235,5,80,
        0,0,234,207,1,0,0,0,234,212,1,0,0,0,234,215,1,0,0,0,234,218,1,0,
        0,0,234,221,1,0,0,0,234,225,1,0,0,0,234,226,1,0,0,0,234,227,1,0,
        0,0,234,228,1,0,0,0,234,229,1,0,0,0,234,230,1,0,0,0,234,231,1,0,
        0,0,234,232,1,0,0,0,234,233,1,0,0,0,235,242,1,0,0,0,236,237,10,10,
        0,0,237,238,3,30,15,0,238,239,3,28,14,11,239,241,1,0,0,0,240,236,
        1,0,0,0,241,244,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,29,1,
        0,0,0,244,242,1,0,0,0,245,246,7,1,0,0,246,31,1,0,0,0,247,248,7,2,
        0,0,248,33,1,0,0,0,249,250,7,3,0,0,250,35,1,0,0,0,251,252,7,4,0,
        0,252,37,1,0,0,0,253,254,7,5,0,0,254,39,1,0,0,0,255,256,5,41,0,0,
        256,41,1,0,0,0,20,45,54,58,71,81,87,91,101,112,126,138,149,162,173,
        176,188,191,203,234,242
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
                     "'pass'", "'continue'", "'break'", "'X'", "'H'", "'Z'", 
                     "'Y'", "'S'", "'SDG'", "'Toffoli'", "'TDG'", "'RX'", 
                     "'RY'", "'RZ'", "'CX'", "'P'", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "'.'", "','", "':'", "';'", "<INVALID>", 
                     "'@'", "'(X)'", "'T'", "'''", "'t'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "SPACES", "COMMENTS", 
                      "ADD", "MINUS", "STAR", "DIV", "IDIV", "MOD", "POWER", 
                      "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", 
                      "NOT_EQ_1", "NOT_EQ_2", "ASSIGN", "DEF", "RETURN", 
                      "RAISE", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", 
                      "FOR", "IN", "TRY", "FINALLY", "EXCEPT", "OR", "AND", 
                      "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", "PASS", 
                      "CONTINUE", "BREAK", "X", "H", "Z", "Y", "S", "SDG", 
                      "T", "TDG", "RX", "RY", "RZ", "CX", "P", "OPEN_PAREN", 
                      "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
                      "CLOSE_BRACE", "DOT", "COMMA", "COLON", "SEMI_COLON", 
                      "NEWLINE", "MATMUL", "KRONECKER", "HERMITIAN", "CONJUGATE", 
                      "TRANSPOSE", "IDENTIFIER", "QUBIT_IDENTIFIER", "QUBIT_TRANSPOSE_IDENTIFIER", 
                      "STRING_LITERAL", "INTEGER_LITERAL", "IMAGINARY_LITERAL", 
                      "FLOAT_LITERAL", "QUBIT_STATE_LITERAL", "QUBIT_TRANSPOSE_STATE_LITERAL" ]

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
    RULE_single_qubit_gate = 18
    RULE_qubit_gate = 19
    RULE_pass = 20

    ruleNames =  [ "start", "statement", "sentence", "if", "elif", "else", 
                   "for", "while", "try", "except", "function_execution", 
                   "function_declaration", "assign", "identifier", "expression", 
                   "binary_operator", "prefix_unitary_operator", "suffix_unitary_operator", 
                   "single_qubit_gate", "qubit_gate", "pass" ]

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
    X=44
    H=45
    Z=46
    Y=47
    S=48
    SDG=49
    T=50
    TDG=51
    RX=52
    RY=53
    RZ=54
    CX=55
    P=56
    OPEN_PAREN=57
    CLOSE_PAREN=58
    OPEN_BRACK=59
    CLOSE_BRACK=60
    OPEN_BRACE=61
    CLOSE_BRACE=62
    DOT=63
    COMMA=64
    COLON=65
    SEMI_COLON=66
    NEWLINE=67
    MATMUL=68
    KRONECKER=69
    HERMITIAN=70
    CONJUGATE=71
    TRANSPOSE=72
    IDENTIFIER=73
    QUBIT_IDENTIFIER=74
    QUBIT_TRANSPOSE_IDENTIFIER=75
    STRING_LITERAL=76
    INTEGER_LITERAL=77
    IMAGINARY_LITERAL=78
    FLOAT_LITERAL=79
    QUBIT_STATE_LITERAL=80
    QUBIT_TRANSPOSE_STATE_LITERAL=81

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
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.statement()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 288215843476602976) != 0 or (((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 2047) != 0):
                    break

            self.state = 47
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
            self.state = 49
            self.sentence()
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self.match(QuantumLanguageParser.SEMI_COLON)
                    self.state = 51
                    self.sentence() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==66:
                self.state = 57
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 60
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
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.if_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.for_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.while_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.try_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.function_execution()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.assign()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.function_declaration()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.pass_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 70
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
            self.state = 73
            self.match(QuantumLanguageParser.IF)
            self.state = 74
            self.expression(0)
            self.state = 75
            self.match(QuantumLanguageParser.COLON)
            self.state = 76
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 77
            self.match(QuantumLanguageParser.INDENT)
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.statement()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 288215843476602976) != 0 or (((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 2047) != 0):
                    break

            self.state = 83
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 84
                self.elif_()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 90
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
            self.state = 93
            self.match(QuantumLanguageParser.ELIF)
            self.state = 94
            self.expression(0)
            self.state = 95
            self.match(QuantumLanguageParser.COLON)
            self.state = 96
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 97
            self.match(QuantumLanguageParser.INDENT)
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.statement()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 288215843476602976) != 0 or (((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 2047) != 0):
                    break

            self.state = 103
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
            self.state = 105
            self.match(QuantumLanguageParser.ELSE)
            self.state = 106
            self.match(QuantumLanguageParser.COLON)
            self.state = 107
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 108
            self.match(QuantumLanguageParser.INDENT)
            self.state = 110 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 109
                self.statement()
                self.state = 112 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 288215843476602976) != 0 or (((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 2047) != 0):
                    break

            self.state = 114
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
            self.state = 116
            self.match(QuantumLanguageParser.FOR)
            self.state = 117
            self.identifier()
            self.state = 118
            self.match(QuantumLanguageParser.IN)
            self.state = 119
            self.expression(0)
            self.state = 120
            self.match(QuantumLanguageParser.COLON)
            self.state = 121
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 122
            self.match(QuantumLanguageParser.INDENT)
            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 123
                self.statement()
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 288215843476602976) != 0 or (((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 2047) != 0):
                    break

            self.state = 128
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
            self.state = 130
            self.match(QuantumLanguageParser.WHILE)
            self.state = 131
            self.expression(0)
            self.state = 132
            self.match(QuantumLanguageParser.COLON)
            self.state = 133
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 134
            self.match(QuantumLanguageParser.INDENT)
            self.state = 136 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 135
                self.statement()
                self.state = 138 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 288215843476602976) != 0 or (((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 2047) != 0):
                    break

            self.state = 140
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

        def NEWLINE(self):
            return self.getToken(QuantumLanguageParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def except_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExceptContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.StatementContext,i)


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
            self.state = 142
            self.match(QuantumLanguageParser.TRY)
            self.state = 143
            self.match(QuantumLanguageParser.COLON)
            self.state = 144
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 145
            self.match(QuantumLanguageParser.INDENT)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 146
                self.statement()
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 288215843476602976) != 0 or (((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 2047) != 0):
                    break

            self.state = 151
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 152
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
            self.state = 154
            self.match(QuantumLanguageParser.EXCEPT)
            self.state = 155
            self.expression(0)
            self.state = 156
            self.match(QuantumLanguageParser.COLON)
            self.state = 157
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 158
            self.match(QuantumLanguageParser.INDENT)
            self.state = 160 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 159
                self.statement()
                self.state = 162 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 288215843476602976) != 0 or (((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 2047) != 0):
                    break

            self.state = 164
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
            self.state = 166
            self.identifier()
            self.state = 167
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 288213642959126624) != 0 or (((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 2047) != 0:
                self.state = 168
                self.expression(0)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==64:
                    self.state = 169
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 170
                    self.expression(0)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 178
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
            self.state = 180
            self.match(QuantumLanguageParser.DEF)
            self.state = 181
            self.identifier()
            self.state = 182
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 7) != 0:
                self.state = 183
                self.identifier()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==64:
                    self.state = 184
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 185
                    self.identifier()
                    self.state = 190
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 193
            self.match(QuantumLanguageParser.CLOSE_PAREN)
            self.state = 194
            self.match(QuantumLanguageParser.COLON)
            self.state = 195
            self.match(QuantumLanguageParser.INDENT)
            self.state = 196
            self.sentence()
            self.state = 197
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
            self.state = 199
            self.identifier()
            self.state = 200
            self.match(QuantumLanguageParser.ASSIGN)
            self.state = 201
            self.expression(0)
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 202
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
            self.state = 205
            _la = self._input.LA(1)
            if not((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & 7) != 0):
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


        def suffix_unitary_operator(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Suffix_unitary_operatorContext,0)


        def single_qubit_gate(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Single_qubit_gateContext,0)


        def qubit_gate(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Qubit_gateContext,0)


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
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 208
                self.match(QuantumLanguageParser.OPEN_PAREN)
                self.state = 209
                self.expression(0)
                self.state = 210
                self.match(QuantumLanguageParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 212
                self.prefix_unitary_operator()
                self.state = 213
                self.expression(14)
                pass

            elif la_ == 3:
                self.state = 215
                self.suffix_unitary_operator()
                self.state = 216
                self.expression(13)
                pass

            elif la_ == 4:
                self.state = 218
                self.single_qubit_gate()
                self.state = 219
                self.expression(12)
                pass

            elif la_ == 5:
                self.state = 221
                self.qubit_gate()
                self.state = 222
                self.expression(0)
                self.state = 223
                self.expression(11)
                pass

            elif la_ == 6:
                self.state = 225
                self.identifier()
                pass

            elif la_ == 7:
                self.state = 226
                self.function_execution()
                pass

            elif la_ == 8:
                self.state = 227
                self.match(QuantumLanguageParser.INTEGER_LITERAL)
                pass

            elif la_ == 9:
                self.state = 228
                self.match(QuantumLanguageParser.STRING_LITERAL)
                pass

            elif la_ == 10:
                self.state = 229
                self.match(QuantumLanguageParser.IMAGINARY_LITERAL)
                pass

            elif la_ == 11:
                self.state = 230
                self.match(QuantumLanguageParser.FLOAT_LITERAL)
                pass

            elif la_ == 12:
                self.state = 231
                self.match(QuantumLanguageParser.TRUE)
                pass

            elif la_ == 13:
                self.state = 232
                self.match(QuantumLanguageParser.FALSE)
                pass

            elif la_ == 14:
                self.state = 233
                self.match(QuantumLanguageParser.QUBIT_STATE_LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = QuantumLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 236
                    if not self.precpred(self._ctx, 10):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                    self.state = 237
                    self.binary_operator()
                    self.state = 238
                    self.expression(11) 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
            self.state = 245
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 524256) != 0 or _la==68 or _la==69):
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
            self.state = 247
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
            self.state = 249
            _la = self._input.LA(1)
            if not((((_la - 70)) & ~0x3f) == 0 and ((1 << (_la - 70)) & 7) != 0):
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


    class Single_qubit_gateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def X(self):
            return self.getToken(QuantumLanguageParser.X, 0)

        def Z(self):
            return self.getToken(QuantumLanguageParser.Z, 0)

        def Y(self):
            return self.getToken(QuantumLanguageParser.Y, 0)

        def H(self):
            return self.getToken(QuantumLanguageParser.H, 0)

        def S(self):
            return self.getToken(QuantumLanguageParser.S, 0)

        def SDG(self):
            return self.getToken(QuantumLanguageParser.SDG, 0)

        def T(self):
            return self.getToken(QuantumLanguageParser.T, 0)

        def TDG(self):
            return self.getToken(QuantumLanguageParser.TDG, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_single_qubit_gate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_qubit_gate" ):
                return visitor.visitSingle_qubit_gate(self)
            else:
                return visitor.visitChildren(self)




    def single_qubit_gate(self):

        localctx = QuantumLanguageParser.Single_qubit_gateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_single_qubit_gate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 4486007441326080) != 0):
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


    class Qubit_gateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RX(self):
            return self.getToken(QuantumLanguageParser.RX, 0)

        def RY(self):
            return self.getToken(QuantumLanguageParser.RY, 0)

        def RZ(self):
            return self.getToken(QuantumLanguageParser.RZ, 0)

        def CX(self):
            return self.getToken(QuantumLanguageParser.CX, 0)

        def P(self):
            return self.getToken(QuantumLanguageParser.P, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_qubit_gate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQubit_gate" ):
                return visitor.visitQubit_gate(self)
            else:
                return visitor.visitChildren(self)




    def qubit_gate(self):

        localctx = QuantumLanguageParser.Qubit_gateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_qubit_gate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 139611588448485376) != 0):
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
        self.enterRule(localctx, 40, self.RULE_pass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
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
         




