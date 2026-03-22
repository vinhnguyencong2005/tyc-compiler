grammar TyC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

// TODO: Define grammar rules here
program: (structDecl | funcDecl)* EOF;

// Struct
structDecl: STRUCT ID structBody SEMICOLON;
structBody: LB structMems RB;
structMems: structMemDecl*;
structMemDecl: explicitType ID SEMICOLON;

// function
funcDecl: returnType? ID LP paramList? RP innerBody;

// parameter list
paramList: param (COMMA param)*;
param: explicitType ID;

// Stament list
innerBody: blockStmt | stmt;
blockStmt: LB stmtList RB;
stmtList: stmt*;
stmt
    : blockStmt //finish
    | varDecl //finish
    | assignStmt //finish
    | returnStmt //finish
    | exprStmt // finish
    | ifStmt //finish
    | forStmt //finish
    | whileStmt //finish
    | continueStmt //finish
    | breakStmt //finsish
    | switchStmt; //finish

// Assign stament 
assignStmt: assignStmt_ SEMICOLON;
assignStmt_: lvalue ASSIGN expr;
lvalue: ID (DOT ID)*;

// If statment 
ifStmt: IF conditions innerBody (ELSE innerBody)?;

// While loop
whileStmt: WHILE conditions innerBody;

// For loop
forStmt: FOR forHeader innerBody;

forHeader: LP forOne forTwo forThree RP;

forOne: forInit? SEMICOLON;
forInit: variableType? ID ASSIGN expr;

forTwo: expr? SEMICOLON;

forThree
    : (assignStmt_
    | ID INCREMENT
    | ID DECREMENT
    | DECREMENT ID
    | INCREMENT ID)?;

// Return statment
returnStmt: RETURN expr? SEMICOLON;

// Break statement
breakStmt: BREAK SEMICOLON;

// Continue statment
continueStmt: CONTINUE SEMICOLON;

// Switch statement
switchStmt: SWITCH LP expr RP LB switchBody RB;

switchBody: caseClause* defaultClause? caseClause*;

caseClause: CASE expr COLON stmtList;

defaultClause: DEFAULT COLON stmtList;

// Conditions
conditions: LP expr RP;

// Expression hierarchy
exprStmt: expr SEMICOLON;
expr: assignmentExpr;

assignmentExpr
    : lvalue ASSIGN assignmentExpr
    | logicalOrExpr
    ;

logicalOrExpr: logicalAndExpr (LOGICAL_OR logicalAndExpr)*;

logicalAndExpr: equalityExpr (LOGICAL_AND equalityExpr)*;

equalityExpr: relationalExpr (equalityRelation relationalExpr)*;

equalityRelation: EQUAL | NOT_EQUAL;

relationalExpr: additiveExpr (orderingRelation additiveExpr)*;

orderingRelation: LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL;

additiveExpr: multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*;

multiplicativeExpr: unaryExpr ((MULTIPLY | DIVIDE | MODULUS) unaryExpr)*;

unaryExpr
    : LOGICAL_NOT unaryExpr
    | INCREMENT unaryExpr
    | DECREMENT unaryExpr
    | PLUS unaryExpr
    | MINUS unaryExpr
    | postfixExpr
    ;

postfixExpr: memberAccessExpr (INCREMENT | DECREMENT)*;

memberAccessExpr: primaryExpr (DOT ID)*;

primaryExpr
    : INTLIT
    | FLOATLIT
    | STRING_LIT
    | ID
    | LP expr RP
    | functionCall
    | structLiteral
    ;

structLiteral: LB (expr (COMMA expr)*)? RB;

// Function call
functionCall: ID LP (expr (COMMA expr)*)? RP;

// Variable declare
varDecl: variableType ID (ASSIGN expr)? SEMICOLON;

// Data types
variableType: explicitType | AUTO;
returnType: explicitType | VOID;
explicitType: primitiveType | structType;
structType: ID;
primitiveType: INT | FLOAT | STRING;

//////////////////////////////////////////////////////////////////////////////////////////////////////
// Below is lexer rules
WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tab

// Comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// Keywords
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// Operators
// Arithmetic operators
PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULUS: '%';

// Relational operators
EQUAL: '==';
NOT_EQUAL: '!=';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';

// Logical operators
LOGICAL_OR: '||';
LOGICAL_AND: '&&';
LOGICAL_NOT: '!';

// Increment/Decrement operators
INCREMENT: '++';
DECREMENT: '--';

// Assignment operator
ASSIGN: '=';

// Member access
DOT: '.';

// Separators
SEMICOLON: ';';
COMMA: ',';
COLON: ':';
LP: '(';
RP: ')';
LB: '{';
RB: '}';

// Numbers
FLOATLIT: ('0'|[1-9][0-9]*)? '.' [0-9]+ EXPONENTPART?
        | ('0'|[1-9][0-9]*) '.' [0-9]* EXPONENTPART?
        | ('0'|[1-9][0-9]*) EXPONENTPART;

fragment EXPONENTPART: [eE] [+-]? [1-9][0-9]*;
INTLIT: [0-9]+;

// Identifier
ID: ([a-z]|[A-Z]|'_')[a-zA-Z0-9_]*;

// String literals
// Error cases must come first to be detected before valid strings

// ILLEGAL_ESCAPE: detects illegal escape sequences
// Any backslash followed by a character that is NOT one of: b, f, r, n, t, ", \
// and is NOT followed by newline or carriage return
ILLEGAL_ESCAPE: '"' STR_CHAR*? '\\' ~[bfrnt"\\\r\n] {
    # Remove opening quote from text
    self.text = self.text[1:]
};

// UNCLOSE_STRING: detects unclosed strings
// String that encounters newline, carriage return, or EOF before closing quote
UNCLOSE_STRING: '"' STR_CHAR*? ([\r\n] | EOF) {
    # Remove opening quote from text
    self.text = self.text[1:]
    # If rule ended on a line break, do not include it in error message.
    if self.text and self.text[-1] in '\r\n':
        self.text = self.text[:-1]
};

// Contains zero or more characters with proper escape sequences
STRING_LIT: '"' STR_CHAR* '"' {
    # Remove enclosing quotes
    self.text = self.text[1:-1]
};

// Fragment for string characters
// Either an escape sequence or any character except ", \, \r, \n
fragment STR_CHAR
    : ESC_SEQ
    | ~["\\\r\n]  // Any character except double quote, backslash, carriage return, newline
    ;

// Fragment for valid escape sequences
fragment ESC_SEQ
    : '\\' [bfrnt"\\]  // Supported escape characters: b, f, r, n, t, ", \
    ;

// Invalid numbers with leading zeros - must come after valid numbers to catch the leftovers
INVALID_NUMBER: '0' [0-9]+ ('.' [0-9]+)? -> type(ERROR_CHAR);

// Invalid identifiers
// INVALID_ID: [0-9]+ ([a-df-zA-DF-Z]|'_') [a-zA-Z0-9_]* -> type(ERROR_CHAR);

ERROR_CHAR: .;