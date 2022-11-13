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
    | assign
    ;

if
    : IF expresion COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    (ELIF COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT)*
    (ELSE COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT)?
    ;

for
    : FOR expresion IN expresion COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    ;

while
    : WHILE expresion COLON INDENT (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) DEDENT
    ;

assign
    : identifier ASSIGN expresion;

identifier
    : IDENTIFIER (DOT IDENTIFIER)*
    ;

expresion
    : OPEN_PAREN expresion CLOSE_PAREN
    | expresion binary_operator expresion
    | unitary_operator expresion
    | identifier
    // | function_excecution
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
