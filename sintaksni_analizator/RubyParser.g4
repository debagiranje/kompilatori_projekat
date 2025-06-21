parser grammar RubyParser;

options { tokenVocab=RubyLekser; }

prog
    : terminator* expression_list EOF
    ;

expression_list
    : (expression terminator)+ (terminator)* 
    ;

expression
    : class_definition
    | method_definition
    | method_inline_call
    | if_statement
    | rvalue
    | return_statement
    | while_statement
    | for_statement
    | instance_variable_assignment
    | assignment
    ;

class_definition
    : CLASS klasa = id_ (LT nadklasa = id_)? crlf* attribute_definition* expression_list? END
    ;


attribute_definition
    : attr_type COLON id_ (COMMA COLON id_)* crlf
    ;

attr_type
    : ATTR_ACCESSOR
    | ATTR_READER
    | ATTR_WRITER
    ;

global_get
    : var_name = lvalue op = ASSIGN global_name = id_global
    ;

global_set
    : global_name = id_global op = ASSIGN result = all_result
    ;

global_result
    : id_global
    ;

method_inline_call
    : method_call
    ;

method_definition
    : (m = modif crlf)? method_definition_header method_definition_body? END
    ;

method_definition_body
    : expression_list
    ;

method_definition_header
    : DEF method_name crlf
    | DEF method_name method_definition_params crlf
    ;

method_name
    : id_method
    | id_
    ;

method_definition_params
    : LPAREN RPAREN
    | LPAREN method_definition_params_list RPAREN
    | method_definition_params_list
    ;

method_definition_params_list
    : method_definition_param_id
    | method_definition_params_list COMMA method_definition_param_id
    ;

method_definition_param_id
    : id_
    ;

return_statement
    : RETURN all_result
    ;

method_call
    : primary (DOT method_name method_call_param_list?)*     
    | method_name method_call_param_list?
    | method_name method_call_args
    ;

method_call_args
    : method_param+
    ;

method_call_param_list
    : LPAREN (method_call_params)? RPAREN
    ;

method_call_params
    : method_param
    | method_call_params COMMA method_param
    ;

method_param
    : method_unnamed_param
    | method_named_param
    ;

method_unnamed_param
    : dynamic_result
    ;

method_named_param
    : id_ op = ASSIGN dynamic_result
    | id_ COLON dynamic_result
    ;

method_call_assignment
    : method_call
    ;

all_result
    : dynamic_result
    | global_result
    ;


cond_expression
    : comparison
    | bool_t
    ;


if_statement
    : IF cond_expression crlf statement_body (elsif_clause)* (else_clause)? END
    ;

elsif_clause
    : ELSIF cond_expression crlf statement_body
    ;

else_clause
    : else_token crlf statement_body
    ;


while_statement
    : WHILE cond_expression crlf statement_body END
    ;

for_statement
    : FOR id_ IN ((int_t dots int_t)|(dynamic_)) crlf statement_body END
    ;

all_assignment
    : dynamic_assignment
    ;

statement_body
    : statement_expression_list
    ;

statement_expression_list
    : expression terminator
    | break_expression terminator
    | statement_expression_list expression terminator
    | statement_expression_list break_expression terminator
    ;

assignment
    : lvalue ASSIGN rvalue
    | var_id = lvalue op = (
        PLUS_ASSIGN
        | MINUS_ASSIGN
        | MUL_ASSIGN
        | DIV_ASSIGN
        | MOD_ASSIGN
        | EXP_ASSIGN
    ) rvalue
    ;

instance_variable_assignment
    : instance_var ASSIGN value = rvalue
    | var_id = instance_var op = (
        PLUS_ASSIGN
        | MINUS_ASSIGN
        | MUL_ASSIGN
        | DIV_ASSIGN
        | MOD_ASSIGN
        | EXP_ASSIGN
    ) rvalue
    ;

dynamic_assignment
    : var_id = lvalue op = ASSIGN dynamic_result
    | var_id = lvalue op = (
        PLUS_ASSIGN
        | MINUS_ASSIGN
        | MUL_ASSIGN
        | DIV_ASSIGN
        | MOD_ASSIGN
        | EXP_ASSIGN
    ) dynamic_result
    ;

initial_array_assignment
    : var_id = lvalue op = ASSIGN LBRACK RBRACK
    ;

array_assignment
    : arr_def = array_selector op = ASSIGN arr_val = dynamic_result
    ;

array_definition
    : LBRACK array_definition_elements RBRACK
    ;

array_definition_elements
    : dynamic_result
    | array_definition_elements COMMA dynamic_result
    ;

array_selector
    : id_ LBRACK dynamic_result RBRACK
    | id_global LBRACK dynamic_result RBRACK
    ;

dynamic_result
    : dynamic_result op = (MUL | DIV | MOD) dynamic_result
    | dynamic_result op = (PLUS | MINUS) dynamic_result
    | LPAREN dynamic_result RPAREN
    | dynamic_
    ;

dynamic_
    : id_
    | int_t
    | float_t
    | str_t
    | inpterp
    | bool_t
    | nil_t
    | method_call
    | id_global
    | array_selector
    ;

comparison
    : left = comp_var op = (LT | GT | LE | GE) right = comp_var
    | left = comp_var op = ( EQ | NEQ) right = comp_var
    ;

comp_var
    : dynamic_result
    | array_selector
    | id_
    | instance_var
    ;

lvalue
    : id_
    | instance_var
    ;

rvalue
    : lvalue
    | initial_array_assignment
    | array_assignment
    | dynamic_assignment
    | assignment
    | method_call
    | bool_t
    | float_t
    | int_t
    | nil_t
    | dynamic_result
    | rvalue EXP rvalue
    | NOT rvalue
    | rvalue (MUL | DIV | MOD) rvalue
    | rvalue (PLUS | MINUS) rvalue
    | rvalue (LT | GT | LE | GE) rvalue
    | rvalue (EQ | NEQ) rvalue
    | rvalue AND rvalue                              
    | rvalue OR rvalue                               
    | BANG rvalue 
    | LPAREN rvalue RPAREN
    ;

break_expression
    : BREAK
    ;

str_t
    : STRING
    ;

float_t
    : FLOAT
    ;

int_t
    : INT
    ;

bool_t
    : TRUE
    | FALSE
    ;

nil_t
    : NIL
    ;

id_
    : ID
    ;

id_global
    : ID_GLOBAL
    ;

id_method
    : ID_METHOD
    ;

terminator
    : terminator SEMI
    | terminator crlf
    | SEMI
    | crlf
    ;

else_token
    : ELSE
    ;

crlf
    : CRLF+
    ;

instance_var
    : INSTANCE_VAR
    ;

modif
    : PRIVATE
    | PUBLIC
    | PROTECTED
    ;

dots
    : DOTDOT
    ;

primary
    : id_
    | instance_var
    | LPAREN expression RPAREN
    ;

inpterp
    : INTERPOLATED_STRING
    ;