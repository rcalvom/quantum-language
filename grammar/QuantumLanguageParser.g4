parser grammar QuantumLanguageParser;

options {
	tokenVocab = QuantumLanguageLexer;
}

start
    : (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) EOF
    ;

sentence
    : if
    | for
    | while
    | try
    | function_execution
    | assign
    ;

if
    : IF expression COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    (elif)*
    (else)?
    ;

elif
    : ELIF expression COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    ;

else
    : ELSE COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    ;

for
    : FOR identifier IN expression COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    ;

while
    : WHILE expression COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    ;

try
    : TRY COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    except
    ;

except
    : EXCEPT expression COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    ;

function_execution
    : identifier OPEN_PAREN (expression (COMMA expression)*)? CLOSE_PAREN
    ;

assign
    : identifier ASSIGN expression;

identifier
    : IDENTIFIER (DOT IDENTIFIER)*
    ;

expression
    : OPEN_PAREN expression CLOSE_PAREN
    | expression binary_operator expression
    | unitary_operator expression
    | identifier
    | function_execution
    | INTEGER_LITERAL
    | STRING_LITERAL
    | IMAGINARY_LITERAL
    | FLOAT_LITERAL
    | TRUE | FALSE
    | QUBIT_STATE_LITERAL
    ;

binary_operator
    : ADD
    | MINUS
    | STAR
    | DIV
    | IDIV
    | MOD
    | POWER
    | LESS_THAN
    | GREATER_THAN
    | EQUALS
    | GT_EQ
    | LT_EQ
    | NOT_EQ_1
    | NOT_EQ_2
    ;

unitary_operator
    : ADD
    | MINUS
    | NOT
    ;
