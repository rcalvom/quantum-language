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
        4,1,64,36,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,3,0,11,8,0,1,0,
        1,0,5,0,15,8,0,10,0,12,0,18,9,0,1,0,1,0,3,0,22,8,0,1,0,1,0,1,1,1,
        1,3,1,28,8,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,35,0,
        16,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,31,1,0,0,0,8,10,3,2,1,0,9,
        11,5,62,0,0,10,9,1,0,0,0,10,11,1,0,0,0,11,12,1,0,0,0,12,13,5,63,
        0,0,13,15,1,0,0,0,14,8,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,16,17,
        1,0,0,0,17,19,1,0,0,0,18,16,1,0,0,0,19,21,3,2,1,0,20,22,5,62,0,0,
        21,20,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,
        0,0,25,28,3,6,3,0,26,28,3,4,2,0,27,25,1,0,0,0,27,26,1,0,0,0,28,3,
        1,0,0,0,29,30,5,33,0,0,30,5,1,0,0,0,31,32,5,3,0,0,32,33,5,28,0,0,
        33,34,5,5,0,0,34,7,1,0,0,0,4,10,16,21,27
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
    RULE_assign = 3

    ruleNames =  [ "start", "sentence", "if", "assign" ]

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
            self.state = 16
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 8
                    self.sentence()

                    self.state = 10
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==62:
                        self.state = 9
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 12
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 18
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 19
            self.sentence()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 20
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 23
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

        def assign(self):
            return self.getTypedRuleContext(QuantumLanguageParser.AssignContext,0)


        def if_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IfContext,0)


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
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.assign()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.if_()
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(QuantumLanguageParser.IF)
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

        def IDENTIFIER(self):
            return self.getToken(QuantumLanguageParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(QuantumLanguageParser.ASSIGN, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(QuantumLanguageParser.INTEGER_LITERAL, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = QuantumLanguageParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(QuantumLanguageParser.IDENTIFIER)
            self.state = 32
            self.match(QuantumLanguageParser.ASSIGN)
            self.state = 33
            self.match(QuantumLanguageParser.INTEGER_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





