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
        4,1,68,309,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        57,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,65,8,2,1,2,1,2,5,2,69,8,2,10,
        2,12,2,72,9,2,1,2,1,2,3,2,76,8,2,1,2,1,2,5,2,80,8,2,10,2,12,2,83,
        9,2,1,2,3,2,86,8,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,94,8,3,1,3,1,3,5,
        3,98,8,3,10,3,12,3,101,9,3,1,3,1,3,3,3,105,8,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,3,4,114,8,4,1,4,1,4,5,4,118,8,4,10,4,12,4,121,9,4,1,4,
        1,4,3,4,125,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,137,
        8,5,1,5,1,5,5,5,141,8,5,10,5,12,5,144,9,5,1,5,1,5,3,5,148,8,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,158,8,6,1,6,1,6,5,6,162,8,6,10,
        6,12,6,165,9,6,1,6,1,6,3,6,169,8,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,
        7,178,8,7,1,7,1,7,5,7,182,8,7,10,7,12,7,185,9,7,1,7,1,7,3,7,189,
        8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,200,8,8,1,8,1,8,5,8,
        204,8,8,10,8,12,8,207,9,8,1,8,1,8,3,8,211,8,8,1,8,1,8,1,9,1,9,1,
        9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,5,14,237,8,14,10,14,12,14,240,9,14,
        3,14,242,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,5,15,252,8,
        15,10,15,12,15,255,9,15,3,15,257,8,15,1,15,1,15,1,15,1,15,1,15,1,
        15,1,16,1,16,1,16,1,16,1,17,1,17,1,17,5,17,272,8,17,10,17,12,17,
        275,9,17,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,18,1,18,3,18,294,8,18,1,18,1,18,1,18,1,18,
        5,18,300,8,18,10,18,12,18,303,9,18,1,19,1,19,1,20,1,20,1,20,0,1,
        36,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        0,2,2,0,1,7,13,19,2,0,1,2,36,36,337,0,42,1,0,0,0,2,56,1,0,0,0,4,
        58,1,0,0,0,6,87,1,0,0,0,8,108,1,0,0,0,10,128,1,0,0,0,12,151,1,0,
        0,0,14,172,1,0,0,0,16,193,1,0,0,0,18,214,1,0,0,0,20,218,1,0,0,0,
        22,222,1,0,0,0,24,225,1,0,0,0,26,228,1,0,0,0,28,231,1,0,0,0,30,245,
        1,0,0,0,32,264,1,0,0,0,34,268,1,0,0,0,36,293,1,0,0,0,38,304,1,0,
        0,0,40,306,1,0,0,0,42,43,3,2,1,0,43,1,1,0,0,0,44,57,3,4,2,0,45,57,
        3,10,5,0,46,57,3,12,6,0,47,57,3,14,7,0,48,57,3,18,9,0,49,57,3,20,
        10,0,50,57,3,22,11,0,51,57,3,24,12,0,52,57,3,26,13,0,53,57,3,28,
        14,0,54,57,3,32,16,0,55,57,3,30,15,0,56,44,1,0,0,0,56,45,1,0,0,0,
        56,46,1,0,0,0,56,47,1,0,0,0,56,48,1,0,0,0,56,49,1,0,0,0,56,50,1,
        0,0,0,56,51,1,0,0,0,56,52,1,0,0,0,56,53,1,0,0,0,56,54,1,0,0,0,56,
        55,1,0,0,0,57,3,1,0,0,0,58,59,5,25,0,0,59,60,3,36,18,0,60,61,5,56,
        0,0,61,70,5,59,0,0,62,64,3,2,1,0,63,65,5,57,0,0,64,63,1,0,0,0,64,
        65,1,0,0,0,65,66,1,0,0,0,66,67,5,58,0,0,67,69,1,0,0,0,68,62,1,0,
        0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,
        1,0,0,0,73,75,3,2,1,0,74,76,5,57,0,0,75,74,1,0,0,0,75,76,1,0,0,0,
        76,77,1,0,0,0,77,81,5,60,0,0,78,80,3,6,3,0,79,78,1,0,0,0,80,83,1,
        0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,84,
        86,3,8,4,0,85,84,1,0,0,0,85,86,1,0,0,0,86,5,1,0,0,0,87,88,5,26,0,
        0,88,89,3,36,18,0,89,90,5,56,0,0,90,99,5,59,0,0,91,93,3,2,1,0,92,
        94,5,57,0,0,93,92,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,58,
        0,0,96,98,1,0,0,0,97,91,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,
        100,1,0,0,0,100,102,1,0,0,0,101,99,1,0,0,0,102,104,3,2,1,0,103,105,
        5,57,0,0,104,103,1,0,0,0,104,105,1,0,0,0,105,106,1,0,0,0,106,107,
        5,60,0,0,107,7,1,0,0,0,108,109,5,27,0,0,109,110,5,56,0,0,110,119,
        5,59,0,0,111,113,3,2,1,0,112,114,5,57,0,0,113,112,1,0,0,0,113,114,
        1,0,0,0,114,115,1,0,0,0,115,116,5,58,0,0,116,118,1,0,0,0,117,111,
        1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,122,
        1,0,0,0,121,119,1,0,0,0,122,124,3,2,1,0,123,125,5,57,0,0,124,123,
        1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,127,5,60,0,0,127,9,1,
        0,0,0,128,129,5,29,0,0,129,130,3,34,17,0,130,131,5,30,0,0,131,132,
        3,36,18,0,132,133,5,56,0,0,133,142,5,59,0,0,134,136,3,2,1,0,135,
        137,5,57,0,0,136,135,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,138,
        139,5,58,0,0,139,141,1,0,0,0,140,134,1,0,0,0,141,144,1,0,0,0,142,
        140,1,0,0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,142,1,0,0,0,145,
        147,3,2,1,0,146,148,5,57,0,0,147,146,1,0,0,0,147,148,1,0,0,0,148,
        149,1,0,0,0,149,150,5,60,0,0,150,11,1,0,0,0,151,152,5,28,0,0,152,
        153,3,36,18,0,153,154,5,56,0,0,154,163,5,59,0,0,155,157,3,2,1,0,
        156,158,5,57,0,0,157,156,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,
        159,160,5,58,0,0,160,162,1,0,0,0,161,155,1,0,0,0,162,165,1,0,0,0,
        163,161,1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,163,1,0,0,0,
        166,168,3,2,1,0,167,169,5,57,0,0,168,167,1,0,0,0,168,169,1,0,0,0,
        169,170,1,0,0,0,170,171,5,60,0,0,171,13,1,0,0,0,172,173,5,31,0,0,
        173,174,5,56,0,0,174,183,5,59,0,0,175,177,3,2,1,0,176,178,5,57,0,
        0,177,176,1,0,0,0,177,178,1,0,0,0,178,179,1,0,0,0,179,180,5,58,0,
        0,180,182,1,0,0,0,181,175,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,
        0,183,184,1,0,0,0,184,186,1,0,0,0,185,183,1,0,0,0,186,188,3,2,1,
        0,187,189,5,57,0,0,188,187,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,
        0,190,191,5,60,0,0,191,192,3,16,8,0,192,15,1,0,0,0,193,194,5,33,
        0,0,194,195,3,36,18,0,195,196,5,56,0,0,196,205,5,59,0,0,197,199,
        3,2,1,0,198,200,5,57,0,0,199,198,1,0,0,0,199,200,1,0,0,0,200,201,
        1,0,0,0,201,202,5,58,0,0,202,204,1,0,0,0,203,197,1,0,0,0,204,207,
        1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,208,1,0,0,0,207,205,
        1,0,0,0,208,210,3,2,1,0,209,211,5,57,0,0,210,209,1,0,0,0,210,211,
        1,0,0,0,211,212,1,0,0,0,212,213,5,60,0,0,213,17,1,0,0,0,214,215,
        5,45,0,0,215,216,3,34,17,0,216,217,3,34,17,0,217,19,1,0,0,0,218,
        219,5,46,0,0,219,220,3,34,17,0,220,221,3,34,17,0,221,21,1,0,0,0,
        222,223,5,47,0,0,223,224,3,34,17,0,224,23,1,0,0,0,225,226,5,48,0,
        0,226,227,3,34,17,0,227,25,1,0,0,0,228,229,5,49,0,0,229,230,3,34,
        17,0,230,27,1,0,0,0,231,232,3,34,17,0,232,241,5,50,0,0,233,238,3,
        36,18,0,234,235,5,55,0,0,235,237,3,36,18,0,236,234,1,0,0,0,237,240,
        1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,242,1,0,0,0,240,238,
        1,0,0,0,241,233,1,0,0,0,241,242,1,0,0,0,242,243,1,0,0,0,243,244,
        5,51,0,0,244,29,1,0,0,0,245,246,5,21,0,0,246,247,3,34,17,0,247,256,
        5,50,0,0,248,253,3,34,17,0,249,250,5,55,0,0,250,252,3,34,17,0,251,
        249,1,0,0,0,252,255,1,0,0,0,253,251,1,0,0,0,253,254,1,0,0,0,254,
        257,1,0,0,0,255,253,1,0,0,0,256,248,1,0,0,0,256,257,1,0,0,0,257,
        258,1,0,0,0,258,259,5,51,0,0,259,260,5,56,0,0,260,261,5,59,0,0,261,
        262,3,2,1,0,262,263,5,60,0,0,263,31,1,0,0,0,264,265,3,34,17,0,265,
        266,5,20,0,0,266,267,3,36,18,0,267,33,1,0,0,0,268,273,5,61,0,0,269,
        270,5,54,0,0,270,272,5,61,0,0,271,269,1,0,0,0,272,275,1,0,0,0,273,
        271,1,0,0,0,273,274,1,0,0,0,274,35,1,0,0,0,275,273,1,0,0,0,276,277,
        6,18,-1,0,277,278,5,50,0,0,278,279,3,36,18,0,279,280,5,51,0,0,280,
        294,1,0,0,0,281,282,3,40,20,0,282,283,3,36,18,10,283,294,1,0,0,0,
        284,294,3,34,17,0,285,294,3,28,14,0,286,294,5,63,0,0,287,294,5,62,
        0,0,288,294,5,64,0,0,289,294,5,65,0,0,290,294,5,39,0,0,291,294,5,
        40,0,0,292,294,5,66,0,0,293,276,1,0,0,0,293,281,1,0,0,0,293,284,
        1,0,0,0,293,285,1,0,0,0,293,286,1,0,0,0,293,287,1,0,0,0,293,288,
        1,0,0,0,293,289,1,0,0,0,293,290,1,0,0,0,293,291,1,0,0,0,293,292,
        1,0,0,0,294,301,1,0,0,0,295,296,10,11,0,0,296,297,3,38,19,0,297,
        298,3,36,18,12,298,300,1,0,0,0,299,295,1,0,0,0,300,303,1,0,0,0,301,
        299,1,0,0,0,301,302,1,0,0,0,302,37,1,0,0,0,303,301,1,0,0,0,304,305,
        7,0,0,0,305,39,1,0,0,0,306,307,7,1,0,0,307,41,1,0,0,0,31,56,64,70,
        75,81,85,93,99,104,113,119,124,136,142,147,157,163,168,177,183,188,
        199,205,210,238,241,253,256,273,293,301
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
                     "'continue'", "'break'", "'matmul'", "'kron'", "'herm'", 
                     "'conjugate'", "'transpose'", "'('", "')'", "'['", 
                     "']'", "'.'", "','", "':'", "';'", "'\\n'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "ADD", "MINUS", "STAR", "DIV", "IDIV", 
                      "MOD", "POWER", "OR_OP", "XOR", "AND_OP", "LEFT_SHIFT", 
                      "RIGHT_SHIFT", "LESS_THAN", "GREATER_THAN", "EQUALS", 
                      "GT_EQ", "LT_EQ", "NOT_EQ_1", "NOT_EQ_2", "ASSIGN", 
                      "DEF", "RETURN", "RAISE", "ASSERT", "IF", "ELIF", 
                      "ELSE", "WHILE", "FOR", "IN", "TRY", "FINALLY", "EXCEPT", 
                      "OR", "AND", "NOT", "IS", "NONE", "TRUE", "FALSE", 
                      "CLASS", "PASS", "CONTINUE", "BREAK", "MATMUL", "KRONECKER", 
                      "HERMITIAN", "CONJUGATE", "TRANSPOSE", "OPEN_PAREN", 
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
    RULE_matmul = 9
    RULE_kronecker = 10
    RULE_hermitian = 11
    RULE_conjugate = 12
    RULE_transpose = 13
    RULE_function_execution = 14
    RULE_function_declaration = 15
    RULE_assign = 16
    RULE_identifier = 17
    RULE_expression = 18
    RULE_binary_operator = 19
    RULE_unitary_operator = 20

    ruleNames =  [ "start", "sentence", "if", "elif", "else", "for", "while", 
                   "try", "except", "matmul", "kronecker", "hermitian", 
                   "conjugate", "transpose", "function_execution", "function_declaration", 
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
    MATMUL=45
    KRONECKER=46
    HERMITIAN=47
    CONJUGATE=48
    TRANSPOSE=49
    OPEN_PAREN=50
    CLOSE_PAREN=51
    OPEN_BRACK=52
    CLOSE_BRACK=53
    DOT=54
    COMMA=55
    COLON=56
    SEMI_COLON=57
    NEWLINE=58
    INDENT=59
    DEDENT=60
    IDENTIFIER=61
    STRING_LITERAL=62
    INTEGER_LITERAL=63
    IMAGINARY_LITERAL=64
    FLOAT_LITERAL=65
    QUBIT_STATE_LITERAL=66
    SPACES=67
    COMMENTS=68

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
            self.state = 42
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


        def matmul(self):
            return self.getTypedRuleContext(QuantumLanguageParser.MatmulContext,0)


        def kronecker(self):
            return self.getTypedRuleContext(QuantumLanguageParser.KroneckerContext,0)


        def hermitian(self):
            return self.getTypedRuleContext(QuantumLanguageParser.HermitianContext,0)


        def conjugate(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ConjugateContext,0)


        def transpose(self):
            return self.getTypedRuleContext(QuantumLanguageParser.TransposeContext,0)


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
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.if_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.for_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.while_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.try_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.matmul()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.kronecker()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 50
                self.hermitian()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 51
                self.conjugate()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 52
                self.transpose()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 53
                self.function_execution()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 54
                self.assign()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 55
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
            self.state = 58
            self.match(QuantumLanguageParser.IF)
            self.state = 59
            self.expression(0)
            self.state = 60
            self.match(QuantumLanguageParser.COLON)
            self.state = 61
            self.match(QuantumLanguageParser.INDENT)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 62
                    self.sentence()

                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==57:
                        self.state = 63
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 66
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 73
            self.sentence()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 74
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 77
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 78
                self.elif_()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 84
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
            self.state = 87
            self.match(QuantumLanguageParser.ELIF)
            self.state = 88
            self.expression(0)
            self.state = 89
            self.match(QuantumLanguageParser.COLON)
            self.state = 90
            self.match(QuantumLanguageParser.INDENT)
            self.state = 99
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    self.sentence()

                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==57:
                        self.state = 92
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 95
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 101
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 102
            self.sentence()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
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
            self.state = 108
            self.match(QuantumLanguageParser.ELSE)
            self.state = 109
            self.match(QuantumLanguageParser.COLON)
            self.state = 110
            self.match(QuantumLanguageParser.INDENT)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 111
                    self.sentence()

                    self.state = 113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==57:
                        self.state = 112
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 115
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 122
            self.sentence()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 123
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 126
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
            self.state = 128
            self.match(QuantumLanguageParser.FOR)
            self.state = 129
            self.identifier()
            self.state = 130
            self.match(QuantumLanguageParser.IN)
            self.state = 131
            self.expression(0)
            self.state = 132
            self.match(QuantumLanguageParser.COLON)
            self.state = 133
            self.match(QuantumLanguageParser.INDENT)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 134
                    self.sentence()

                    self.state = 136
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==57:
                        self.state = 135
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 138
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 145
            self.sentence()
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 146
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 149
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
            self.state = 151
            self.match(QuantumLanguageParser.WHILE)
            self.state = 152
            self.expression(0)
            self.state = 153
            self.match(QuantumLanguageParser.COLON)
            self.state = 154
            self.match(QuantumLanguageParser.INDENT)
            self.state = 163
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 155
                    self.sentence()

                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==57:
                        self.state = 156
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 159
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 165
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 166
            self.sentence()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 167
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 170
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
            self.state = 172
            self.match(QuantumLanguageParser.TRY)
            self.state = 173
            self.match(QuantumLanguageParser.COLON)
            self.state = 174
            self.match(QuantumLanguageParser.INDENT)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 175
                    self.sentence()

                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==57:
                        self.state = 176
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 179
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 186
            self.sentence()
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 187
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 190
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 191
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
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 197
                    self.sentence()

                    self.state = 199
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==57:
                        self.state = 198
                        self.match(QuantumLanguageParser.SEMI_COLON)


                    self.state = 201
                    self.match(QuantumLanguageParser.NEWLINE) 
                self.state = 207
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 208
            self.sentence()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
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


    class MatmulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MATMUL(self):
            return self.getToken(QuantumLanguageParser.MATMUL, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,i)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_matmul

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatmul" ):
                return visitor.visitMatmul(self)
            else:
                return visitor.visitChildren(self)




    def matmul(self):

        localctx = QuantumLanguageParser.MatmulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_matmul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(QuantumLanguageParser.MATMUL)
            self.state = 215
            self.identifier()
            self.state = 216
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KroneckerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KRONECKER(self):
            return self.getToken(QuantumLanguageParser.KRONECKER, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,i)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_kronecker

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKronecker" ):
                return visitor.visitKronecker(self)
            else:
                return visitor.visitChildren(self)




    def kronecker(self):

        localctx = QuantumLanguageParser.KroneckerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_kronecker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(QuantumLanguageParser.KRONECKER)
            self.state = 219
            self.identifier()
            self.state = 220
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HermitianContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HERMITIAN(self):
            return self.getToken(QuantumLanguageParser.HERMITIAN, 0)

        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_hermitian

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHermitian" ):
                return visitor.visitHermitian(self)
            else:
                return visitor.visitChildren(self)




    def hermitian(self):

        localctx = QuantumLanguageParser.HermitianContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_hermitian)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(QuantumLanguageParser.HERMITIAN)
            self.state = 223
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConjugateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONJUGATE(self):
            return self.getToken(QuantumLanguageParser.CONJUGATE, 0)

        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_conjugate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConjugate" ):
                return visitor.visitConjugate(self)
            else:
                return visitor.visitChildren(self)




    def conjugate(self):

        localctx = QuantumLanguageParser.ConjugateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_conjugate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(QuantumLanguageParser.CONJUGATE)
            self.state = 226
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransposeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANSPOSE(self):
            return self.getToken(QuantumLanguageParser.TRANSPOSE, 0)

        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_transpose

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTranspose" ):
                return visitor.visitTranspose(self)
            else:
                return visitor.visitChildren(self)




    def transpose(self):

        localctx = QuantumLanguageParser.TransposeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_transpose)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(QuantumLanguageParser.TRANSPOSE)
            self.state = 229
            self.identifier()
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
        self.enterRule(localctx, 28, self.RULE_function_execution)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.identifier()
            self.state = 232
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & -2304715391319932922) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 7) != 0:
                self.state = 233
                self.expression(0)
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 234
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 235
                    self.expression(0)
                    self.state = 240
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 243
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
        self.enterRule(localctx, 30, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(QuantumLanguageParser.DEF)
            self.state = 246
            self.identifier()
            self.state = 247
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==61:
                self.state = 248
                self.identifier()
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==55:
                    self.state = 249
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 250
                    self.identifier()
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 258
            self.match(QuantumLanguageParser.CLOSE_PAREN)
            self.state = 259
            self.match(QuantumLanguageParser.COLON)
            self.state = 260
            self.match(QuantumLanguageParser.INDENT)
            self.state = 261
            self.sentence()
            self.state = 262
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
        self.enterRule(localctx, 32, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.identifier()
            self.state = 265
            self.match(QuantumLanguageParser.ASSIGN)
            self.state = 266
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
        self.enterRule(localctx, 34, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(QuantumLanguageParser.IDENTIFIER)
            self.state = 273
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 269
                    self.match(QuantumLanguageParser.DOT)
                    self.state = 270
                    self.match(QuantumLanguageParser.IDENTIFIER) 
                self.state = 275
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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 277
                self.match(QuantumLanguageParser.OPEN_PAREN)
                self.state = 278
                self.expression(0)
                self.state = 279
                self.match(QuantumLanguageParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 281
                self.unitary_operator()
                self.state = 282
                self.expression(10)
                pass

            elif la_ == 3:
                self.state = 284
                self.identifier()
                pass

            elif la_ == 4:
                self.state = 285
                self.function_execution()
                pass

            elif la_ == 5:
                self.state = 286
                self.match(QuantumLanguageParser.INTEGER_LITERAL)
                pass

            elif la_ == 6:
                self.state = 287
                self.match(QuantumLanguageParser.STRING_LITERAL)
                pass

            elif la_ == 7:
                self.state = 288
                self.match(QuantumLanguageParser.IMAGINARY_LITERAL)
                pass

            elif la_ == 8:
                self.state = 289
                self.match(QuantumLanguageParser.FLOAT_LITERAL)
                pass

            elif la_ == 9:
                self.state = 290
                self.match(QuantumLanguageParser.TRUE)
                pass

            elif la_ == 10:
                self.state = 291
                self.match(QuantumLanguageParser.FALSE)
                pass

            elif la_ == 11:
                self.state = 292
                self.match(QuantumLanguageParser.QUBIT_STATE_LITERAL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = QuantumLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 295
                    if not self.precpred(self._ctx, 11):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                    self.state = 296
                    self.binary_operator()
                    self.state = 297
                    self.expression(12) 
                self.state = 303
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
        self.enterRule(localctx, 38, self.RULE_binary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
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
        self.enterRule(localctx, 40, self.RULE_unitary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
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
        self._predicates[18] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         




