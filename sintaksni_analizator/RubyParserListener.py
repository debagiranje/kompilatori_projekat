# Generated from sintaksni_analizator/RubyParser.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RubyParser import RubyParser
else:
    from RubyParser import RubyParser

# This class defines a complete listener for a parse tree produced by RubyParser.
class RubyParserListener(ParseTreeListener):

    # Enter a parse tree produced by RubyParser#prog.
    def enterProg(self, ctx:RubyParser.ProgContext):
        pass

    # Exit a parse tree produced by RubyParser#prog.
    def exitProg(self, ctx:RubyParser.ProgContext):
        pass


    # Enter a parse tree produced by RubyParser#expression_list.
    def enterExpression_list(self, ctx:RubyParser.Expression_listContext):
        pass

    # Exit a parse tree produced by RubyParser#expression_list.
    def exitExpression_list(self, ctx:RubyParser.Expression_listContext):
        pass


    # Enter a parse tree produced by RubyParser#expression.
    def enterExpression(self, ctx:RubyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by RubyParser#expression.
    def exitExpression(self, ctx:RubyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by RubyParser#class_definition.
    def enterClass_definition(self, ctx:RubyParser.Class_definitionContext):
        pass

    # Exit a parse tree produced by RubyParser#class_definition.
    def exitClass_definition(self, ctx:RubyParser.Class_definitionContext):
        pass


    # Enter a parse tree produced by RubyParser#attribute_definition.
    def enterAttribute_definition(self, ctx:RubyParser.Attribute_definitionContext):
        pass

    # Exit a parse tree produced by RubyParser#attribute_definition.
    def exitAttribute_definition(self, ctx:RubyParser.Attribute_definitionContext):
        pass


    # Enter a parse tree produced by RubyParser#attr_type.
    def enterAttr_type(self, ctx:RubyParser.Attr_typeContext):
        pass

    # Exit a parse tree produced by RubyParser#attr_type.
    def exitAttr_type(self, ctx:RubyParser.Attr_typeContext):
        pass


    # Enter a parse tree produced by RubyParser#global_get.
    def enterGlobal_get(self, ctx:RubyParser.Global_getContext):
        pass

    # Exit a parse tree produced by RubyParser#global_get.
    def exitGlobal_get(self, ctx:RubyParser.Global_getContext):
        pass


    # Enter a parse tree produced by RubyParser#global_set.
    def enterGlobal_set(self, ctx:RubyParser.Global_setContext):
        pass

    # Exit a parse tree produced by RubyParser#global_set.
    def exitGlobal_set(self, ctx:RubyParser.Global_setContext):
        pass


    # Enter a parse tree produced by RubyParser#global_result.
    def enterGlobal_result(self, ctx:RubyParser.Global_resultContext):
        pass

    # Exit a parse tree produced by RubyParser#global_result.
    def exitGlobal_result(self, ctx:RubyParser.Global_resultContext):
        pass


    # Enter a parse tree produced by RubyParser#method_inline_call.
    def enterMethod_inline_call(self, ctx:RubyParser.Method_inline_callContext):
        pass

    # Exit a parse tree produced by RubyParser#method_inline_call.
    def exitMethod_inline_call(self, ctx:RubyParser.Method_inline_callContext):
        pass


    # Enter a parse tree produced by RubyParser#method_definition.
    def enterMethod_definition(self, ctx:RubyParser.Method_definitionContext):
        pass

    # Exit a parse tree produced by RubyParser#method_definition.
    def exitMethod_definition(self, ctx:RubyParser.Method_definitionContext):
        pass


    # Enter a parse tree produced by RubyParser#method_definition_body.
    def enterMethod_definition_body(self, ctx:RubyParser.Method_definition_bodyContext):
        pass

    # Exit a parse tree produced by RubyParser#method_definition_body.
    def exitMethod_definition_body(self, ctx:RubyParser.Method_definition_bodyContext):
        pass


    # Enter a parse tree produced by RubyParser#method_definition_header.
    def enterMethod_definition_header(self, ctx:RubyParser.Method_definition_headerContext):
        pass

    # Exit a parse tree produced by RubyParser#method_definition_header.
    def exitMethod_definition_header(self, ctx:RubyParser.Method_definition_headerContext):
        pass


    # Enter a parse tree produced by RubyParser#method_name.
    def enterMethod_name(self, ctx:RubyParser.Method_nameContext):
        pass

    # Exit a parse tree produced by RubyParser#method_name.
    def exitMethod_name(self, ctx:RubyParser.Method_nameContext):
        pass


    # Enter a parse tree produced by RubyParser#method_definition_params.
    def enterMethod_definition_params(self, ctx:RubyParser.Method_definition_paramsContext):
        pass

    # Exit a parse tree produced by RubyParser#method_definition_params.
    def exitMethod_definition_params(self, ctx:RubyParser.Method_definition_paramsContext):
        pass


    # Enter a parse tree produced by RubyParser#method_definition_params_list.
    def enterMethod_definition_params_list(self, ctx:RubyParser.Method_definition_params_listContext):
        pass

    # Exit a parse tree produced by RubyParser#method_definition_params_list.
    def exitMethod_definition_params_list(self, ctx:RubyParser.Method_definition_params_listContext):
        pass


    # Enter a parse tree produced by RubyParser#method_definition_param_id.
    def enterMethod_definition_param_id(self, ctx:RubyParser.Method_definition_param_idContext):
        pass

    # Exit a parse tree produced by RubyParser#method_definition_param_id.
    def exitMethod_definition_param_id(self, ctx:RubyParser.Method_definition_param_idContext):
        pass


    # Enter a parse tree produced by RubyParser#return_statement.
    def enterReturn_statement(self, ctx:RubyParser.Return_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#return_statement.
    def exitReturn_statement(self, ctx:RubyParser.Return_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#method_call.
    def enterMethod_call(self, ctx:RubyParser.Method_callContext):
        pass

    # Exit a parse tree produced by RubyParser#method_call.
    def exitMethod_call(self, ctx:RubyParser.Method_callContext):
        pass


    # Enter a parse tree produced by RubyParser#method_call_args.
    def enterMethod_call_args(self, ctx:RubyParser.Method_call_argsContext):
        pass

    # Exit a parse tree produced by RubyParser#method_call_args.
    def exitMethod_call_args(self, ctx:RubyParser.Method_call_argsContext):
        pass


    # Enter a parse tree produced by RubyParser#method_call_param_list.
    def enterMethod_call_param_list(self, ctx:RubyParser.Method_call_param_listContext):
        pass

    # Exit a parse tree produced by RubyParser#method_call_param_list.
    def exitMethod_call_param_list(self, ctx:RubyParser.Method_call_param_listContext):
        pass


    # Enter a parse tree produced by RubyParser#method_call_params.
    def enterMethod_call_params(self, ctx:RubyParser.Method_call_paramsContext):
        pass

    # Exit a parse tree produced by RubyParser#method_call_params.
    def exitMethod_call_params(self, ctx:RubyParser.Method_call_paramsContext):
        pass


    # Enter a parse tree produced by RubyParser#method_param.
    def enterMethod_param(self, ctx:RubyParser.Method_paramContext):
        pass

    # Exit a parse tree produced by RubyParser#method_param.
    def exitMethod_param(self, ctx:RubyParser.Method_paramContext):
        pass


    # Enter a parse tree produced by RubyParser#method_unnamed_param.
    def enterMethod_unnamed_param(self, ctx:RubyParser.Method_unnamed_paramContext):
        pass

    # Exit a parse tree produced by RubyParser#method_unnamed_param.
    def exitMethod_unnamed_param(self, ctx:RubyParser.Method_unnamed_paramContext):
        pass


    # Enter a parse tree produced by RubyParser#method_named_param.
    def enterMethod_named_param(self, ctx:RubyParser.Method_named_paramContext):
        pass

    # Exit a parse tree produced by RubyParser#method_named_param.
    def exitMethod_named_param(self, ctx:RubyParser.Method_named_paramContext):
        pass


    # Enter a parse tree produced by RubyParser#method_call_assignment.
    def enterMethod_call_assignment(self, ctx:RubyParser.Method_call_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#method_call_assignment.
    def exitMethod_call_assignment(self, ctx:RubyParser.Method_call_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#all_result.
    def enterAll_result(self, ctx:RubyParser.All_resultContext):
        pass

    # Exit a parse tree produced by RubyParser#all_result.
    def exitAll_result(self, ctx:RubyParser.All_resultContext):
        pass


    # Enter a parse tree produced by RubyParser#cond_expression.
    def enterCond_expression(self, ctx:RubyParser.Cond_expressionContext):
        pass

    # Exit a parse tree produced by RubyParser#cond_expression.
    def exitCond_expression(self, ctx:RubyParser.Cond_expressionContext):
        pass


    # Enter a parse tree produced by RubyParser#if_statement.
    def enterIf_statement(self, ctx:RubyParser.If_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#if_statement.
    def exitIf_statement(self, ctx:RubyParser.If_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#elsif_clause.
    def enterElsif_clause(self, ctx:RubyParser.Elsif_clauseContext):
        pass

    # Exit a parse tree produced by RubyParser#elsif_clause.
    def exitElsif_clause(self, ctx:RubyParser.Elsif_clauseContext):
        pass


    # Enter a parse tree produced by RubyParser#else_clause.
    def enterElse_clause(self, ctx:RubyParser.Else_clauseContext):
        pass

    # Exit a parse tree produced by RubyParser#else_clause.
    def exitElse_clause(self, ctx:RubyParser.Else_clauseContext):
        pass


    # Enter a parse tree produced by RubyParser#while_statement.
    def enterWhile_statement(self, ctx:RubyParser.While_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#while_statement.
    def exitWhile_statement(self, ctx:RubyParser.While_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#for_statement.
    def enterFor_statement(self, ctx:RubyParser.For_statementContext):
        pass

    # Exit a parse tree produced by RubyParser#for_statement.
    def exitFor_statement(self, ctx:RubyParser.For_statementContext):
        pass


    # Enter a parse tree produced by RubyParser#all_assignment.
    def enterAll_assignment(self, ctx:RubyParser.All_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#all_assignment.
    def exitAll_assignment(self, ctx:RubyParser.All_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#statement_body.
    def enterStatement_body(self, ctx:RubyParser.Statement_bodyContext):
        pass

    # Exit a parse tree produced by RubyParser#statement_body.
    def exitStatement_body(self, ctx:RubyParser.Statement_bodyContext):
        pass


    # Enter a parse tree produced by RubyParser#statement_expression_list.
    def enterStatement_expression_list(self, ctx:RubyParser.Statement_expression_listContext):
        pass

    # Exit a parse tree produced by RubyParser#statement_expression_list.
    def exitStatement_expression_list(self, ctx:RubyParser.Statement_expression_listContext):
        pass


    # Enter a parse tree produced by RubyParser#assignment.
    def enterAssignment(self, ctx:RubyParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#assignment.
    def exitAssignment(self, ctx:RubyParser.AssignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#instance_variable_assignment.
    def enterInstance_variable_assignment(self, ctx:RubyParser.Instance_variable_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#instance_variable_assignment.
    def exitInstance_variable_assignment(self, ctx:RubyParser.Instance_variable_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#dynamic_assignment.
    def enterDynamic_assignment(self, ctx:RubyParser.Dynamic_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#dynamic_assignment.
    def exitDynamic_assignment(self, ctx:RubyParser.Dynamic_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#initial_array_assignment.
    def enterInitial_array_assignment(self, ctx:RubyParser.Initial_array_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#initial_array_assignment.
    def exitInitial_array_assignment(self, ctx:RubyParser.Initial_array_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#array_assignment.
    def enterArray_assignment(self, ctx:RubyParser.Array_assignmentContext):
        pass

    # Exit a parse tree produced by RubyParser#array_assignment.
    def exitArray_assignment(self, ctx:RubyParser.Array_assignmentContext):
        pass


    # Enter a parse tree produced by RubyParser#array_definition.
    def enterArray_definition(self, ctx:RubyParser.Array_definitionContext):
        pass

    # Exit a parse tree produced by RubyParser#array_definition.
    def exitArray_definition(self, ctx:RubyParser.Array_definitionContext):
        pass


    # Enter a parse tree produced by RubyParser#array_definition_elements.
    def enterArray_definition_elements(self, ctx:RubyParser.Array_definition_elementsContext):
        pass

    # Exit a parse tree produced by RubyParser#array_definition_elements.
    def exitArray_definition_elements(self, ctx:RubyParser.Array_definition_elementsContext):
        pass


    # Enter a parse tree produced by RubyParser#array_selector.
    def enterArray_selector(self, ctx:RubyParser.Array_selectorContext):
        pass

    # Exit a parse tree produced by RubyParser#array_selector.
    def exitArray_selector(self, ctx:RubyParser.Array_selectorContext):
        pass


    # Enter a parse tree produced by RubyParser#dynamic_result.
    def enterDynamic_result(self, ctx:RubyParser.Dynamic_resultContext):
        pass

    # Exit a parse tree produced by RubyParser#dynamic_result.
    def exitDynamic_result(self, ctx:RubyParser.Dynamic_resultContext):
        pass


    # Enter a parse tree produced by RubyParser#dynamic_.
    def enterDynamic_(self, ctx:RubyParser.Dynamic_Context):
        pass

    # Exit a parse tree produced by RubyParser#dynamic_.
    def exitDynamic_(self, ctx:RubyParser.Dynamic_Context):
        pass


    # Enter a parse tree produced by RubyParser#comparison.
    def enterComparison(self, ctx:RubyParser.ComparisonContext):
        pass

    # Exit a parse tree produced by RubyParser#comparison.
    def exitComparison(self, ctx:RubyParser.ComparisonContext):
        pass


    # Enter a parse tree produced by RubyParser#comp_var.
    def enterComp_var(self, ctx:RubyParser.Comp_varContext):
        pass

    # Exit a parse tree produced by RubyParser#comp_var.
    def exitComp_var(self, ctx:RubyParser.Comp_varContext):
        pass


    # Enter a parse tree produced by RubyParser#lvalue.
    def enterLvalue(self, ctx:RubyParser.LvalueContext):
        pass

    # Exit a parse tree produced by RubyParser#lvalue.
    def exitLvalue(self, ctx:RubyParser.LvalueContext):
        pass


    # Enter a parse tree produced by RubyParser#rvalue.
    def enterRvalue(self, ctx:RubyParser.RvalueContext):
        pass

    # Exit a parse tree produced by RubyParser#rvalue.
    def exitRvalue(self, ctx:RubyParser.RvalueContext):
        pass


    # Enter a parse tree produced by RubyParser#break_expression.
    def enterBreak_expression(self, ctx:RubyParser.Break_expressionContext):
        pass

    # Exit a parse tree produced by RubyParser#break_expression.
    def exitBreak_expression(self, ctx:RubyParser.Break_expressionContext):
        pass


    # Enter a parse tree produced by RubyParser#str_t.
    def enterStr_t(self, ctx:RubyParser.Str_tContext):
        pass

    # Exit a parse tree produced by RubyParser#str_t.
    def exitStr_t(self, ctx:RubyParser.Str_tContext):
        pass


    # Enter a parse tree produced by RubyParser#float_t.
    def enterFloat_t(self, ctx:RubyParser.Float_tContext):
        pass

    # Exit a parse tree produced by RubyParser#float_t.
    def exitFloat_t(self, ctx:RubyParser.Float_tContext):
        pass


    # Enter a parse tree produced by RubyParser#int_t.
    def enterInt_t(self, ctx:RubyParser.Int_tContext):
        pass

    # Exit a parse tree produced by RubyParser#int_t.
    def exitInt_t(self, ctx:RubyParser.Int_tContext):
        pass


    # Enter a parse tree produced by RubyParser#bool_t.
    def enterBool_t(self, ctx:RubyParser.Bool_tContext):
        pass

    # Exit a parse tree produced by RubyParser#bool_t.
    def exitBool_t(self, ctx:RubyParser.Bool_tContext):
        pass


    # Enter a parse tree produced by RubyParser#nil_t.
    def enterNil_t(self, ctx:RubyParser.Nil_tContext):
        pass

    # Exit a parse tree produced by RubyParser#nil_t.
    def exitNil_t(self, ctx:RubyParser.Nil_tContext):
        pass


    # Enter a parse tree produced by RubyParser#id_.
    def enterId_(self, ctx:RubyParser.Id_Context):
        pass

    # Exit a parse tree produced by RubyParser#id_.
    def exitId_(self, ctx:RubyParser.Id_Context):
        pass


    # Enter a parse tree produced by RubyParser#id_global.
    def enterId_global(self, ctx:RubyParser.Id_globalContext):
        pass

    # Exit a parse tree produced by RubyParser#id_global.
    def exitId_global(self, ctx:RubyParser.Id_globalContext):
        pass


    # Enter a parse tree produced by RubyParser#id_method.
    def enterId_method(self, ctx:RubyParser.Id_methodContext):
        pass

    # Exit a parse tree produced by RubyParser#id_method.
    def exitId_method(self, ctx:RubyParser.Id_methodContext):
        pass


    # Enter a parse tree produced by RubyParser#terminator.
    def enterTerminator(self, ctx:RubyParser.TerminatorContext):
        pass

    # Exit a parse tree produced by RubyParser#terminator.
    def exitTerminator(self, ctx:RubyParser.TerminatorContext):
        pass


    # Enter a parse tree produced by RubyParser#else_token.
    def enterElse_token(self, ctx:RubyParser.Else_tokenContext):
        pass

    # Exit a parse tree produced by RubyParser#else_token.
    def exitElse_token(self, ctx:RubyParser.Else_tokenContext):
        pass


    # Enter a parse tree produced by RubyParser#crlf.
    def enterCrlf(self, ctx:RubyParser.CrlfContext):
        pass

    # Exit a parse tree produced by RubyParser#crlf.
    def exitCrlf(self, ctx:RubyParser.CrlfContext):
        pass


    # Enter a parse tree produced by RubyParser#instance_var.
    def enterInstance_var(self, ctx:RubyParser.Instance_varContext):
        pass

    # Exit a parse tree produced by RubyParser#instance_var.
    def exitInstance_var(self, ctx:RubyParser.Instance_varContext):
        pass


    # Enter a parse tree produced by RubyParser#modif.
    def enterModif(self, ctx:RubyParser.ModifContext):
        pass

    # Exit a parse tree produced by RubyParser#modif.
    def exitModif(self, ctx:RubyParser.ModifContext):
        pass


    # Enter a parse tree produced by RubyParser#dots.
    def enterDots(self, ctx:RubyParser.DotsContext):
        pass

    # Exit a parse tree produced by RubyParser#dots.
    def exitDots(self, ctx:RubyParser.DotsContext):
        pass


    # Enter a parse tree produced by RubyParser#primary.
    def enterPrimary(self, ctx:RubyParser.PrimaryContext):
        pass

    # Exit a parse tree produced by RubyParser#primary.
    def exitPrimary(self, ctx:RubyParser.PrimaryContext):
        pass


    # Enter a parse tree produced by RubyParser#inpterp.
    def enterInpterp(self, ctx:RubyParser.InpterpContext):
        pass

    # Exit a parse tree produced by RubyParser#inpterp.
    def exitInpterp(self, ctx:RubyParser.InpterpContext):
        pass


