lexer grammar RubyLekser;

// keywords 
CLASS   : 'class';
MODULE  : 'module';
DEF     : 'def';
END     : 'end';
IF      : 'if';
ELSE    : 'else';
ELSIF   : 'elsif';
WHILE   : 'while';
DO      : 'do';
RETURN  : 'return';
TRUE    : 'true';
FALSE   : 'false';
NIL     : 'nil';
FOR     : 'for';
ALIAS   : 'alias';
IN      : 'in';
BREAK   : 'break';
DOTDOT  : '..';

//modifs
PRIVATE : 'private';
PUBLIC  : 'public';
PROTECTED : 'protected';

// ops 
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';
MOD     : '%';
ASSIGN  : '=';
EQ      : '==';
NEQ     : '!=';
LT      : '<';
GT      : '>';
LE      : '<=';
GE      : '>=';
DOT     : '.';
PLUS_ASSIGN : '+=';
MINUS_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
MOD_ASSIGN: '%=';
EXP_ASSIGN: '**=';
NOT     : 'not';
EXP     : '**';
AND     : '&&';
OR      : '||';
BANG    : '!';


// syms 
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
LBRACK  : '[';
RBRACK  : ']';
COMMA   : ',';
COLON   : ':';
SEMI    : ';';

// lits/types
INT     : [0-9]+;
FLOAT   : [0-9]+ '.' [0-9]+;
STRING  : '"' ( ~["\\] | '\\' . )* '"' | '\'' ( ~['\\] | '\\' . )* '\''; 
INTERPOLATED_STRING : '"' ( ~["\\#] | '\\' . | '#{' .*? '}' )* '"' ;


//attrs
ATTR_ACCESSOR : 'attr_accessor';
ATTR_READER   : 'attr_reader';
ATTR_WRITER   : 'attr_writer';


// ids 
ID              : [a-zA-Z_][a-zA-Z0-9_]*;
INSTANCE_VAR    : '@' ID;
ID_GLOBAL       : '$' ID;
ID_METHOD       : [a-zA-Z_][a-zA-Z0-9_]* '?';

// comms, crlf i praznine
LINE_COMMENT : '#' ~[\r\n]* -> skip ;
ML_COMMENT   : ('=begin' .*? '=end' '\r'? '\n') -> skip ;
CRLF         : ('\r'? '\n')+;
WS           : [ \t\r]+ -> skip ;
