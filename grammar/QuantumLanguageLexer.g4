lexer grammar QuantumLanguageLexer;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr4.Token import CommonToken
import re
import importlib
# Allow languages to extend the lexer and parser, by loading the parser dynamically
module_path = __name__[:-5]
language_name = __name__.split('.')[-1]
language_name = language_name[:-5]  # Remove Lexer from name
LanguageParser = getattr(importlib.import_module('{}Parser'.format(module_path)), '{}Parser'.format(language_name))
}

@lexer::members {
@property
def tokens(self):
    try:
        return self._tokens
    except AttributeError:
        self._tokens = []
        return self._tokens
@property
def indents(self):
    try:
        return self._indents
    except AttributeError:
        self._indents = []
        return self._indents
@property
def opened(self):
    try:
        return self._opened
    except AttributeError:
        self._opened = 0
        return self._opened
@opened.setter
def opened(self, value):
    self._opened = value
@property
def lastToken(self):
    try:
        return self._lastToken
    except AttributeError:
        self._lastToken = None
        return self._lastToken
@lastToken.setter
def lastToken(self, value):
    self._lastToken = value
def reset(self):
    super().reset()
    self.tokens = []
    self.indents = []
    self.opened = 0
    self.lastToken = None
def emitToken(self, t):
    super().emitToken(t)
    self.tokens.append(t)
def nextToken(self):
    if self._input.LA(1) == Token.EOF and self.indents:
        for i in range(len(self.tokens)-1,-1,-1):
            if self.tokens[i].type == Token.EOF:
                self.tokens.pop(i)
        self.emitToken(self.commonToken(LanguageParser.NEWLINE, '\n'))
        while self.indents:
            self.emitToken(self.createDedent())
            self.indents.pop()
        self.emitToken(self.commonToken(LanguageParser.EOF, "<EOF>"))
    next = super().nextToken()
    if next.channel == Token.DEFAULT_CHANNEL:
        self.lastToken = next
    return next if not self.tokens else self.tokens.pop(0)
def createDedent(self):
    dedent = self.commonToken(LanguageParser.DEDENT, "")
    dedent.line = self.lastToken.line
    return dedent
def commonToken(self, type, text, indent=0):
    stop = self.getCharIndex()-1-indent
    start = (stop - len(text) + 1) if text else stop
    return CommonToken(self._tokenFactorySourcePair, type, super().DEFAULT_TOKEN_CHANNEL, start, stop)
@staticmethod
def getIndentationCount(spaces):
    count = 0
    for ch in spaces:
        if ch == '\t':
            count += 8 - (count % 8)
        else:
            count += 1
    return count
def atStartOfInput(self):
    return Lexer.column.fget(self) == 0 and Lexer.line.fget(self) == 1
}

/* Skip */
SPACES: [ \t]+ -> skip;

/* Comments */
COMMENTS: '#' ~[\r\n\f]* -> skip;

/* Operators*/
// Math operators
ADD : '+';
MINUS : '-';
STAR : '*';
DIV : '/';
IDIV : '//';
MOD : '%';
POWER : '**';

// Bit operators
//OR_OP : '|';
//XOR : '^';
//AND_OP : '&';
//LEFT_SHIFT : '<<';
//RIGHT_SHIFT : '>>';

// Logical operators
LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ_1 : '<>';
NOT_EQ_2 : '!=';

// Assignations
ASSIGN : '=';
//ADD_ASSIGN : '+=';
//SUB_ASSIGN : '-=';
//MULT_ASSIGN : '*=';
//AT_ASSIGN : '@=';
//DIV_ASSIGN : '/=';
//MOD_ASSIGN : '%=';
//AND_ASSIGN : '&=';
//OR_ASSIGN : '|=';
//XOR_ASSIGN : '^=';
//LEFT_SHIFT_ASSIGN : '<<=';
//RIGHT_SHIFT_ASSIGN : '>>=';
//POWER_ASSIGN : '**=';
//IDIV_ASSIGN : '//=';

