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
        4,1,69,327,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,4,0,62,8,0,11,0,12,0,63,1,0,1,
        0,1,1,1,1,1,1,5,1,71,8,1,10,1,12,1,74,9,1,1,1,3,1,77,8,1,1,1,1,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,93,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,4,3,101,8,3,11,3,12,3,102,1,3,1,3,5,3,107,8,3,
        10,3,12,3,110,9,3,1,3,3,3,113,8,3,1,4,1,4,1,4,1,4,1,4,1,4,4,4,121,
        8,4,11,4,12,4,122,1,4,1,4,1,5,1,5,1,5,1,5,1,5,4,5,132,8,5,11,5,12,
        5,133,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,146,8,6,11,6,12,
        6,147,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,4,7,158,8,7,11,7,12,7,159,
        1,7,1,7,1,8,1,8,1,8,1,8,1,8,4,8,169,8,8,11,8,12,8,170,1,8,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,9,4,9,182,8,9,11,9,12,9,183,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,5,10,193,8,10,10,10,12,10,196,9,10,3,10,198,
        8,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,208,8,11,10,11,
        12,11,211,9,11,3,11,213,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,13,1,13,1,13,1,13,1,13,3,13,229,8,13,1,14,1,14,1,14,
        1,14,1,14,3,14,236,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,3,18,261,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,3,19,285,8,19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,293,8,19,10,
        19,12,19,296,9,19,1,20,1,20,1,20,1,20,3,20,302,8,20,1,21,1,21,1,
        21,1,21,3,21,308,8,21,1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,25,1,
        25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,29,0,1,38,30,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,0,3,2,0,5,18,58,59,2,0,5,6,36,36,1,0,60,62,346,0,
        61,1,0,0,0,2,67,1,0,0,0,4,92,1,0,0,0,6,94,1,0,0,0,8,114,1,0,0,0,
        10,126,1,0,0,0,12,137,1,0,0,0,14,151,1,0,0,0,16,163,1,0,0,0,18,175,
        1,0,0,0,20,187,1,0,0,0,22,201,1,0,0,0,24,220,1,0,0,0,26,228,1,0,
        0,0,28,235,1,0,0,0,30,237,1,0,0,0,32,243,1,0,0,0,34,249,1,0,0,0,
        36,260,1,0,0,0,38,284,1,0,0,0,40,301,1,0,0,0,42,307,1,0,0,0,44,309,
        1,0,0,0,46,312,1,0,0,0,48,314,1,0,0,0,50,316,1,0,0,0,52,318,1,0,
        0,0,54,320,1,0,0,0,56,322,1,0,0,0,58,324,1,0,0,0,60,62,3,2,1,0,61,
        60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,
        0,65,66,5,0,0,1,66,1,1,0,0,0,67,72,3,4,2,0,68,69,5,56,0,0,69,71,
        3,4,2,0,70,68,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,
        73,76,1,0,0,0,74,72,1,0,0,0,75,77,5,56,0,0,76,75,1,0,0,0,76,77,1,
        0,0,0,77,78,1,0,0,0,78,79,5,57,0,0,79,3,1,0,0,0,80,93,3,6,3,0,81,
        93,3,12,6,0,82,93,3,14,7,0,83,93,3,16,8,0,84,93,3,20,10,0,85,93,
        3,34,17,0,86,93,3,22,11,0,87,93,3,54,27,0,88,93,3,56,28,0,89,93,
        3,58,29,0,90,93,3,38,19,0,91,93,3,24,12,0,92,80,1,0,0,0,92,81,1,
        0,0,0,92,82,1,0,0,0,92,83,1,0,0,0,92,84,1,0,0,0,92,85,1,0,0,0,92,
        86,1,0,0,0,92,87,1,0,0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,1,0,0,
        0,92,91,1,0,0,0,93,5,1,0,0,0,94,95,5,25,0,0,95,96,3,38,19,0,96,97,
        5,55,0,0,97,98,5,57,0,0,98,100,5,1,0,0,99,101,3,2,1,0,100,99,1,0,
        0,0,101,102,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,104,1,0,
        0,0,104,108,5,2,0,0,105,107,3,8,4,0,106,105,1,0,0,0,107,110,1,0,
        0,0,108,106,1,0,0,0,108,109,1,0,0,0,109,112,1,0,0,0,110,108,1,0,
        0,0,111,113,3,10,5,0,112,111,1,0,0,0,112,113,1,0,0,0,113,7,1,0,0,
        0,114,115,5,26,0,0,115,116,3,38,19,0,116,117,5,55,0,0,117,118,5,
        57,0,0,118,120,5,1,0,0,119,121,3,2,1,0,120,119,1,0,0,0,121,122,1,
        0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,124,1,0,0,0,124,125,5,
        2,0,0,125,9,1,0,0,0,126,127,5,27,0,0,127,128,5,55,0,0,128,129,5,
        57,0,0,129,131,5,1,0,0,130,132,3,2,1,0,131,130,1,0,0,0,132,133,1,
        0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,135,1,0,0,0,135,136,5,
        2,0,0,136,11,1,0,0,0,137,138,5,29,0,0,138,139,3,36,18,0,139,140,
        5,30,0,0,140,141,3,38,19,0,141,142,5,55,0,0,142,143,5,57,0,0,143,
        145,5,1,0,0,144,146,3,2,1,0,145,144,1,0,0,0,146,147,1,0,0,0,147,
        145,1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,150,5,2,0,0,150,
        13,1,0,0,0,151,152,5,28,0,0,152,153,3,38,19,0,153,154,5,55,0,0,154,
        155,5,57,0,0,155,157,5,1,0,0,156,158,3,2,1,0,157,156,1,0,0,0,158,
        159,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,
        162,5,2,0,0,162,15,1,0,0,0,163,164,5,31,0,0,164,165,5,55,0,0,165,
        166,5,57,0,0,166,168,5,1,0,0,167,169,3,2,1,0,168,167,1,0,0,0,169,
        170,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,
        173,5,2,0,0,173,174,3,18,9,0,174,17,1,0,0,0,175,176,5,33,0,0,176,
        177,3,38,19,0,177,178,5,55,0,0,178,179,5,57,0,0,179,181,5,1,0,0,
        180,182,3,2,1,0,181,180,1,0,0,0,182,183,1,0,0,0,183,181,1,0,0,0,
        183,184,1,0,0,0,184,185,1,0,0,0,185,186,5,2,0,0,186,19,1,0,0,0,187,
        188,3,36,18,0,188,197,5,47,0,0,189,194,3,38,19,0,190,191,5,54,0,
        0,191,193,3,38,19,0,192,190,1,0,0,0,193,196,1,0,0,0,194,192,1,0,
        0,0,194,195,1,0,0,0,195,198,1,0,0,0,196,194,1,0,0,0,197,189,1,0,
        0,0,197,198,1,0,0,0,198,199,1,0,0,0,199,200,5,48,0,0,200,21,1,0,
        0,0,201,202,5,21,0,0,202,203,3,36,18,0,203,212,5,47,0,0,204,209,
        3,36,18,0,205,206,5,54,0,0,206,208,3,36,18,0,207,205,1,0,0,0,208,
        211,1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,213,1,0,0,0,211,
        209,1,0,0,0,212,204,1,0,0,0,212,213,1,0,0,0,213,214,1,0,0,0,214,
        215,5,48,0,0,215,216,5,55,0,0,216,217,5,1,0,0,217,218,3,4,2,0,218,
        219,5,2,0,0,219,23,1,0,0,0,220,221,5,46,0,0,221,222,3,28,14,0,222,
        25,1,0,0,0,223,224,5,12,0,0,224,225,3,36,18,0,225,226,5,19,0,0,226,
        229,1,0,0,0,227,229,5,68,0,0,228,223,1,0,0,0,228,227,1,0,0,0,229,
        27,1,0,0,0,230,231,5,19,0,0,231,232,3,36,18,0,232,233,5,13,0,0,233,
        236,1,0,0,0,234,236,5,69,0,0,235,230,1,0,0,0,235,234,1,0,0,0,236,
        29,1,0,0,0,237,238,5,12,0,0,238,239,3,36,18,0,239,240,5,19,0,0,240,
        241,3,36,18,0,241,242,5,13,0,0,242,31,1,0,0,0,243,244,5,19,0,0,244,
        245,3,36,18,0,245,246,5,12,0,0,246,247,3,36,18,0,247,248,5,19,0,
        0,248,33,1,0,0,0,249,250,3,36,18,0,250,251,5,20,0,0,251,252,3,38,
        19,0,252,35,1,0,0,0,253,261,5,63,0,0,254,255,5,12,0,0,255,256,5,
        63,0,0,256,261,5,19,0,0,257,258,5,19,0,0,258,259,5,63,0,0,259,261,
        5,13,0,0,260,253,1,0,0,0,260,254,1,0,0,0,260,257,1,0,0,0,261,37,
        1,0,0,0,262,263,6,19,-1,0,263,264,5,47,0,0,264,265,3,38,19,0,265,
        266,5,48,0,0,266,285,1,0,0,0,267,268,3,48,24,0,268,269,3,38,19,17,
        269,285,1,0,0,0,270,285,3,52,26,0,271,285,3,36,18,0,272,285,3,20,
        10,0,273,285,3,40,20,0,274,285,3,42,21,0,275,285,3,44,22,0,276,285,
        3,26,13,0,277,285,3,28,14,0,278,285,5,65,0,0,279,285,5,64,0,0,280,
        285,5,66,0,0,281,285,5,67,0,0,282,285,5,39,0,0,283,285,5,40,0,0,
        284,262,1,0,0,0,284,267,1,0,0,0,284,270,1,0,0,0,284,271,1,0,0,0,
        284,272,1,0,0,0,284,273,1,0,0,0,284,274,1,0,0,0,284,275,1,0,0,0,
        284,276,1,0,0,0,284,277,1,0,0,0,284,278,1,0,0,0,284,279,1,0,0,0,
        284,280,1,0,0,0,284,281,1,0,0,0,284,282,1,0,0,0,284,283,1,0,0,0,
        285,294,1,0,0,0,286,287,10,14,0,0,287,288,3,46,23,0,288,289,3,38,
        19,15,289,293,1,0,0,0,290,291,10,16,0,0,291,293,3,50,25,0,292,286,
        1,0,0,0,292,290,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,0,294,295,
        1,0,0,0,295,39,1,0,0,0,296,294,1,0,0,0,297,302,3,30,15,0,298,299,
        3,26,13,0,299,300,3,28,14,0,300,302,1,0,0,0,301,297,1,0,0,0,301,
        298,1,0,0,0,302,41,1,0,0,0,303,308,3,32,16,0,304,305,3,28,14,0,305,
        306,3,26,13,0,306,308,1,0,0,0,307,303,1,0,0,0,307,304,1,0,0,0,308,
        43,1,0,0,0,309,310,3,28,14,0,310,311,3,28,14,0,311,45,1,0,0,0,312,
        313,7,0,0,0,313,47,1,0,0,0,314,315,7,1,0,0,315,49,1,0,0,0,316,317,
        7,2,0,0,317,51,1,0,0,0,318,319,5,45,0,0,319,53,1,0,0,0,320,321,5,
        42,0,0,321,55,1,0,0,0,322,323,5,44,0,0,323,57,1,0,0,0,324,325,5,
        43,0,0,325,59,1,0,0,0,25,63,72,76,92,102,108,112,122,133,147,159,
        170,183,194,197,209,212,228,235,260,284,292,294,301,307
    ]

