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
        4,1,64,293,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,3,0,37,8,0,1,0,1,0,5,0,41,
        8,0,10,0,12,0,44,9,0,1,0,1,0,3,0,48,8,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,3,1,58,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,68,8,3,1,
        3,1,3,5,3,72,8,3,10,3,12,3,75,9,3,1,3,1,3,3,3,79,8,3,1,3,1,3,5,3,
        83,8,3,10,3,12,3,86,9,3,1,3,3,3,89,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,97,8,4,1,4,1,4,5,4,101,8,4,10,4,12,4,104,9,4,1,4,1,4,3,4,108,8,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,5,117,8,5,1,5,1,5,5,5,121,8,5,10,
        5,12,5,124,9,5,1,5,1,5,3,5,128,8,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,3,6,140,8,6,1,6,1,6,5,6,144,8,6,10,6,12,6,147,9,6,1,6,
        1,6,3,6,151,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,161,8,7,1,7,
        1,7,5,7,165,8,7,10,7,12,7,168,9,7,1,7,1,7,3,7,172,8,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,8,3,8,181,8,8,1,8,1,8,5,8,185,8,8,10,8,12,8,188,
        9,8,1,8,1,8,3,8,192,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,
        203,8,9,1,9,1,9,5,9,207,8,9,10,9,12,9,210,9,9,1,9,1,9,3,9,214,8,
        9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,5,10,223,8,10,10,10,12,10,226,
        9,10,3,10,228,8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,
        238,8,11,10,11,12,11,241,9,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,5,13,256,8,13,10,13,12,13,259,9,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,
        1,14,1,14,1,14,1,14,3,14,278,8,14,1,14,1,14,1,14,1,14,5,14,284,8,
        14,10,14,12,14,287,9,14,1,15,1,15,1,16,1,16,1,16,0,1,28,17,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,0,2,2,0,9,15,21,27,2,0,9,
        10,44,44,321,0,42,1,0,0,0,2,57,1,0,0,0,4,59,1,0,0,0,6,61,1,0,0,0,
        8,90,1,0,0,0,10,111,1,0,0,0,12,131,1,0,0,0,14,154,1,0,0,0,16,175,
        1,0,0,0,18,196,1,0,0,0,20,217,1,0,0,0,22,231,1,0,0,0,24,248,1,0,
        0,0,26,252,1,0,0,0,28,277,1,0,0,0,30,288,1,0,0,0,32,290,1,0,0,0,
        34,36,3,2,1,0,35,37,5,62,0,0,36,35,1,0,0,0,36,37,1,0,0,0,37,38,1,
        0,0,0,38,39,5,63,0,0,39,41,1,0,0,0,40,34,1,0,0,0,41,44,1,0,0,0,42,
        40,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,44,42,1,0,0,0,45,47,3,2,1,
        0,46,48,5,62,0,0,47,46,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,
        5,0,0,1,50,1,1,0,0,0,51,58,3,6,3,0,52,58,3,12,6,0,53,58,3,14,7,0,
        54,58,3,16,8,0,55,58,3,20,10,0,56,58,3,24,12,0,57,51,1,0,0,0,57,
        52,1,0,0,0,57,53,1,0,0,0,57,54,1,0,0,0,57,55,1,0,0,0,57,56,1,0,0,
        0,58,3,1,0,0,0,59,60,3,22,11,0,60,5,1,0,0,0,61,62,5,33,0,0,62,63,
        3,28,14,0,63,64,5,61,0,0,64,73,5,1,0,0,65,67,3,2,1,0,66,68,5,62,
        0,0,67,66,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,5,63,0,0,70,
        72,1,0,0,0,71,65,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,
        0,74,76,1,0,0,0,75,73,1,0,0,0,76,78,3,2,1,0,77,79,5,62,0,0,78,77,
        1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,80,84,5,2,0,0,81,83,3,8,4,0,
        82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,88,1,
        0,0,0,86,84,1,0,0,0,87,89,3,10,5,0,88,87,1,0,0,0,88,89,1,0,0,0,89,
        7,1,0,0,0,90,91,5,34,0,0,91,92,3,28,14,0,92,93,5,61,0,0,93,102,5,
        1,0,0,94,96,3,2,1,0,95,97,5,62,0,0,96,95,1,0,0,0,96,97,1,0,0,0,97,
        98,1,0,0,0,98,99,5,63,0,0,99,101,1,0,0,0,100,94,1,0,0,0,101,104,
        1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,105,1,0,0,0,104,102,
        1,0,0,0,105,107,3,2,1,0,106,108,5,62,0,0,107,106,1,0,0,0,107,108,
        1,0,0,0,108,109,1,0,0,0,109,110,5,2,0,0,110,9,1,0,0,0,111,112,5,
        35,0,0,112,113,5,61,0,0,113,122,5,1,0,0,114,116,3,2,1,0,115,117,
        5,62,0,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,
        5,63,0,0,119,121,1,0,0,0,120,114,1,0,0,0,121,124,1,0,0,0,122,120,
        1,0,0,0,122,123,1,0,0,0,123,125,1,0,0,0,124,122,1,0,0,0,125,127,
        3,2,1,0,126,128,5,62,0,0,127,126,1,0,0,0,127,128,1,0,0,0,128,129,
        1,0,0,0,129,130,5,2,0,0,130,11,1,0,0,0,131,132,5,37,0,0,132,133,
        3,26,13,0,133,134,5,38,0,0,134,135,3,28,14,0,135,136,5,61,0,0,136,
        145,5,1,0,0,137,139,3,2,1,0,138,140,5,62,0,0,139,138,1,0,0,0,139,
        140,1,0,0,0,140,141,1,0,0,0,141,142,5,63,0,0,142,144,1,0,0,0,143,
        137,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,
        148,1,0,0,0,147,145,1,0,0,0,148,150,3,2,1,0,149,151,5,62,0,0,150,
        149,1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,5,2,0,0,153,
        13,1,0,0,0,154,155,5,36,0,0,155,156,3,28,14,0,156,157,5,61,0,0,157,
        166,5,1,0,0,158,160,3,2,1,0,159,161,5,62,0,0,160,159,1,0,0,0,160,
        161,1,0,0,0,161,162,1,0,0,0,162,163,5,63,0,0,163,165,1,0,0,0,164,
        158,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,
        169,1,0,0,0,168,166,1,0,0,0,169,171,3,2,1,0,170,172,5,62,0,0,171,
        170,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,2,0,0,174,
        15,1,0,0,0,175,176,5,39,0,0,176,177,5,61,0,0,177,186,5,1,0,0,178,
        180,3,2,1,0,179,181,5,62,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,
        182,1,0,0,0,182,183,5,63,0,0,183,185,1,0,0,0,184,178,1,0,0,0,185,
        188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,
        186,1,0,0,0,189,191,3,2,1,0,190,192,5,62,0,0,191,190,1,0,0,0,191,
        192,1,0,0,0,192,193,1,0,0,0,193,194,5,2,0,0,194,195,3,18,9,0,195,
        17,1,0,0,0,196,197,5,41,0,0,197,198,3,28,14,0,198,199,5,61,0,0,199,
        208,5,1,0,0,200,202,3,2,1,0,201,203,5,62,0,0,202,201,1,0,0,0,202,
        203,1,0,0,0,203,204,1,0,0,0,204,205,5,63,0,0,205,207,1,0,0,0,206,
        200,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,
        211,1,0,0,0,210,208,1,0,0,0,211,213,3,2,1,0,212,214,5,62,0,0,213,
        212,1,0,0,0,213,214,1,0,0,0,214,215,1,0,0,0,215,216,5,2,0,0,216,
        19,1,0,0,0,217,218,3,26,13,0,218,227,5,53,0,0,219,224,3,28,14,0,
        220,221,5,60,0,0,221,223,3,28,14,0,222,220,1,0,0,0,223,226,1,0,0,
        0,224,222,1,0,0,0,224,225,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,
        0,227,219,1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,230,5,54,0,
        0,230,21,1,0,0,0,231,232,5,29,0,0,232,233,3,26,13,0,233,234,5,53,
        0,0,234,239,3,26,13,0,235,236,5,60,0,0,236,238,3,26,13,0,237,235,
        1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,242,
        1,0,0,0,241,239,1,0,0,0,242,243,5,54,0,0,243,244,5,61,0,0,244,245,
        5,1,0,0,245,246,3,2,1,0,246,247,5,2,0,0,247,23,1,0,0,0,248,249,3,
        26,13,0,249,250,5,28,0,0,250,251,3,28,14,0,251,25,1,0,0,0,252,257,
        5,3,0,0,253,254,5,59,0,0,254,256,5,3,0,0,255,253,1,0,0,0,256,259,
        1,0,0,0,257,255,1,0,0,0,257,258,1,0,0,0,258,27,1,0,0,0,259,257,1,
        0,0,0,260,261,6,14,-1,0,261,262,5,53,0,0,262,263,3,28,14,0,263,264,
        5,54,0,0,264,278,1,0,0,0,265,266,3,32,16,0,266,267,3,28,14,10,267,
        278,1,0,0,0,268,278,3,26,13,0,269,278,3,20,10,0,270,278,5,5,0,0,
        271,278,5,4,0,0,272,278,5,6,0,0,273,278,5,7,0,0,274,278,5,47,0,0,
        275,278,5,48,0,0,276,278,5,8,0,0,277,260,1,0,0,0,277,265,1,0,0,0,
        277,268,1,0,0,0,277,269,1,0,0,0,277,270,1,0,0,0,277,271,1,0,0,0,
        277,272,1,0,0,0,277,273,1,0,0,0,277,274,1,0,0,0,277,275,1,0,0,0,
        277,276,1,0,0,0,278,285,1,0,0,0,279,280,10,11,0,0,280,281,3,30,15,
        0,281,282,3,28,14,12,282,284,1,0,0,0,283,279,1,0,0,0,284,287,1,0,
        0,0,285,283,1,0,0,0,285,286,1,0,0,0,286,29,1,0,0,0,287,285,1,0,0,
        0,288,289,7,0,0,0,289,31,1,0,0,0,290,291,7,1,0,0,291,33,1,0,0,0,
        33,36,42,47,57,67,73,78,84,88,96,102,107,116,122,127,139,145,150,
        160,166,171,180,186,191,202,208,213,224,227,239,257,277,285
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
    RULE_complex_sentence = 2
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
    RULE_unitary_operator = 16

    ruleNames =  [ "start", "sentence", "complex_sentence", "if", "elif", 
                   "else", "for", "while", "try", "except", "function_execution", 
                   "function_declaration", "assign", "identifier", "expression", 
                   "binary_operator", "unitary_operator" ]

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
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.sentence()

                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 35
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 38
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 45
            self.sentence()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 46
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 49
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
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.if_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.for_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 53
                self.while_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.try_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.function_execution()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Complex_sentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Function_declarationContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_complex_sentence

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComplex_sentence" ):
                return visitor.visitComplex_sentence(self)
            else:
                return visitor.visitChildren(self)




    def complex_sentence(self):

        localctx = QuantumLanguageParser.Complex_sentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_complex_sentence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.function_declaration()
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
        self.enterRule(localctx, 6, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(QuantumLanguageParser.IF)
            self.state = 62
            self.expression(0)
            self.state = 63
            self.match(QuantumLanguageParser.COLON)
            self.state = 64
            self.match(QuantumLanguageParser.INDENT)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 65
                    self.sentence()

                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 66
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 69
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 76
            self.sentence()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 77
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 80
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 81
                self.elif_()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 87
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
        self.enterRule(localctx, 8, self.RULE_elif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(QuantumLanguageParser.ELIF)
            self.state = 91
            self.expression(0)
            self.state = 92
            self.match(QuantumLanguageParser.COLON)
            self.state = 93
            self.match(QuantumLanguageParser.INDENT)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    self.sentence()

                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 95
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 98
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 105
            self.sentence()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 106
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 109
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
        self.enterRule(localctx, 10, self.RULE_else)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(QuantumLanguageParser.ELSE)
            self.state = 112
            self.match(QuantumLanguageParser.COLON)
            self.state = 113
            self.match(QuantumLanguageParser.INDENT)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 114
                    self.sentence()

                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 115
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 118
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 125
            self.sentence()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 126
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 129
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
        self.enterRule(localctx, 12, self.RULE_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(QuantumLanguageParser.FOR)
            self.state = 132
            self.identifier()
            self.state = 133
            self.match(QuantumLanguageParser.IN)
            self.state = 134
            self.expression(0)
            self.state = 135
            self.match(QuantumLanguageParser.COLON)
            self.state = 136
            self.match(QuantumLanguageParser.INDENT)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(QuantumLanguageParser.WHILE)
            self.state = 155
            self.expression(0)
            self.state = 156
            self.match(QuantumLanguageParser.COLON)
            self.state = 157
            self.match(QuantumLanguageParser.INDENT)
            self.state = 166
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 158
                    self.sentence()

                    self.state = 160
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 159
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 162
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 168
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 169
            self.sentence()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 170
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 173
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
        self.enterRule(localctx, 16, self.RULE_try)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(QuantumLanguageParser.TRY)
            self.state = 176
            self.match(QuantumLanguageParser.COLON)
            self.state = 177
            self.match(QuantumLanguageParser.INDENT)
            self.state = 186
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 178
                    self.sentence()

                    self.state = 180
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 179
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 182
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 188
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 189
            self.sentence()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 190
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 193
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 194
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
            self.state = 196
            self.match(QuantumLanguageParser.EXCEPT)
            self.state = 197
            self.expression(0)
            self.state = 198
            self.match(QuantumLanguageParser.COLON)
            self.state = 199
            self.match(QuantumLanguageParser.INDENT)
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 200
                    self.sentence()

                    self.state = 202
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 201
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 204
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

            self.state = 211
            self.sentence()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 212
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 215
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
            self.state = 217
            self.identifier()
            self.state = 218
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 9447003905853432) != 0:
                self.state = 219
                self.expression(0)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==60:
                    self.state = 220
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 221
                    self.expression(0)
                    self.state = 226
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 229
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
            self.state = 231
            self.match(QuantumLanguageParser.DEF)
            self.state = 232
            self.identifier()
            self.state = 233
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 234
            self.identifier()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==60:
                self.state = 235
                self.match(QuantumLanguageParser.COMMA)
                self.state = 236
                self.identifier()
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            self.match(QuantumLanguageParser.CLOSE_PAREN)
            self.state = 243
            self.match(QuantumLanguageParser.COLON)
            self.state = 244
            self.match(QuantumLanguageParser.INDENT)
            self.state = 245
            self.sentence()
            self.state = 246
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
            self.state = 248
            self.identifier()
            self.state = 249
            self.match(QuantumLanguageParser.ASSIGN)
            self.state = 250
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
        self.enterRule(localctx, 26, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(QuantumLanguageParser.IDENTIFIER)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 253
                    self.match(QuantumLanguageParser.DOT)
                    self.state = 254
                    self.match(QuantumLanguageParser.IDENTIFIER) 
                self.state = 259
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 261
                self.match(QuantumLanguageParser.OPEN_PAREN)
                self.state = 262
                self.expression(0)
                self.state = 263
                self.match(QuantumLanguageParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 265
                self.unitary_operator()
                self.state = 266
                self.expression(10)
                pass

            elif la_ == 3:
                self.state = 268
                self.identifier()
                pass

            elif la_ == 4:
                self.state = 269
                self.function_execution()
                pass

            elif la_ == 5:
                self.state = 270
                self.match(QuantumLanguageParser.INTEGER_LITERAL)
                pass

            elif la_ == 6:
                self.state = 271
                self.match(QuantumLanguageParser.STRING_LITERAL)
                pass

            elif la_ == 7:
                self.state = 272
                self.match(QuantumLanguageParser.IMAGINARY_LITERAL)
                pass

            elif la_ == 8:
                self.state = 273
                self.match(QuantumLanguageParser.FLOAT_LITERAL)
                pass

            elif la_ == 9:
                self.state = 274
                self.match(QuantumLanguageParser.TRUE)
                pass

            elif la_ == 10:
                self.state = 275
                self.match(QuantumLanguageParser.FALSE)
                pass

            elif la_ == 11:
                self.state = 276
                self.match(QuantumLanguageParser.QUBIT_STATE_LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = QuantumLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 279
                    if not self.precpred(self._ctx, 11):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                    self.state = 280
                    self.binary_operator()
                    self.state = 281
                    self.expression(12) 
                self.state = 287
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
        self.enterRule(localctx, 30, self.RULE_binary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
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
        self.enterRule(localctx, 32, self.RULE_unitary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
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
        self._predicates[14] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         




