lexer grammar QuantumLanguageLexer;

// Token injection implementation
// tokens { INDENT, DEDENT }

// Define superclass
options {
    superClass=QuantumLanguageLexerBase;
}


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
OR_OP : '|';
XOR : '^';
AND_OP : '&';
LEFT_SHIFT : '<<';
RIGHT_SHIFT : '>>';

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
// TODO: ADD diferent types of assignations

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
NEWLINE : '\n';

// tokens { INDENT, DEDENT }
INDENT: '{';
DEDENT: '}';


/* Identifier*/
IDENTIFIER: [a-zA-Z][a-zA-Z0-9_]*;

/* Literals */
STRING_LITERAL
    : '\'' . '\''
    | '"' . '"'
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




SPACES: [ \t\r\n]+ -> skip;

/* Tokens to skip */
COMMENTS: '#'~[\r\n]+ -> skip;