class QuantumLanguageParser ( Parser ):

    grammarFileName = "QuantumLanguageParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'//'", "'%'", 
                     "'**'", "'<'", "'>'", "'=='", "'>='", "'<='", "'<>'", 
                     "'!='", "'|'", "'='", "'def'", "'return'", "'raise'", 
                     "'assert'", "'if'", "'elif'", "'else'", "'while'", 
                     "'for'", "'in'", "'try'", "'finally'", "'except'", 
                     "'or'", "'and'", "'not'", "'is'", "'None'", "'True'", 
                     "'False'", "'class'", "'pass'", "'continue'", "'break'", 
                     "'pi'", "'plot'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'.'", "','", "':'", "';'", "<INVALID>", "'@'", 
                     "'(X)'", "'T'", "'''", "'t'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "SPACES", "COMMENTS", 
                      "ADD", "MINUS", "STAR", "DIV", "IDIV", "MOD", "POWER", 
                      "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", 
                      "NOT_EQ_1", "NOT_EQ_2", "PIPE", "ASSIGN", "DEF", "RETURN", 
                      "RAISE", "ASSERT", "IF", "ELIF", "ELSE", "WHILE", 
                      "FOR", "IN", "TRY", "FINALLY", "EXCEPT", "OR", "AND", 
                      "NOT", "IS", "NONE", "TRUE", "FALSE", "CLASS", "PASS", 
                      "CONTINUE", "BREAK", "PI", "PLOT", "OPEN_PAREN", "CLOSE_PAREN", 
                      "OPEN_BRACK", "CLOSE_BRACK", "OPEN_BRACE", "CLOSE_BRACE", 
                      "DOT", "COMMA", "COLON", "SEMI_COLON", "NEWLINE", 
                      "MATMUL", "KRONECKER", "HERMITIAN", "CONJUGATE", "TRANSPOSE", 
                      "IDENTIFIER", "STRING_LITERAL", "INTEGER_LITERAL", 
                      "IMAGINARY_LITERAL", "FLOAT_LITERAL", "BRA_LITERAL", 
                      "KET_LITERAL" ]

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
    RULE_plot = 12
    RULE_bra = 13
    RULE_ket = 14
    RULE_braket = 15
    RULE_ketbra = 16
    RULE_assign = 17
    RULE_identifier = 18
    RULE_expression = 19
    RULE_inner_product = 20
    RULE_outer_product = 21
    RULE_kron_product = 22
    RULE_binary_operator = 23
    RULE_prefix_unitary_operator = 24
    RULE_suffix_unitary_operator = 25
    RULE_constant = 26
    RULE_pass = 27
    RULE_break = 28
    RULE_continue = 29

    ruleNames =  [ "start", "statement", "sentence", "if", "elif", "else", 
                   "for", "while", "try", "except", "function_execution", 
                   "function_declaration", "plot", "bra", "ket", "braket", 
                   "ketbra", "assign", "identifier", "expression", "inner_product", 
                   "outer_product", "kron_product", "binary_operator", "prefix_unitary_operator", 
                   "suffix_unitary_operator", "constant", "pass", "break", 
                   "continue" ]

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
    PIPE=19
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
    PI=45
    PLOT=46
    OPEN_PAREN=47
    CLOSE_PAREN=48
    OPEN_BRACK=49
    CLOSE_BRACK=50
    OPEN_BRACE=51
    CLOSE_BRACE=52
    DOT=53
    COMMA=54
    COLON=55
    SEMI_COLON=56
    NEWLINE=57
    MATMUL=58
    KRONECKER=59
    HERMITIAN=60
    CONJUGATE=61
    TRANSPOSE=62
    IDENTIFIER=63
    STRING_LITERAL=64
    INTEGER_LITERAL=65
    IMAGINARY_LITERAL=66
    FLOAT_LITERAL=67
    BRA_LITERAL=68
    KET_LITERAL=69

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
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.statement()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223093238948687776) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 63) != 0):
                    break

            self.state = 65
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
            self.state = 67
            self.sentence()
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 68
                    self.match(QuantumLanguageParser.SEMI_COLON)
                    self.state = 69
                    self.sentence() 
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 75
                self.match(QuantumLanguageParser.SEMI_COLON)


            self.state = 78
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


        def break_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.BreakContext,0)


        def continue_(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ContinueContext,0)


        def expression(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ExpressionContext,0)


        def plot(self):
            return self.getTypedRuleContext(QuantumLanguageParser.PlotContext,0)


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
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.if_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.for_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.while_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 83
                self.try_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 84
                self.function_execution()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 85
                self.assign()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 86
                self.function_declaration()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 87
                self.pass_()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 88
                self.break_()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 89
                self.continue_()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 90
                self.expression(0)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 91
                self.plot()
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
            self.state = 94
            self.match(QuantumLanguageParser.IF)
            self.state = 95
            self.expression(0)
            self.state = 96
            self.match(QuantumLanguageParser.COLON)
            self.state = 97
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 98
            self.match(QuantumLanguageParser.INDENT)
            self.state = 100 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 99
                self.statement()
                self.state = 102 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223093238948687776) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 63) != 0):
                    break

            self.state = 104
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 105
                self.elif_()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 111
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
            self.state = 114
            self.match(QuantumLanguageParser.ELIF)
            self.state = 115
            self.expression(0)
            self.state = 116
            self.match(QuantumLanguageParser.COLON)
            self.state = 117
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 118
            self.match(QuantumLanguageParser.INDENT)
            self.state = 120 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 119
                self.statement()
                self.state = 122 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223093238948687776) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 63) != 0):
                    break

            self.state = 124
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
            self.state = 126
            self.match(QuantumLanguageParser.ELSE)
            self.state = 127
            self.match(QuantumLanguageParser.COLON)
            self.state = 128
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 129
            self.match(QuantumLanguageParser.INDENT)
            self.state = 131 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 130
                self.statement()
                self.state = 133 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223093238948687776) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 63) != 0):
                    break

            self.state = 135
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
            self.state = 137
            self.match(QuantumLanguageParser.FOR)
            self.state = 138
            self.identifier()
            self.state = 139
            self.match(QuantumLanguageParser.IN)
            self.state = 140
            self.expression(0)
            self.state = 141
            self.match(QuantumLanguageParser.COLON)
            self.state = 142
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 143
            self.match(QuantumLanguageParser.INDENT)
            self.state = 145 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 144
                self.statement()
                self.state = 147 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223093238948687776) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 63) != 0):
                    break

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
            self.state = 151
            self.match(QuantumLanguageParser.WHILE)
            self.state = 152
            self.expression(0)
            self.state = 153
            self.match(QuantumLanguageParser.COLON)
            self.state = 154
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 155
            self.match(QuantumLanguageParser.INDENT)
            self.state = 157 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 156
                self.statement()
                self.state = 159 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223093238948687776) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 63) != 0):
                    break

            self.state = 161
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
            self.state = 163
            self.match(QuantumLanguageParser.TRY)
            self.state = 164
            self.match(QuantumLanguageParser.COLON)
            self.state = 165
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 166
            self.match(QuantumLanguageParser.INDENT)
            self.state = 168 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 167
                self.statement()
                self.state = 170 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223093238948687776) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 63) != 0):
                    break

            self.state = 172
            self.match(QuantumLanguageParser.DEDENT)
            self.state = 173
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
            self.state = 175
            self.match(QuantumLanguageParser.EXCEPT)
            self.state = 176
            self.expression(0)
            self.state = 177
            self.match(QuantumLanguageParser.COLON)
            self.state = 178
            self.match(QuantumLanguageParser.NEWLINE)
            self.state = 179
            self.match(QuantumLanguageParser.INDENT)
            self.state = 181 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 180
                self.statement()
                self.state = 183 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & -9223093238948687776) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 63) != 0):
                    break

            self.state = 185
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
            self.state = 187
            self.identifier()
            self.state = 188
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & -9223194397006884768) != 0 or (((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 63) != 0:
                self.state = 189
                self.expression(0)
                self.state = 194
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==54:
                    self.state = 190
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 191
                    self.expression(0)
                    self.state = 196
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 199
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
            self.state = 201
            self.match(QuantumLanguageParser.DEF)
            self.state = 202
            self.identifier()
            self.state = 203
            self.match(QuantumLanguageParser.OPEN_PAREN)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & -9223372036854247424) != 0:
                self.state = 204
                self.identifier()
                self.state = 209
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==54:
                    self.state = 205
                    self.match(QuantumLanguageParser.COMMA)
                    self.state = 206
                    self.identifier()
                    self.state = 211
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 214
            self.match(QuantumLanguageParser.CLOSE_PAREN)
            self.state = 215
            self.match(QuantumLanguageParser.COLON)
            self.state = 216
            self.match(QuantumLanguageParser.INDENT)
            self.state = 217
            self.sentence()
            self.state = 218
            self.match(QuantumLanguageParser.DEDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLOT(self):
            return self.getToken(QuantumLanguageParser.PLOT, 0)

        def ket(self):
            return self.getTypedRuleContext(QuantumLanguageParser.KetContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_plot

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlot" ):
                return visitor.visitPlot(self)
            else:
                return visitor.visitChildren(self)




    def plot(self):

        localctx = QuantumLanguageParser.PlotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_plot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(QuantumLanguageParser.PLOT)
            self.state = 221
            self.ket()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(QuantumLanguageParser.LESS_THAN, 0)

        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def PIPE(self):
            return self.getToken(QuantumLanguageParser.PIPE, 0)

        def BRA_LITERAL(self):
            return self.getToken(QuantumLanguageParser.BRA_LITERAL, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_bra

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBra" ):
                return visitor.visitBra(self)
            else:
                return visitor.visitChildren(self)




    def bra(self):

        localctx = QuantumLanguageParser.BraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_bra)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.match(QuantumLanguageParser.LESS_THAN)
                self.state = 224
                self.identifier()
                self.state = 225
                self.match(QuantumLanguageParser.PIPE)
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(QuantumLanguageParser.BRA_LITERAL)
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


    class KetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIPE(self):
            return self.getToken(QuantumLanguageParser.PIPE, 0)

        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def GREATER_THAN(self):
            return self.getToken(QuantumLanguageParser.GREATER_THAN, 0)

        def KET_LITERAL(self):
            return self.getToken(QuantumLanguageParser.KET_LITERAL, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_ket

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKet" ):
                return visitor.visitKet(self)
            else:
                return visitor.visitChildren(self)




    def ket(self):

        localctx = QuantumLanguageParser.KetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ket)
        try:
            self.state = 235
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(QuantumLanguageParser.PIPE)
                self.state = 231
                self.identifier()
                self.state = 232
                self.match(QuantumLanguageParser.GREATER_THAN)
                pass
            elif token in [69]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(QuantumLanguageParser.KET_LITERAL)
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


    class BraketContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(QuantumLanguageParser.LESS_THAN, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,i)


        def PIPE(self):
            return self.getToken(QuantumLanguageParser.PIPE, 0)

        def GREATER_THAN(self):
            return self.getToken(QuantumLanguageParser.GREATER_THAN, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_braket

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBraket" ):
                return visitor.visitBraket(self)
            else:
                return visitor.visitChildren(self)




    def braket(self):

        localctx = QuantumLanguageParser.BraketContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_braket)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(QuantumLanguageParser.LESS_THAN)
            self.state = 238
            self.identifier()
            self.state = 239
            self.match(QuantumLanguageParser.PIPE)
            self.state = 240
            self.identifier()
            self.state = 241
            self.match(QuantumLanguageParser.GREATER_THAN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KetbraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(QuantumLanguageParser.PIPE)
            else:
                return self.getToken(QuantumLanguageParser.PIPE, i)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,i)


        def LESS_THAN(self):
            return self.getToken(QuantumLanguageParser.LESS_THAN, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_ketbra

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKetbra" ):
                return visitor.visitKetbra(self)
            else:
                return visitor.visitChildren(self)




    def ketbra(self):

        localctx = QuantumLanguageParser.KetbraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ketbra)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(QuantumLanguageParser.PIPE)
            self.state = 244
            self.identifier()
            self.state = 245
            self.match(QuantumLanguageParser.LESS_THAN)
            self.state = 246
            self.identifier()
            self.state = 247
            self.match(QuantumLanguageParser.PIPE)
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
        self.enterRule(localctx, 34, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.identifier()
            self.state = 250
            self.match(QuantumLanguageParser.ASSIGN)
            self.state = 251
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

        def IDENTIFIER(self):
            return self.getToken(QuantumLanguageParser.IDENTIFIER, 0)

        def LESS_THAN(self):
            return self.getToken(QuantumLanguageParser.LESS_THAN, 0)

        def PIPE(self):
            return self.getToken(QuantumLanguageParser.PIPE, 0)

        def GREATER_THAN(self):
            return self.getToken(QuantumLanguageParser.GREATER_THAN, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = QuantumLanguageParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_identifier)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(QuantumLanguageParser.IDENTIFIER)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(QuantumLanguageParser.LESS_THAN)
                self.state = 255
                self.match(QuantumLanguageParser.IDENTIFIER)
                self.state = 256
                self.match(QuantumLanguageParser.PIPE)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.match(QuantumLanguageParser.PIPE)
                self.state = 258
                self.match(QuantumLanguageParser.IDENTIFIER)
                self.state = 259
                self.match(QuantumLanguageParser.GREATER_THAN)
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


        def constant(self):
            return self.getTypedRuleContext(QuantumLanguageParser.ConstantContext,0)


        def identifier(self):
            return self.getTypedRuleContext(QuantumLanguageParser.IdentifierContext,0)


        def function_execution(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Function_executionContext,0)


        def inner_product(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Inner_productContext,0)


        def outer_product(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Outer_productContext,0)


        def kron_product(self):
            return self.getTypedRuleContext(QuantumLanguageParser.Kron_productContext,0)


        def bra(self):
            return self.getTypedRuleContext(QuantumLanguageParser.BraContext,0)


        def ket(self):
            return self.getTypedRuleContext(QuantumLanguageParser.KetContext,0)


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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 263
                self.match(QuantumLanguageParser.OPEN_PAREN)
                self.state = 264
                self.expression(0)
                self.state = 265
                self.match(QuantumLanguageParser.CLOSE_PAREN)
                pass

            elif la_ == 2:
                self.state = 267
                self.prefix_unitary_operator()
                self.state = 268
                self.expression(17)
                pass

            elif la_ == 3:
                self.state = 270
                self.constant()
                pass

            elif la_ == 4:
                self.state = 271
                self.identifier()
                pass

            elif la_ == 5:
                self.state = 272
                self.function_execution()
                pass

            elif la_ == 6:
                self.state = 273
                self.inner_product()
                pass

            elif la_ == 7:
                self.state = 274
                self.outer_product()
                pass

            elif la_ == 8:
                self.state = 275
                self.kron_product()
                pass

            elif la_ == 9:
                self.state = 276
                self.bra()
                pass

            elif la_ == 10:
                self.state = 277
                self.ket()
                pass

            elif la_ == 11:
                self.state = 278
                self.match(QuantumLanguageParser.INTEGER_LITERAL)
                pass

            elif la_ == 12:
                self.state = 279
                self.match(QuantumLanguageParser.STRING_LITERAL)
                pass

            elif la_ == 13:
                self.state = 280
                self.match(QuantumLanguageParser.IMAGINARY_LITERAL)
                pass

            elif la_ == 14:
                self.state = 281
                self.match(QuantumLanguageParser.FLOAT_LITERAL)
                pass

            elif la_ == 15:
                self.state = 282
                self.match(QuantumLanguageParser.TRUE)
                pass

            elif la_ == 16:
                self.state = 283
                self.match(QuantumLanguageParser.FALSE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 292
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = QuantumLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 286
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 287
                        self.binary_operator()
                        self.state = 288
                        self.expression(15)
                        pass

                    elif la_ == 2:
                        localctx = QuantumLanguageParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 290
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 291
                        self.suffix_unitary_operator()
                        pass

             
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Inner_productContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def braket(self):
            return self.getTypedRuleContext(QuantumLanguageParser.BraketContext,0)


        def bra(self):
            return self.getTypedRuleContext(QuantumLanguageParser.BraContext,0)


        def ket(self):
            return self.getTypedRuleContext(QuantumLanguageParser.KetContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_inner_product

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInner_product" ):
                return visitor.visitInner_product(self)
            else:
                return visitor.visitChildren(self)




    def inner_product(self):

        localctx = QuantumLanguageParser.Inner_productContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_inner_product)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.braket()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.bra()
                self.state = 299
                self.ket()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Outer_productContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ketbra(self):
            return self.getTypedRuleContext(QuantumLanguageParser.KetbraContext,0)


        def ket(self):
            return self.getTypedRuleContext(QuantumLanguageParser.KetContext,0)


        def bra(self):
            return self.getTypedRuleContext(QuantumLanguageParser.BraContext,0)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_outer_product

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOuter_product" ):
                return visitor.visitOuter_product(self)
            else:
                return visitor.visitChildren(self)




    def outer_product(self):

        localctx = QuantumLanguageParser.Outer_productContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_outer_product)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.ketbra()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.ket()
                self.state = 305
                self.bra()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kron_productContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ket(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(QuantumLanguageParser.KetContext)
            else:
                return self.getTypedRuleContext(QuantumLanguageParser.KetContext,i)


        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_kron_product

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKron_product" ):
                return visitor.visitKron_product(self)
            else:
                return visitor.visitChildren(self)




    def kron_product(self):

        localctx = QuantumLanguageParser.Kron_productContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_kron_product)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.ket()
            self.state = 310
            self.ket()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 46, self.RULE_binary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 864691128455659488) != 0):
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
        self.enterRule(localctx, 48, self.RULE_prefix_unitary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 68719476832) != 0):
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
        self.enterRule(localctx, 50, self.RULE_suffix_unitary_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 8070450532247928832) != 0):
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


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PI(self):
            return self.getToken(QuantumLanguageParser.PI, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_constant

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = QuantumLanguageParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_constant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(QuantumLanguageParser.PI)
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
        self.enterRule(localctx, 54, self.RULE_pass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(QuantumLanguageParser.PASS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(QuantumLanguageParser.BREAK, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = QuantumLanguageParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.match(QuantumLanguageParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(QuantumLanguageParser.CONTINUE, 0)

        def getRuleIndex(self):
            return QuantumLanguageParser.RULE_continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue" ):
                return visitor.visitContinue(self)
            else:
                return visitor.visitChildren(self)




    def continue_(self):

        localctx = QuantumLanguageParser.ContinueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(QuantumLanguageParser.CONTINUE)
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
        self._predicates[19] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         




