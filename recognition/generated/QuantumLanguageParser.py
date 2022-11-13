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
        4,1,64,273,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,3,0,33,8,0,1,0,1,0,5,0,37,8,0,10,0,12,0,40,9,0,
        1,0,1,0,3,0,44,8,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,54,8,1,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,62,8,2,1,2,1,2,5,2,66,8,2,10,2,12,2,69,
        9,2,1,2,1,2,3,2,73,8,2,1,2,1,2,5,2,77,8,2,10,2,12,2,80,9,2,1,2,3,
        2,83,8,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,91,8,3,1,3,1,3,5,3,95,8,3,10,
        3,12,3,98,9,3,1,3,1,3,3,3,102,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,
        4,111,8,4,1,4,1,4,5,4,115,8,4,10,4,12,4,118,9,4,1,4,1,4,3,4,122,
        8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,134,8,5,1,5,1,5,
        5,5,138,8,5,10,5,12,5,141,9,5,1,5,1,5,3,5,145,8,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,155,8,6,1,6,1,6,5,6,159,8,6,10,6,12,6,162,
        9,6,1,6,1,6,3,6,166,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,175,8,7,
        1,7,1,7,5,7,179,8,7,10,7,12,7,182,9,7,1,7,1,7,3,7,186,8,7,1,7,1,
        7,4,7,190,8,7,11,7,12,7,191,1,8,1,8,1,8,1,8,1,8,1,8,3,8,200,8,8,
        1,8,1,8,5,8,204,8,8,10,8,12,8,207,9,8,1,8,1,8,3,8,211,8,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,5,9,220,8,9,10,9,12,9,223,9,9,3,9,225,8,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,236,8,11,10,11,12,
        11,239,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,258,8,12,1,12,1,12,1,12,1,
        12,5,12,264,8,12,10,12,12,12,267,9,12,1,13,1,13,1,14,1,14,1,14,0,
        1,24,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,2,2,0,9,15,21,
        27,2,0,9,10,44,44,303,0,38,1,0,0,0,2,53,1,0,0,0,4,55,1,0,0,0,6,84,
        1,0,0,0,8,105,1,0,0,0,10,125,1,0,0,0,12,148,1,0,0,0,14,169,1,0,0,
        0,16,193,1,0,0,0,18,214,1,0,0,0,20,228,1,0,0,0,22,232,1,0,0,0,24,
        257,1,0,0,0,26,268,1,0,0,0,28,270,1,0,0,0,30,32,3,2,1,0,31,33,5,
        62,0,0,32,31,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,35,5,63,0,0,
        35,37,1,0,0,0,36,30,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,
        0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,43,3,2,1,0,42,44,5,62,0,0,43,
        42,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,46,5,0,0,1,46,1,1,0,0,
        0,47,54,3,4,2,0,48,54,3,10,5,0,49,54,3,12,6,0,50,54,3,14,7,0,51,
        54,3,18,9,0,52,54,3,20,10,0,53,47,1,0,0,0,53,48,1,0,0,0,53,49,1,
        0,0,0,53,50,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,3,1,0,0,0,55,
        56,5,33,0,0,56,57,3,24,12,0,57,58,5,61,0,0,58,67,5,1,0,0,59,61,3,
        2,1,0,60,62,5,62,0,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,
        64,5,63,0,0,64,66,1,0,0,0,65,59,1,0,0,0,66,69,1,0,0,0,67,65,1,0,
        0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,0,70,72,3,2,1,0,71,73,
        5,62,0,0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,78,5,2,0,0,
        75,77,3,6,3,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,
        0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,81,83,3,8,4,0,82,81,1,0,0,0,82,
        83,1,0,0,0,83,5,1,0,0,0,84,85,5,34,0,0,85,86,3,24,12,0,86,87,5,61,
        0,0,87,96,5,1,0,0,88,90,3,2,1,0,89,91,5,62,0,0,90,89,1,0,0,0,90,
        91,1,0,0,0,91,92,1,0,0,0,92,93,5,63,0,0,93,95,1,0,0,0,94,88,1,0,
        0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,98,96,
        1,0,0,0,99,101,3,2,1,0,100,102,5,62,0,0,101,100,1,0,0,0,101,102,
        1,0,0,0,102,103,1,0,0,0,103,104,5,2,0,0,104,7,1,0,0,0,105,106,5,
        35,0,0,106,107,5,61,0,0,107,116,5,1,0,0,108,110,3,2,1,0,109,111,
        5,62,0,0,110,109,1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,
        5,63,0,0,113,115,1,0,0,0,114,108,1,0,0,0,115,118,1,0,0,0,116,114,
        1,0,0,0,116,117,1,0,0,0,117,119,1,0,0,0,118,116,1,0,0,0,119,121,
        3,2,1,0,120,122,5,62,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,123,
        1,0,0,0,123,124,5,2,0,0,124,9,1,0,0,0,125,126,5,37,0,0,126,127,3,
        22,11,0,127,128,5,38,0,0,128,129,3,24,12,0,129,130,5,61,0,0,130,
        139,5,1,0,0,131,133,3,2,1,0,132,134,5,62,0,0,133,132,1,0,0,0,133,
        134,1,0,0,0,134,135,1,0,0,0,135,136,5,63,0,0,136,138,1,0,0,0,137,
        131,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,
        142,1,0,0,0,141,139,1,0,0,0,142,144,3,2,1,0,143,145,5,62,0,0,144,
        143,1,0,0,0,144,145,1,0,0,0,145,146,1,0,0,0,146,147,5,2,0,0,147,
        11,1,0,0,0,148,149,5,36,0,0,149,150,3,24,12,0,150,151,5,61,0,0,151,
        160,5,1,0,0,152,154,3,2,1,0,153,155,5,62,0,0,154,153,1,0,0,0,154,
        155,1,0,0,0,155,156,1,0,0,0,156,157,5,63,0,0,157,159,1,0,0,0,158,
        152,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,
        163,1,0,0,0,162,160,1,0,0,0,163,165,3,2,1,0,164,166,5,62,0,0,165,
        164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,168,5,2,0,0,168,
        13,1,0,0,0,169,170,5,39,0,0,170,171,5,61,0,0,171,180,5,1,0,0,172,
        174,3,2,1,0,173,175,5,62,0,0,174,173,1,0,0,0,174,175,1,0,0,0,175,
        176,1,0,0,0,176,177,5,63,0,0,177,179,1,0,0,0,178,172,1,0,0,0,179,
        182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,183,1,0,0,0,182,
        180,1,0,0,0,183,185,3,2,1,0,184,186,5,62,0,0,185,184,1,0,0,0,185,
        186,1,0,0,0,186,187,1,0,0,0,187,189,5,2,0,0,188,190,3,16,8,0,189,
        188,1,0,0,0,190,191,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,
        15,1,0,0,0,193,194,5,41,0,0,194,195,3,24,12,0,195,196,5,61,0,0,196,
        205,5,1,0,0,197,199,3,2,1,0,198,200,5,62,0,0,199,198,1,0,0,0,199,
        200,1,0,0,0,200,201,1,0,0,0,201,202,5,63,0,0,202,204,1,0,0,0,203,
        197,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,
        208,1,0,0,0,207,205,1,0,0,0,208,210,3,2,1,0,209,211,5,62,0,0,210,
        209,1,0,0,0,210,211,1,0,0,0,211,212,1,0,0,0,212,213,5,2,0,0,213,
        17,1,0,0,0,214,215,3,22,11,0,215,224,5,53,0,0,216,221,3,24,12,0,
        217,218,5,60,0,0,218,220,3,24,12,0,219,217,1,0,0,0,220,223,1,0,0,
        0,221,219,1,0,0,0,221,222,1,0,0,0,222,225,1,0,0,0,223,221,1,0,0,
        0,224,216,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,226,227,5,54,0,
        0,227,19,1,0,0,0,228,229,3,22,11,0,229,230,5,28,0,0,230,231,3,24,
        12,0,231,21,1,0,0,0,232,237,5,3,0,0,233,234,5,59,0,0,234,236,5,3,
        0,0,235,233,1,0,0,0,236,239,1,0,0,0,237,235,1,0,0,0,237,238,1,0,
        0,0,238,23,1,0,0,0,239,237,1,0,0,0,240,241,6,12,-1,0,241,242,5,53,
        0,0,242,243,3,24,12,0,243,244,5,54,0,0,244,258,1,0,0,0,245,246,3,
        28,14,0,246,247,3,24,12,10,247,258,1,0,0,0,248,258,3,22,11,0,249,
        258,3,18,9,0,250,258,5,5,0,0,251,258,5,4,0,0,252,258,5,6,0,0,253,
        258,5,7,0,0,254,258,5,47,0,0,255,258,5,48,0,0,256,258,5,8,0,0,257,
        240,1,0,0,0,257,245,1,0,0,0,257,248,1,0,0,0,257,249,1,0,0,0,257,
        250,1,0,0,0,257,251,1,0,0,0,257,252,1,0,0,0,257,253,1,0,0,0,257,
        254,1,0,0,0,257,255,1,0,0,0,257,256,1,0,0,0,258,265,1,0,0,0,259,
        260,10,11,0,0,260,261,3,26,13,0,261,262,3,24,12,12,262,264,1,0,0,
        0,263,259,1,0,0,0,264,267,1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,
        0,266,25,1,0,0,0,267,265,1,0,0,0,268,269,7,0,0,0,269,27,1,0,0,0,
        270,271,7,1,0,0,271,29,1,0,0,0,33,32,38,43,53,61,67,72,78,82,90,
        96,101,110,116,121,133,139,144,154,160,165,174,180,185,191,199,205,
        210,221,224,237,257,265
    ]

