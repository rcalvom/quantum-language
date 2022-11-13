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
        4,1,64,198,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,3,0,23,8,0,1,0,1,0,5,0,27,8,0,
        10,0,12,0,30,9,0,1,0,1,0,3,0,34,8,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,
        42,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,2,1,2,5,2,54,8,2,10,
        2,12,2,57,9,2,1,2,1,2,3,2,61,8,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,69,
        8,2,1,2,1,2,5,2,73,8,2,10,2,12,2,76,9,2,1,2,1,2,3,2,80,8,2,1,2,1,
        2,5,2,84,8,2,10,2,12,2,87,9,2,1,2,1,2,1,2,1,2,1,2,3,2,94,8,2,1,2,
        1,2,5,2,98,8,2,10,2,12,2,101,9,2,1,2,1,2,3,2,105,8,2,1,2,1,2,3,2,
        109,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,119,8,3,1,3,1,3,5,3,
        123,8,3,10,3,12,3,126,9,3,1,3,1,3,3,3,130,8,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,3,4,140,8,4,1,4,1,4,5,4,144,8,4,10,4,12,4,147,9,4,
        1,4,1,4,3,4,151,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,5,6,162,
        8,6,10,6,12,6,165,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,3,7,183,8,7,1,7,1,7,1,7,1,7,5,7,189,8,7,10,
        7,12,7,192,9,7,1,8,1,8,1,9,1,9,1,9,0,1,14,10,0,2,4,6,8,10,12,14,
        16,18,0,2,2,0,9,15,21,27,2,0,9,10,44,44,221,0,28,1,0,0,0,2,41,1,
        0,0,0,4,43,1,0,0,0,6,110,1,0,0,0,8,133,1,0,0,0,10,154,1,0,0,0,12,
        158,1,0,0,0,14,182,1,0,0,0,16,193,1,0,0,0,18,195,1,0,0,0,20,22,3,
        2,1,0,21,23,5,62,0,0,22,21,1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,24,
        25,5,63,0,0,25,27,1,0,0,0,26,20,1,0,0,0,27,30,1,0,0,0,28,26,1,0,
        0,0,28,29,1,0,0,0,29,31,1,0,0,0,30,28,1,0,0,0,31,33,3,2,1,0,32,34,
        5,62,0,0,33,32,1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,35,36,5,0,0,1,
        36,1,1,0,0,0,37,42,3,4,2,0,38,42,3,6,3,0,39,42,3,8,4,0,40,42,3,10,
        5,0,41,37,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,3,
        1,0,0,0,43,44,5,33,0,0,44,45,3,14,7,0,45,46,5,61,0,0,46,55,5,1,0,
        0,47,49,3,2,1,0,48,50,5,62,0,0,49,48,1,0,0,0,49,50,1,0,0,0,50,51,
        1,0,0,0,51,52,5,63,0,0,52,54,1,0,0,0,53,47,1,0,0,0,54,57,1,0,0,0,
        55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,60,3,
        2,1,0,59,61,5,62,0,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,
        85,5,2,0,0,63,64,5,34,0,0,64,65,5,61,0,0,65,74,5,1,0,0,66,68,3,2,
        1,0,67,69,5,62,0,0,68,67,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,
        71,5,63,0,0,71,73,1,0,0,0,72,66,1,0,0,0,73,76,1,0,0,0,74,72,1,0,
        0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,79,3,2,1,0,78,80,
        5,62,0,0,79,78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,5,2,0,0,
        82,84,1,0,0,0,83,63,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,
        0,0,0,86,108,1,0,0,0,87,85,1,0,0,0,88,89,5,35,0,0,89,90,5,61,0,0,
        90,99,5,1,0,0,91,93,3,2,1,0,92,94,5,62,0,0,93,92,1,0,0,0,93,94,1,
        0,0,0,94,95,1,0,0,0,95,96,5,63,0,0,96,98,1,0,0,0,97,91,1,0,0,0,98,
        101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,102,1,0,0,0,101,99,
        1,0,0,0,102,104,3,2,1,0,103,105,5,62,0,0,104,103,1,0,0,0,104,105,
        1,0,0,0,105,106,1,0,0,0,106,107,5,2,0,0,107,109,1,0,0,0,108,88,1,
        0,0,0,108,109,1,0,0,0,109,5,1,0,0,0,110,111,5,37,0,0,111,112,3,14,
        7,0,112,113,5,38,0,0,113,114,3,14,7,0,114,115,5,61,0,0,115,124,5,
        1,0,0,116,118,3,2,1,0,117,119,5,62,0,0,118,117,1,0,0,0,118,119,1,
        0,0,0,119,120,1,0,0,0,120,121,5,63,0,0,121,123,1,0,0,0,122,116,1,
        0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,127,1,
        0,0,0,126,124,1,0,0,0,127,129,3,2,1,0,128,130,5,62,0,0,129,128,1,
        0,0,0,129,130,1,0,0,0,130,131,1,0,0,0,131,132,5,2,0,0,132,7,1,0,
        0,0,133,134,5,36,0,0,134,135,3,14,7,0,135,136,5,61,0,0,136,145,5,
        1,0,0,137,139,3,2,1,0,138,140,5,62,0,0,139,138,1,0,0,0,139,140,1,
        0,0,0,140,141,1,0,0,0,141,142,5,63,0,0,142,144,1,0,0,0,143,137,1,
        0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,148,1,
        0,0,0,147,145,1,0,0,0,148,150,3,2,1,0,149,151,5,62,0,0,150,149,1,
        0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,5,2,0,0,153,9,1,0,
        0,0,154,155,3,12,6,0,155,156,5,28,0,0,156,157,3,14,7,0,157,11,1,
        0,0,0,158,163,5,3,0,0,159,160,5,59,0,0,160,162,5,3,0,0,161,159,1,
        0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,13,1,0,
        0,0,165,163,1,0,0,0,166,167,6,7,-1,0,167,168,5,53,0,0,168,169,3,
        14,7,0,169,170,5,54,0,0,170,183,1,0,0,0,171,172,3,18,9,0,172,173,
        3,14,7,9,173,183,1,0,0,0,174,183,3,12,6,0,175,183,5,5,0,0,176,183,
        5,4,0,0,177,183,5,6,0,0,178,183,5,7,0,0,179,183,5,47,0,0,180,183,
        5,48,0,0,181,183,5,8,0,0,182,166,1,0,0,0,182,171,1,0,0,0,182,174,
        1,0,0,0,182,175,1,0,0,0,182,176,1,0,0,0,182,177,1,0,0,0,182,178,
        1,0,0,0,182,179,1,0,0,0,182,180,1,0,0,0,182,181,1,0,0,0,183,190,
        1,0,0,0,184,185,10,10,0,0,185,186,3,16,8,0,186,187,3,14,7,11,187,
        189,1,0,0,0,188,184,1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,
        191,1,0,0,0,191,15,1,0,0,0,192,190,1,0,0,0,193,194,7,0,0,0,194,17,
        1,0,0,0,195,196,7,1,0,0,196,19,1,0,0,0,24,22,28,33,41,49,55,60,68,
        74,79,85,93,99,104,108,118,124,129,139,145,150,163,182,190
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
    RULE_for = 3
    RULE_while = 4
    RULE_assign = 5
    RULE_identifier = 6
    RULE_expresion = 7
    RULE_binary_operator = 8
    RULE_unitary_operator = 9

    ruleNames =  [ "start", "sentence", "if", "for", "while", "assign", 
                   "identifier", "expresion", "binary_operator", "unitary_operator" ]

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
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 20
                    self.sentence()

                    self.state = 22
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 21
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 24
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 31
            self.sentence()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 32
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 35
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
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.if_()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.for_()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.while_()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.assign()
                pass
            else:
                raise NoViableAltException(self)

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

        def expresion(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpresionContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.COLON)
            else:
                return self.getToken(QuantumLanguageParser.COLON, i)

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.INDENT)
            else:
                return self.getToken(QuantumLanguageParser.INDENT, i)

        def DEDENT(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.DEDENT)
            else:
                return self.getToken(QuantumLanguageParser.DEDENT, i)

        def sentence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.SentenceContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.ELIF)
            else:
                return self.getToken(QuantumLanguageParser.ELIF, i)

        def ELSE(self):
            return self.getToken(QuantumLanguageParser.ELSE, 0)

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
            self.state = 43
            self.match(QuantumLanguageParser.IF)
            self.state = 44
            self.expresion(0)
            self.state = 45
            self.match(QuantumLanguageParser.COLON)
            self.state = 46
            self.match(QuantumLanguageParser.INDENT)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 47
                    self.sentence()

                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 48
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 51
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 58
            self.sentence()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 59
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 62
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 63
                self.match(QuantumLanguageParser.ELIF)
                self.state = 64
                self.match(QuantumLanguageParser.COLON)
                self.state = 65
                self.match(QuantumLanguageParser.INDENT)
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 66
                        self.sentence()

                        self.state = 68
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==62:
                            self.state = 67
                            self.match(QuantumLanguageParser.SEMI_COLON)


                        self.state = 70
                        self.match(QuantumLanguageParser.NEWLINE) 
                    self.state = 76
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                self.state = 77
                self.sentence()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==62:
                    self.state = 78
                    self.match(QuantumLanguageParser.SEMI_COLON)


                self.state = 81
                self.match(QuantumLanguageParser.DEDENT)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 88
                self.match(QuantumLanguageParser.ELSE)
                self.state = 89
                self.match(QuantumLanguageParser.COLON)
                self.state = 90
                self.match(QuantumLanguageParser.INDENT)
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 91
                        self.sentence()

                        self.state = 93
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==62:
                            self.state = 92
                            self.match(QuantumLanguageParser.SEMI_COLON)


                        self.state = 95
                        self.match(QuantumLanguageParser.NEWLINE) 
                    self.state = 101
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                self.state = 102
                self.sentence()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==62:
                    self.state = 103
                    self.match(QuantumLanguageParser.SEMI_COLON)


                self.state = 106
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

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.ExpresionContext,i)


        def IN(self):
            return self.getToken(QuantumLanguageParser.IN, 0)

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
        self.enterRule(localctx, 6, self.RULE_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(QuantumLanguageParser.FOR)
            self.state = 111
            self.expresion(0)
            self.state = 112
            self.match(QuantumLanguageParser.IN)
            self.state = 113
            self.expresion(0)
            self.state = 114
            self.match(QuantumLanguageParser.COLON)
            self.state = 115
            self.match(QuantumLanguageParser.INDENT)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 116
                    self.sentence()

                    self.state = 118
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 117
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 120
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 127
            self.sentence()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 128
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 131
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

        def expresion(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpresionContext,0)


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
        self.enterRule(localctx, 8, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(QuantumLanguageParser.WHILE)
            self.state = 134
            self.expresion(0)
            self.state = 135
            self.match(QuantumLanguageParser.COLON)
            self.state = 136
            self.match(QuantumLanguageParser.INDENT)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 137
                    self.sentence()

                    self.state = 139
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 138
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 141
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 148
            self.sentence()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 149
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 152
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

        def expresion(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpresionContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = QuantumLanguageParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.identifier()
            self.state = 155
            self.match(QuantumLanguageParser.ASSIGN)
            self.state = 156
            self.expresion(0)
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
        self.enterRule(localctx, 12, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(QuantumLanguageParser.IDENTIFIER)
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 159
                    self.match(QuantumLanguageParser.DOT)
                    self.state = 160
                    self.match(QuantumLanguageParser.IDENTIFIER) 
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(QuantumLanguageParser.OPEN_PAREN, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.ExpresionContext,i)


        def CLOSE_PAREN(self):
            return self.getToken(QuantumLanguageParser.CLOSE_PAREN, 0)

        def unitary_operator(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Unitary_operatorContext,0)


        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


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
            return QuantumLanguageParser.RULE_expresion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = QuantumLanguageParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expresion, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.state = 167
                self.match(QuantumLanguageParser.OPEN_PAREN)
                self.state = 168
                self.expresion(0)
                self.state = 169
                self.match(QuantumLanguageParser.CLOSE_PAREN)
                pass
            elif token in [9, 10, 44]:
                self.state = 171
                self.unitary_operator()
                self.state = 172
                self.expresion(9)
                pass
            elif token in [3]:
                self.state = 174
                self.identifier()
                pass
            elif token in [5]:
                self.state = 175
                self.match(QuantumLanguageParser.INTEGER_LITERAL)
                pass
            elif token in [4]:
                self.state = 176
                self.match(QuantumLanguageParser.STRING_LITERAL)
                pass
            elif token in [6]:
                self.state = 177
                self.match(QuantumLanguageParser.IMAGINARY_LITERAL)
                pass
            elif token in [7]:
                self.state = 178
                self.match(QuantumLanguageParser.FLOAT_LITERAL)
                pass
            elif token in [47]:
                self.state = 179
                self.match(QuantumLanguageParser.TRUE)
                pass
            elif token in [48]:
                self.state = 180
                self.match(QuantumLanguageParser.FALSE)
                pass
            elif token in [8]:
                self.state = 181
                self.match(QuantumLanguageParser.QUBIT_STATE_LITERAL)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = QuantumLanguageParser.ExpresionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                    self.state = 184
                    if not self.precpred(self._ctx, 10):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                    self.state = 185
                    self.binary_operator()
                    self.state = 186
                    self.expresion(11) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_binary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
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
        self.enterRule(localctx, 18, self.RULE_unitary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        self._predicates[7] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         




