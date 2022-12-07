parser grammar QuantumLanguageParser;

options {
	tokenVocab = QuantumLanguageLexer;
}

start
    : statement+ EOF
    ;

statement
    : sentence (';' sentence)* (';')? NEWLINE;

sentence
    : if
    | for
    | while
    | try
    | function_execution
    | assign
    | function_declaration
    | pass
    | break
    | continue
    | expression
    ;


if
    : IF expression COLON NEWLINE INDENT statement+ DEDENT
    (elif)*
    (else)?
    ;

elif
    : ELIF expression COLON NEWLINE INDENT statement+ DEDENT
    ;

else
    : ELSE COLON NEWLINE INDENT statement+ DEDENT
    ;

for
    : FOR identifier IN expression COLON NEWLINE INDENT statement+ DEDENT
    ;

while
    : WHILE expression COLON NEWLINE INDENT statement+ DEDENT
    ;

try
    : TRY COLON NEWLINE INDENT statement+ DEDENT except
    ;

except
    : EXCEPT expression COLON NEWLINE INDENT statement+ DEDENT
    ;

function_execution
    : identifier OPEN_PAREN (expression (COMMA expression)*)? CLOSE_PAREN
    ;

function_declaration
    : DEF identifier OPEN_PAREN (identifier (COMMA identifier)*)? CLOSE_PAREN COLON INDENT sentence DEDENT
    ;

assign
    : identifier ASSIGN expression SEMI_COLON?;

identifier
    : IDENTIFIER
    ;

expression
    : OPEN_PAREN expression CLOSE_PAREN
    | prefix_unitary_operator expression
    | expression suffix_unitary_operator
    | single_qubit_gate expression
    | qubit_gate expression expression
    | constant
    | expression binary_operator expression
    | identifier
    | function_execution
    | inner_product
    | outer_product
    | bra
    | ket
    | INTEGER_LITERAL
    | STRING_LITERAL
    | IMAGINARY_LITERAL
    | FLOAT_LITERAL
    | TRUE | FALSE
    | QUBIT_STATE_LITERAL
    ;

inner_product
    : braket
    | bra ket
    ;

outer_product
    : ketbra
    | ket bra
    ;

bra
    : LESS_THAN (QUBIT_STATE_LITERAL|identifier) PIPE
    ;

ket
    : PIPE (QUBIT_STATE_LITERAL|identifier) GREATER_THAN
    ;

braket
    : LESS_THAN (QUBIT_STATE_LITERAL|identifier) PIPE (QUBIT_STATE_LITERAL|identifier) GREATER_THAN
    ;

ketbra
    : PIPE (QUBIT_STATE_LITERAL|identifier) GREATER_THAN LESS_THAN (QUBIT_STATE_LITERAL|identifier) PIPE
    ;

binary_operator
    : ADD
    | MINUS
    | STAR
    | DIV
    | IDIV
    | MOD
    | POWER
    | MATMUL
    | KRONECKER
    | LESS_THAN
    | GREATER_THAN
    | EQUALS
    | GT_EQ
    | LT_EQ
    | NOT_EQ_1
    | NOT_EQ_2
    ;

prefix_unitary_operator
    : ADD
    | MINUS
    | NOT
    ;

suffix_unitary_operator
    : HERMITIAN
    | CONJUGATE
    | TRANSPOSE
    ;

single_qubit_gate
    : X
    | Z
    | Y
    | H
    | S
    | SDG
    | T
    | TDG
    ;

qubit_gate
    : RX
    | RY
    | RZ
    | CX
    | P
    ;

constant
    : PI
    ;

pass
    : PASS
    ;

break
    : BREAK
    ;

continue
    : CONTINUE
    ;