// Reserved keywords
DEF : 'def';
RETURN : 'return';
RAISE : 'raise';
//FROM : 'from';
//IMPORT : 'import';
//AS : 'as';
//GLOBAL : 'global';
//NONLOCAL : 'nonlocal';
ASSERT : 'assert';
IF : 'if';
ELIF : 'elif';
ELSE : 'else';
WHILE : 'while';
FOR : 'for';
IN : 'in';
TRY : 'try';
FINALLY : 'finally';
//WITH : 'with';
EXCEPT : 'except';
//LAMBDA : 'lambda';
OR : 'or';
AND : 'and';
NOT : 'not';
IS : 'is';
NONE : 'None';
TRUE : 'True';
FALSE : 'False';
CLASS : 'class';
//YIELD : 'yield';
//DEL : 'del';
PASS : 'pass';
CONTINUE : 'continue';
BREAK : 'break';
//ASYNC : 'async';
//AWAIT : 'await';
//TODO: Use commentned keywords


/* Grouping literals */
OPEN_PAREN : '(';
CLOSE_PAREN : ')';
OPEN_BRACK : '[';
CLOSE_BRACK : ']';
//OPEN_BRACE : '{';
//CLOSE_BRACE : '}';

/* Structural literals */
DOT : '.';
COMMA : ',';
COLON : ':';
SEMI_COLON : ';';
NEWLINE
 : ( {self.atStartOfInput()}?   SPACES
   | ( '\r'? '\n' | '\r' | '\f' ) SPACES?
   )
   {
tempt = Lexer.text.fget(self)
newLine = re.sub("[^\r\n\f]+", "", tempt)
spaces = re.sub("[\r\n\f]+", "", tempt)
la_char = ""
try:
    la = self._input.LA(1)
    la_char = chr(la)       # Python does not compare char to ints directly
except ValueError:          # End of file
    pass
# Strip newlines inside open clauses except if we are near EOF. We keep NEWLINEs near EOF to
# satisfy the final newline needed by the single_put rule used by the REPL.
try:
    nextnext_la = self._input.LA(2)
    nextnext_la_char = chr(nextnext_la)
except ValueError:
    nextnext_eof = True
else:
    nextnext_eof = False
if self.opened > 0 or nextnext_eof is False and (la_char == '\r' or la_char == '\n' or la_char == '\f' or la_char == '#'):
    self.skip()
else:
    indent = self.getIndentationCount(spaces)
    previous = self.indents[-1] if self.indents else 0
    self.emitToken(self.commonToken(self.NEWLINE, newLine, indent=indent))      # NEWLINE is actually the '\n' char
    if indent == previous:
        self.skip()
    elif indent > previous:
        self.indents.append(indent)
        self.emitToken(self.commonToken(LanguageParser.INDENT, spaces))
    else:
        while self.indents and self.indents[-1] > indent:
            self.emitToken(self.createDedent())
            self.indents.pop()
    }
 ;



// tokens { INDENT, DEDENT }
//INDENT: '{';
//DEDENT: '}';


// Linear Algebra Symbols
MATMUL : '@';
KRONECKER : '(X)';
HERMITIAN : 'T';
CONJUGATE : '\'';
TRANSPOSE: 't';


/* Identifier*/
IDENTIFIER: [a-zA-Z][a-zA-Z0-9_]*;

/* Qubits*/
QUBIT_IDENTIFIER
    : '|'[a-zA-Z][a-zA-Z0-9_]*'>'
    ;

QUBIT_TRANSPOSE_IDENTIFIER
    : '<'[a-zA-Z][a-zA-Z0-9_]*'|'
    ;

/* Literals */
STRING_LITERAL
    : '\'' .*? '\''
    | '"' .*? '"'
    ;

INTEGER_LITERAL
    : [1-9][0-9]*
    | [0]
    ;
//TODO: ADD BIN OCTAL HEX NUMBERS

IMAGINARY_LITERAL
    : (FLOAT_LITERAL|INTEGER_LITERAL) [iI]
    ;

FLOAT_LITERAL
    : INTEGER_LITERAL '.' [0-9]+
    ;

QUBIT_STATE_LITERAL
    : '|' [01+-]+ '>'
    ;

QUBIT_TRANSPOSE_STATE_LITERAL
    : '<' [01+-]+ '|'
    ;





