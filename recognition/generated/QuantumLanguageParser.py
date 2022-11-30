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
        4,1,63,277,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,42,8,
        1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,2,1,2,5,2,54,8,2,10,2,12,
        2,57,9,2,1,2,1,2,3,2,61,8,2,1,2,1,2,5,2,65,8,2,10,2,12,2,68,9,2,
        1,2,3,2,71,8,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,79,8,3,1,3,1,3,5,3,83,
        8,3,10,3,12,3,86,9,3,1,3,1,3,3,3,90,8,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,3,4,99,8,4,1,4,1,4,5,4,103,8,4,10,4,12,4,106,9,4,1,4,1,4,3,4,
        110,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,122,8,5,1,5,
        1,5,5,5,126,8,5,10,5,12,5,129,9,5,1,5,1,5,3,5,133,8,5,1,5,1,5,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,143,8,6,1,6,1,6,5,6,147,8,6,10,6,12,6,
        150,9,6,1,6,1,6,3,6,154,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,163,
        8,7,1,7,1,7,5,7,167,8,7,10,7,12,7,170,9,7,1,7,1,7,3,7,174,8,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,185,8,8,1,8,1,8,5,8,189,8,
        8,10,8,12,8,192,9,8,1,8,1,8,3,8,196,8,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,5,9,205,8,9,10,9,12,9,208,9,9,3,9,210,8,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,220,8,10,10,10,12,10,223,9,10,3,10,225,
        8,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,5,12,240,8,12,10,12,12,12,243,9,12,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        262,8,13,1,13,1,13,1,13,1,13,5,13,268,8,13,10,13,12,13,271,9,13,
        1,14,1,14,1,15,1,15,1,15,0,1,26,16,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,0,2,2,0,1,7,13,19,2,0,1,2,36,36,305,0,32,1,0,0,0,2,41,
        1,0,0,0,4,43,1,0,0,0,6,72,1,0,0,0,8,93,1,0,0,0,10,113,1,0,0,0,12,
        136,1,0,0,0,14,157,1,0,0,0,16,178,1,0,0,0,18,199,1,0,0,0,20,213,
        1,0,0,0,22,232,1,0,0,0,24,236,1,0,0,0,26,261,1,0,0,0,28,272,1,0,
        0,0,30,274,1,0,0,0,32,33,3,2,1,0,33,1,1,0,0,0,34,42,3,4,2,0,35,42,
        3,10,5,0,36,42,3,12,6,0,37,42,3,14,7,0,38,42,3,18,9,0,39,42,3,22,
        11,0,40,42,3,20,10,0,41,34,1,0,0,0,41,35,1,0,0,0,41,36,1,0,0,0,41,
        37,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,1,0,0,0,42,3,1,0,0,
        0,43,44,5,25,0,0,44,45,3,26,13,0,45,46,5,51,0,0,46,55,5,54,0,0,47,
        49,3,2,1,0,48,50,5,52,0,0,49,48,1,0,0,0,49,50,1,0,0,0,50,51,1,0,
        0,0,51,52,5,53,0,0,52,54,1,0,0,0,53,47,1,0,0,0,54,57,1,0,0,0,55,
        53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,0,58,60,3,2,1,
        0,59,61,5,52,0,0,60,59,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,66,
        5,55,0,0,63,65,3,6,3,0,64,63,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,
        66,67,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,69,71,3,8,4,0,70,69,1,
        0,0,0,70,71,1,0,0,0,71,5,1,0,0,0,72,73,5,26,0,0,73,74,3,26,13,0,
        74,75,5,51,0,0,75,84,5,54,0,0,76,78,3,2,1,0,77,79,5,52,0,0,78,77,
        1,0,0,0,78,79,1,0,0,0,79,80,1,0,0,0,80,81,5,53,0,0,81,83,1,0,0,0,
        82,76,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,
        0,0,0,86,84,1,0,0,0,87,89,3,2,1,0,88,90,5,52,0,0,89,88,1,0,0,0,89,
        90,1,0,0,0,90,91,1,0,0,0,91,92,5,55,0,0,92,7,1,0,0,0,93,94,5,27,
        0,0,94,95,5,51,0,0,95,104,5,54,0,0,96,98,3,2,1,0,97,99,5,52,0,0,
        98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,53,0,0,101,
        103,1,0,0,0,102,96,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,
        1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,109,3,2,1,0,108,110,
        5,52,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,111,1,0,0,0,111,112,
        5,55,0,0,112,9,1,0,0,0,113,114,5,29,0,0,114,115,3,24,12,0,115,116,
        5,30,0,0,116,117,3,26,13,0,117,118,5,51,0,0,118,127,5,54,0,0,119,
        121,3,2,1,0,120,122,5,52,0,0,121,120,1,0,0,0,121,122,1,0,0,0,122,
        123,1,0,0,0,123,124,5,53,0,0,124,126,1,0,0,0,125,119,1,0,0,0,126,
        129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,
        127,1,0,0,0,130,132,3,2,1,0,131,133,5,52,0,0,132,131,1,0,0,0,132,
        133,1,0,0,0,133,134,1,0,0,0,134,135,5,55,0,0,135,11,1,0,0,0,136,
        137,5,28,0,0,137,138,3,26,13,0,138,139,5,51,0,0,139,148,5,54,0,0,
        140,142,3,2,1,0,141,143,5,52,0,0,142,141,1,0,0,0,142,143,1,0,0,0,
        143,144,1,0,0,0,144,145,5,53,0,0,145,147,1,0,0,0,146,140,1,0,0,0,
        147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,
        150,148,1,0,0,0,151,153,3,2,1,0,152,154,5,52,0,0,153,152,1,0,0,0,
        153,154,1,0,0,0,154,155,1,0,0,0,155,156,5,55,0,0,156,13,1,0,0,0,
        157,158,5,31,0,0,158,159,5,51,0,0,159,168,5,54,0,0,160,162,3,2,1,
        0,161,163,5,52,0,0,162,161,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,
        0,164,165,5,53,0,0,165,167,1,0,0,0,166,160,1,0,0,0,167,170,1,0,0,
        0,168,166,1,0,0,0,168,169,1,0,0,0,169,171,1,0,0,0,170,168,1,0,0,
        0,171,173,3,2,1,0,172,174,5,52,0,0,173,172,1,0,0,0,173,174,1,0,0,
        0,174,175,1,0,0,0,175,176,5,55,0,0,176,177,3,16,8,0,177,15,1,0,0,
        0,178,179,5,33,0,0,179,180,3,26,13,0,180,181,5,51,0,0,181,190,5,
        54,0,0,182,184,3,2,1,0,183,185,5,52,0,0,184,183,1,0,0,0,184,185,
        1,0,0,0,185,186,1,0,0,0,186,187,5,53,0,0,187,189,1,0,0,0,188,182,
        1,0,0,0,189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,193,
        1,0,0,0,192,190,1,0,0,0,193,195,3,2,1,0,194,196,5,52,0,0,195,194,
        1,0,0,0,195,196,1,0,0,0,196,197,1,0,0,0,197,198,5,55,0,0,198,17,
        1,0,0,0,199,200,3,24,12,0,200,209,5,45,0,0,201,206,3,26,13,0,202,
        203,5,50,0,0,203,205,3,26,13,0,204,202,1,0,0,0,205,208,1,0,0,0,206,
        204,1,0,0,0,206,207,1,0,0,0,207,210,1,0,0,0,208,206,1,0,0,0,209,
        201,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,5,46,0,0,212,
        19,1,0,0,0,213,214,5,21,0,0,214,215,3,24,12,0,215,224,5,45,0,0,216,
        221,3,24,12,0,217,218,5,50,0,0,218,220,3,24,12,0,219,217,1,0,0,0,
        220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,225,1,0,0,0,
        223,221,1,0,0,0,224,216,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,
        226,227,5,46,0,0,227,228,5,51,0,0,228,229,5,54,0,0,229,230,3,2,1,
        0,230,231,5,55,0,0,231,21,1,0,0,0,232,233,3,24,12,0,233,234,5,20,
        0,0,234,235,3,26,13,0,235,23,1,0,0,0,236,241,5,56,0,0,237,238,5,
        49,0,0,238,240,5,56,0,0,239,237,1,0,0,0,240,243,1,0,0,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,25,1,0,0,0,243,241,1,0,0,0,244,245,6,
        13,-1,0,245,246,5,45,0,0,246,247,3,26,13,0,247,248,5,46,0,0,248,
        262,1,0,0,0,249,250,3,30,15,0,250,251,3,26,13,10,251,262,1,0,0,0,
        252,262,3,24,12,0,253,262,3,18,9,0,254,262,5,58,0,0,255,262,5,57,
        0,0,256,262,5,59,0,0,257,262,5,60,0,0,258,262,5,39,0,0,259,262,5,
        40,0,0,260,262,5,61,0,0,261,244,1,0,0,0,261,249,1,0,0,0,261,252,
        1,0,0,0,261,253,1,0,0,0,261,254,1,0,0,0,261,255,1,0,0,0,261,256,
        1,0,0,0,261,257,1,0,0,0,261,258,1,0,0,0,261,259,1,0,0,0,261,260,
        1,0,0,0,262,269,1,0,0,0,263,264,10,11,0,0,264,265,3,28,14,0,265,
        266,3,26,13,12,266,268,1,0,0,0,267,263,1,0,0,0,268,271,1,0,0,0,269,
        267,1,0,0,0,269,270,1,0,0,0,270,27,1,0,0,0,271,269,1,0,0,0,272,273,
        7,0,0,0,273,29,1,0,0,0,274,275,7,1,0,0,275,31,1,0,0,0,31,41,49,55,
        60,66,70,78,84,89,98,104,109,121,127,132,142,148,153,162,168,173,
        184,190,195,206,209,221,224,241,261,269
    ]

