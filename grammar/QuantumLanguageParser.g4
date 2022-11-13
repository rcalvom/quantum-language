parser grammar QuantumLanguageParser;

options {
	tokenVocab = QuantumLanguageLexer;
}

start
    : (sentence (SEMI_COLON? NEWLINE))* (sentence SEMI_COLON?) EOF
    ;

sentence
    : assign
    | if
    ;

if
    : IF
    ;

assign
    : IDENTIFIER ASSIGN INTEGER_LITERAL;