class QuantumLanguageParser ( Parser ):

    grammarFileName = "QuantumLanguageParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'//'", "'%'", 
                     "'**'", "'|'", "'^'", "'&'", "'<<'", "'>>'", "'<'", 
                     "'>'", "'=='", "'>='", "'<='", "'<>'", "'!='", "'='", 
                     "'def'", "'return'", "'raise'", "'assert'", "'if'", 
                     "'elif'", "'else'", "'while'", "'for'", "'in'", "'try'", 
                     "'finally'", "'except'", "'or'", "'and'", "'not'", 
                     "'is'", "'None'", "'True'", "'False'", "'class'", "'pass'", 
                     "'continue'", "'break'", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'", "'.'", "','", "':'", "';'", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "IDENTIFIER", "STRING_LITERAL", 
                      "INTEGER_LITERAL", "IMAGINARY_LITERAL", "FLOAT_LITERAL", 
                      "QUBIT_STATE_LITERAL", "ADD", "MINUS", "STAR", "DIV", 
                      "IDIV", "MOD", "POWER", "OR_OP", "XOR", "AND_OP", 
                      "LEFT_SHIFT", "RIGHT_SHIFT", "LESS_THAN", "GREATER_THAN", 
                      "EQUALS", "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", 
                      "ASSIGN", "DEF", "RETURN", "RAISE", "ASSERT", "IF", 
                      "ELIF", "ELSE", "WHILE", "FOR", "IN", "TRY", "FINALLY", 
                      "EXCEPT", "OR", "AND", "NOT", "IS", "NONE", "TRUE", 
                      "FALSE", "CLASS", "PASS", "CONTINUE", "BREAK", "OPEN_PAREN", 
                      "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", 
                      "CLOSE_BRACE", "DOT", "COMMA", "COLON", "SEMI_COLON", 
                      "NEWLINE", "SKIP_" ]

    RULE_start = 0
    RULE_sentence = 1
    RULE_if = 2
    RULE_elif = 3
    RULE_else = 4
    RULE_for = 5
    RULE_while = 6
    RULE_try = 7
    RULE_except = 8
    RULE_function_execution = 9
    RULE_assign = 10
    RULE_identifier = 11
    RULE_expression = 12
    RULE_binary_operator = 13
    RULE_unitary_operator = 14

    ruleNames =  [ "start", "sentence", "if", "elif", "else", "for", "while", 
                   "try", "except", "function_execution", "assign", "identifier", 
                   "expression", "binary_operator", "unitary_operator" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    IDENTIFIER=3
    STRING_LITERAL=4
    INTEGER_LITERAL=5
    IMAGINARY_LITERAL=6
    FLOAT_LITERAL=7
    QUBIT_STATE_LITERAL=8
    ADD=9
    MINUS=10
    STAR=11
    DIV=12
    IDIV=13
    MOD=14
    POWER=15
    OR_OP=16
    XOR=17
    AND_OP=18
    LEFT_SHIFT=19
    RIGHT_SHIFT=20
    LESS_THAN=21
    GREATER_THAN=22
    EQUALS=23
    GT_EQ=24
    LT_EQ=25
    NOT_EQ_1=26
    NOT_EQ_2=27
    ASSIGN=28
    DEF=29
    RETURN=30
    RAISE=31
    ASSERT=32
    IF=33
    ELIF=34
    ELSE=35
    WHILE=36
    FOR=37
    IN=38
    TRY=39
    FINALLY=40
    EXCEPT=41
    OR=42
    AND=43
    NOT=44
    IS=45
    NONE=46
    TRUE=47
    FALSE=48
    CLASS=49
    PASS=50
    CONTINUE=51
    BREAK=52
    OPEN_PAREN=53
    CLOSE_PAREN=54
    OPEN_BRACK=55
    CLOSE_BRACK=56
    OPEN_BRACE=57
    CLOSE_BRACE=58
    DOT=59
    COMMA=60
    COLON=61
    SEMI_COLON=62
    NEWLINE=63
    SKIP_=64

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
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30
                    self.sentence()

                    self.state = 32
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 31
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 34
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 41
            self.sentence()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 42
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 45
            self.match(QuantumLanguageParser.EOF)
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


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_sentence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentence" ):
                return visitor.visitSentence(self)
            else:
                return visitor.visitChildren(self)




    def sentence(self):

        localctx = QuantumLanguageParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentence)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.if_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.for_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.while_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.try_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 51
                self.function_execution()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.assign()
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

        def INDENT(self):
            return self.getToken(QuantumLanguageParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(QuantumLanguageParser.DEDENT, 0)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.SentenceContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,i)


        def elif_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.ElifContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.ElifContext,i)


        def else_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ElseContext,0)


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
            return QuantumLanguageParser.RULE_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = QuantumLanguageParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(QuantumLanguageParser.IF)
            self.state = 56
            self.expression(0)
            self.state = 57
            self.match(QuantumLanguageParser.COLON)
            self.state = 58
            self.match(QuantumLanguageParser.INDENT)
            self.state = 67
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59
                    self.sentence()

                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 60
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 63
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 69
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 70
            self.sentence()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 71
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 74
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 75
                self.elif_()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 81
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
            return QuantumLanguageParser.RULE_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif" ):
                return visitor.visitElif(self)
            else:
                return visitor.visitChildren(self)




    def elif_(self):

        localctx = QuantumLanguageParser.ElifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_elif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(QuantumLanguageParser.ELIF)
            self.state = 85
            self.expression(0)
            self.state = 86
            self.match(QuantumLanguageParser.COLON)
            self.state = 87
            self.match(QuantumLanguageParser.INDENT)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 88
                    self.sentence()

                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 89
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 92
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 99
            self.sentence()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 100
                self.match(QuantumLanguageParser.SEMI_COLON)


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
            return QuantumLanguageParser.RULE_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)




    def else_(self):

        localctx = QuantumLanguageParser.ElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(QuantumLanguageParser.ELSE)
            self.state = 106
            self.match(QuantumLanguageParser.COLON)
            self.state = 107
            self.match(QuantumLanguageParser.INDENT)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 108
                    self.sentence()

                    self.state = 110
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 109
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 112
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 119
            self.sentence()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 120
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 123
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
            return QuantumLanguageParser.RULE_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)




    def for_(self):

        localctx = QuantumLanguageParser.ForContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(QuantumLanguageParser.FOR)
            self.state = 126
            self.identifier()
            self.state = 127
            self.match(QuantumLanguageParser.IN)
            self.state = 128
            self.expression(0)
            self.state = 129
            self.match(QuantumLanguageParser.COLON)
            self.state = 130
            self.match(QuantumLanguageParser.INDENT)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 131
                    self.sentence()

                    self.state = 133
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 132
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 135
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 142
            self.sentence()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 143
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 146
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
            return QuantumLanguageParser.RULE_while

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = QuantumLanguageParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(QuantumLanguageParser.WHILE)
            self.state = 149
            self.expression(0)
            self.state = 150
            self.match(QuantumLanguageParser.COLON)
            self.state = 151
            self.match(QuantumLanguageParser.INDENT)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 152
                    self.sentence()

                    self.state = 154
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 153
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 156
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 163
            self.sentence()
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 164
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 167
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

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.SentenceContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,i)


        def except_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.ExceptContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.ExceptContext,i)


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
            return QuantumLanguageParser.RULE_try

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTry" ):
                return visitor.visitTry(self)
            else:
                return visitor.visitChildren(self)




    def try_(self):

        localctx = QuantumLanguageParser.TryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_try)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(QuantumLanguageParser.TRY)
            self.state = 170
            self.match(QuantumLanguageParser.COLON)
            self.state = 171
            self.match(QuantumLanguageParser.INDENT)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 172
                    self.sentence()

                    self.state = 174
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 173
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 176
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 183
            self.sentence()
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 184
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 187
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 189 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 188
                self.except_()
                self.state = 191 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==41):
                    break

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
        self.enterRule(localctx, 16, self.RULE_except)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(QuantumLanguageParser.EXCEPT)
            self.state = 194
            self.expression(0)
            self.state = 195
            self.match(QuantumLanguageParser.COLON)
            self.state = 196
            self.match(QuantumLanguageParser.INDENT)
            self.state = 205
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 197
                    self.sentence()

                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 198
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 201
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 208
            self.sentence()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 209
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 212
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
        self.enterRule(localctx, 18, self.RULE_function_execution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.identifier()
            self.state = 215
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 9447003905853432) != 0:
                self.state = 216
                self.expression(0)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==60:
                    self.state = 217
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 218
                    self.expression(0)
                    self.state = 223
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 226
            self.match(QuantumLanguageParser.CLOSE_PAREN)
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


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = QuantumLanguageParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.identifier()
            self.state = 229
            self.match(QuantumLanguageParser.ASSIGN)
            self.state = 230
            self.expression(0)
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

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.IDENTIFIER)
            else:
                return self.getToken(QuantumLanguageParser.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.DOT)
            else:
                return self.getToken(QuantumLanguageParser.DOT, i)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = QuantumLanguageParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(QuantumLanguageParser.IDENTIFIER)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 233
                    self.match(QuantumLanguageParser.DOT)
                    self.state = 234
                    self.match(QuantumLanguageParser.IDENTIFIER) 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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

        def unitary_operator(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Unitary_operatorContext,0)


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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 241
                self.match(QuantumLanguageParser.OPEN_PAREN)
                self.state = 242
                self.expression(0)
                self.state = 243
                self.match(QuantumLanguageParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 245
                self.unitary_operator()
                self.state = 246
                self.expression(10)
                pass

            elif la_ == 3:
                self.state = 248
                self.identifier()
                pass

            elif la_ == 4:
                self.state = 249
                self.function_execution()
                pass

            elif la_ == 5:
                self.state = 250
                self.match(QuantumLanguageParser.INTEGER_LITERAL)
                pass

            elif la_ == 6:
                self.state = 251
                self.match(QuantumLanguageParser.STRING_LITERAL)
                pass

            elif la_ == 7:
                self.state = 252
                self.match(QuantumLanguageParser.IMAGINARY_LITERAL)
                pass

            elif la_ == 8:
                self.state = 253
                self.match(QuantumLanguageParser.FLOAT_LITERAL)
                pass

            elif la_ == 9:
                self.state = 254
                self.match(QuantumLanguageParser.TRUE)
                pass

            elif la_ == 10:
                self.state = 255
                self.match(QuantumLanguageParser.FALSE)
                pass

            elif la_ == 11:
                self.state = 256
                self.match(QuantumLanguageParser.QUBIT_STATE_LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 265
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = QuantumLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 259
                    if not self.precpred(self._ctx, 11):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                    self.state = 260
                    self.binary_operator()
                    self.state = 261
                    self.expression(12) 
                self.state = 267
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_binary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 266403328) != 0):
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


    class Unitary_operatorContext(ParserRuleContext):
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
            return QuantumLanguageParser.RULE_unitary_operator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnitary_operator" ):
                return visitor.visitUnitary_operator(self)
            else:
                return visitor.visitChildren(self)




    def unitary_operator(self):

        localctx = QuantumLanguageParser.Unitary_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_unitary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 17592186045952) != 0):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         