class QuantumLanguageParser ( Parser ):

    grammarFileName = "QuantumLanguageParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'//'", "'%'", 
                     "'**'", "'|'", "'^'", "'&'", "'<<'", "'>>'", "'<'", 
                     "'>'", "'=='", "'>='", "'<='", "'<>'", "'!='", "'='", 
                     "'def'", "'return'", "'raise'", "'assert'", "'if'", 
                     "'elif'", "'else'", "'while'", "'for'", "'in'", "'try'", 
                     "'finally'", "'except'", "'or'", "'and'", "'not'", 
                     "'is'", "'None'", "'True'", "'False'", "'class'", "'pass'", 
                     "'continue'", "'break'", "'('", "')'", "'['", "']'", 
                     "'.'", "','", "':'", "';'", "'\\n'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ADD", "MINUS", "STAR", "DIV", "IDIV", 
                      "MOD", "POWER", "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", 
                      "RIGHT_SHIFT", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                      "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "ASSIGN", 
                      "DEF", "RETURN", "RAISE", "ASSERT", "IF", "ELIF", 
                      "ELSE", "WHILE", "FOR", "IN", "TRY", "FINALLY", "EXCEPT", 
                      "OR", "AND", "NOT", "IS", "NONE", "TRUE", "FALSE", 
                      "CLASS", "PASS", "CONTINUE", "BREAK", "OPEN_PAREN", 
                      "CLOSE_PAREN", "OPEN_BRACK", "CLOSE_BRACK", "DOT", 
                      "COMMA", "COLON", "SEMI_COLON", "NEWLINE", "INDENT", 
                      "DEDENT", "IDENTIFIER", "STRING_LITERAL", "INTEGER_LITERAL", 
                      "IMAGINARY_LITERAL", "FLOAT_LITERAL", "QUBIT_STATE_LITERAL", 
                      "SPACES", "COMMENTS" ]

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
    RULE_function_declaration = 10
    RULE_assign = 11
    RULE_identifier = 12
    RULE_expression = 13
    RULE_binary_operator = 14
    RULE_unitary_operator = 15

    ruleNames =  [ "start", "sentence", "if", "elif", "else", "for", "while", 
                   "try", "except", "function_execution", "function_declaration", 
                   "assign", "identifier", "expression", "binary_operator", 
                   "unitary_operator" ]

    EOF = Token.EOF
    ADD=1
    MINUS=2
    STAR=3
    DIV=4
    IDIV=5
    MOD=6
    POWER=7
    OR_OP=8
    XOR=9
    AND_OP=10
    LEFT_SHIFT=11
    RIGHT_SHIFT=12
    LESS_THAN=13
    GREATER_THAN=14
    EQUALS=15
    GT_EQ=16
    LT_EQ=17
    NOT_EQ_1=18
    NOT_EQ_2=19
    ASSIGN=20
    DEF=21
    RETURN=22
    RAISE=23
    ASSERT=24
    IF=25
    ELIF=26
    ELSE=27
    WHILE=28
    FOR=29
    IN=30
    TRY=31
    FINALLY=32
    EXCEPT=33
    OR=34
    AND=35
    NOT=36
    IS=37
    NONE=38
    TRUE=39
    FALSE=40
    CLASS=41
    PASS=42
    CONTINUE=43
    BREAK=44
    OPEN_PAREN=45
    CLOSE_PAREN=46
    OPEN_BRACK=47
    CLOSE_BRACK=48
    DOT=49
    COMMA=50
    COLON=51
    SEMI_COLON=52
    NEWLINE=53
    INDENT=54
    DEDENT=55
    IDENTIFIER=56
    STRING_LITERAL=57
    INTEGER_LITERAL=58
    IMAGINARY_LITERAL=59
    FLOAT_LITERAL=60
    QUBIT_STATE_LITERAL=61
    SPACES=62
    COMMENTS=63

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

        def sentence(self):
            return self.getTypedRuleContext(QuantumLanguageParser.SentenceContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.sentence()
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
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.if_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.for_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.while_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.try_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 38
                self.function_execution()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 39
                self.assign()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 40
                self.function_declaration()
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
            self.state = 43
            self.match(QuantumLanguageParser.IF)
            self.state = 44
            self.expression(0)
            self.state = 45
            self.match(QuantumLanguageParser.COLON)
            self.state = 46
            self.match(QuantumLanguageParser.INDENT)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 47
                    self.sentence()

                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 48
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 51
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 58
            self.sentence()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 59
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 62
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 63
                self.elif_()
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 69
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
            self.state = 72
            self.match(QuantumLanguageParser.ELIF)
            self.state = 73
            self.expression(0)
            self.state = 74
            self.match(QuantumLanguageParser.COLON)
            self.state = 75
            self.match(QuantumLanguageParser.INDENT)
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 76
                    self.sentence()

                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 77
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 80
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 87
            self.sentence()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 88
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 91
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
            self.state = 93
            self.match(QuantumLanguageParser.ELSE)
            self.state = 94
            self.match(QuantumLanguageParser.COLON)
            self.state = 95
            self.match(QuantumLanguageParser.INDENT)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 96
                    self.sentence()

                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 97
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 100
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 107
            self.sentence()
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 108
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 111
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
            self.state = 113
            self.match(QuantumLanguageParser.FOR)
            self.state = 114
            self.identifier()
            self.state = 115
            self.match(QuantumLanguageParser.IN)
            self.state = 116
            self.expression(0)
            self.state = 117
            self.match(QuantumLanguageParser.COLON)
            self.state = 118
            self.match(QuantumLanguageParser.INDENT)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 119
                    self.sentence()

                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 120
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 123
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 130
            self.sentence()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 131
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 134
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
            self.state = 136
            self.match(QuantumLanguageParser.WHILE)
            self.state = 137
            self.expression(0)
            self.state = 138
            self.match(QuantumLanguageParser.COLON)
            self.state = 139
            self.match(QuantumLanguageParser.INDENT)
            self.state = 148
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 140
                    self.sentence()

                    self.state = 142
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 141
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 144
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 150
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 151
            self.sentence()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 152
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 155
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
        self.enterRule(localctx, 14, self.RULE_try)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(QuantumLanguageParser.TRY)
            self.state = 158
            self.match(QuantumLanguageParser.COLON)
            self.state = 159
            self.match(QuantumLanguageParser.INDENT)
            self.state = 168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 160
                    self.sentence()

                    self.state = 162
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 161
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 164
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 171
            self.sentence()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 172
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 175
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 176
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
        self.enterRule(localctx, 16, self.RULE_except)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(QuantumLanguageParser.EXCEPT)
            self.state = 179
            self.expression(0)
            self.state = 180
            self.match(QuantumLanguageParser.COLON)
            self.state = 181
            self.match(QuantumLanguageParser.INDENT)
            self.state = 190
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 182
                    self.sentence()

                    self.state = 184
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==52:
                        self.state = 183
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 186
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 192
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 193
            self.sentence()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 194
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 197
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
            self.state = 199
            self.identifier()
            self.state = 200
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 4539665326748467206) != 0:
                self.state = 201
                self.expression(0)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 202
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 203
                    self.expression(0)
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 211
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
        self.enterRule(localctx, 20, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(QuantumLanguageParser.DEF)
            self.state = 214
            self.identifier()
            self.state = 215
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 216
                self.identifier()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 217
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 218
                    self.identifier()
                    self.state = 223
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 226
            self.match(QuantumLanguageParser.CLOSE_PAREN)
            self.state = 227
            self.match(QuantumLanguageParser.COLON)
            self.state = 228
            self.match(QuantumLanguageParser.INDENT)
            self.state = 229
            self.sentence()
            self.state = 230
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
        self.enterRule(localctx, 22, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.identifier()
            self.state = 233
            self.match(QuantumLanguageParser.ASSIGN)
            self.state = 234
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
        self.enterRule(localctx, 24, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(QuantumLanguageParser.IDENTIFIER)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 237
                    self.match(QuantumLanguageParser.DOT)
                    self.state = 238
                    self.match(QuantumLanguageParser.IDENTIFIER) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 245
                self.match(QuantumLanguageParser.OPEN_PAREN)
                self.state = 246
                self.expression(0)
                self.state = 247
                self.match(QuantumLanguageParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 249
                self.unitary_operator()
                self.state = 250
                self.expression(10)
                pass

            elif la_ == 3:
                self.state = 252
                self.identifier()
                pass

            elif la_ == 4:
                self.state = 253
                self.function_execution()
                pass

            elif la_ == 5:
                self.state = 254
                self.match(QuantumLanguageParser.INTEGER_LITERAL)
                pass

            elif la_ == 6:
                self.state = 255
                self.match(QuantumLanguageParser.STRING_LITERAL)
                pass

            elif la_ == 7:
                self.state = 256
                self.match(QuantumLanguageParser.IMAGINARY_LITERAL)
                pass

            elif la_ == 8:
                self.state = 257
                self.match(QuantumLanguageParser.FLOAT_LITERAL)
                pass

            elif la_ == 9:
                self.state = 258
                self.match(QuantumLanguageParser.TRUE)
                pass

            elif la_ == 10:
                self.state = 259
                self.match(QuantumLanguageParser.FALSE)
                pass

            elif la_ == 11:
                self.state = 260
                self.match(QuantumLanguageParser.QUBIT_STATE_LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = QuantumLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 263
                    if not self.precpred(self._ctx, 11):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                    self.state = 264
                    self.binary_operator()
                    self.state = 265
                    self.expression(12) 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_binary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1040638) != 0):
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
        self.enterRule(localctx, 30, self.RULE_unitary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 68719476742) != 0):
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
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         




