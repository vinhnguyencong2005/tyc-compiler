"""
AST Generation module for TyC programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.TyCVisitor import TyCVisitor
from build.TyCParser import TyCParser
from src.utils.nodes import *


class ASTGeneration(TyCVisitor):
    """AST Generation visitor for TyC language."""
    def visitProgram(self, ctx: TyCParser.ProgramContext):
        return Program([self.visit(ctx.getChild(i)) for i in range(ctx.getChildCount() - 1)])
    
    # ========== Struct ==========
    def visitStructDecl(self, ctx: TyCParser.StructDeclContext):
        name = ctx.ID().getText()
        body = self.visit(ctx.structBody())
        return StructDecl(name, body)
    
    def visitStructBody(self, ctx: TyCParser.StructBodyContext):
        return self.visit(ctx.structMems())
    
    def visitStructMems(self, ctx: TyCParser.StructMemsContext):
        return [self.visit(mem_ctx) for mem_ctx in ctx.structMemDecl()]
    
    def visitStructMemDecl(self, ctx: TyCParser.StructMemDeclContext):
        member_type = self.visit(ctx.explicitType())
        member_name = ctx.ID().getText()
        return MemberDecl(member_type, member_name)

    # ========== Function ==========
    def visitFuncDecl(self, ctx: TyCParser.FuncDeclContext):
        return_type = None
        if ctx.returnType():
            return_type = self.visit(ctx.returnType())
        
        name = ctx.ID().getText()

        params = []
        if ctx.paramList():
            params = self.visit(ctx.paramList())

        body = self.visit(ctx.innerBody())
        return FuncDecl(return_type, name, params, body)
    
    def visitParamList(self, ctx: TyCParser.ParamListContext):
        return [self.visit(param_ctx) for param_ctx in ctx.param()]
    
    def visitParam(self, ctx: TyCParser.ParamContext):
        """param: explicitType ID;"""
        param_type = self.visit(ctx.explicitType())
        param_name = ctx.ID().getText()
        return Param(param_type, param_name)
    
    # ========== Statements ==========
    def visitInnerBody(self, ctx: TyCParser.InnerBodyContext):
        """innerBody: blockStmt | stmt;"""
        return self.visit(ctx.getChild(0))

    def visitBlockStmt(self, ctx:TyCParser.BlockStmtContext):
        """blockStmt: LB stmtList RB | stmt;"""
        return BlockStmt(self.visit(ctx.stmtList())) if ctx.stmtList() else BlockStmt([self.visit(ctx.stmt())])

    # Visit a parse tree produced by TyCParser#stmtList.
    def visitStmtList(self, ctx:TyCParser.StmtListContext):
        """stmtList: stmt*;"""
        return [self.visit(stmt_ctx) for stmt_ctx in ctx.stmt()]

    # Visit a parse tree produced by TyCParser#stmt.
    def visitStmt(self, ctx:TyCParser.StmtContext):
        return self.visit(ctx.getChild(0))


    # Visit a parse tree produced by TyCParser#assignStmt.
    def visitAssignStmt(self, ctx:TyCParser.AssignStmtContext):
        """assignStmt: assignStmt_ SEMICOLON;"""
        return ExprStmt(self.visit(ctx.assignStmt_()))


    # Visit a parse tree produced by TyCParser#assignStmt_.
    def visitAssignStmt_(self, ctx:TyCParser.AssignStmt_Context):
        """assignStmt_: lvalue ASSIGN expr;"""
        return AssignExpr(self.visit(ctx.lvalue()), self.visit(ctx.expr()))


    # Visit a parse tree produced by TyCParser#lvalue.
    def visitLvalue(self, ctx:TyCParser.LvalueContext):
        ids = [tok.getText() for tok in ctx.ID()]
        node = Identifier(ids[0])
        for name in ids[1:]:
            node = MemberAccess(node, name)
        return node

    # Visit a parse tree produced by TyCParser#ifStmt.
    def visitIfStmt(self, ctx:TyCParser.IfStmtContext):
        """ifStmt: IF conditions innerBody (ELSE innerBody)?;"""
        condition = self.visit(ctx.conditions())
        then_branch = self.visit(ctx.innerBody(0))
        else_branch = self.visit(ctx.innerBody(1)) if ctx.ELSE() else None
        return IfStmt(condition, then_branch, else_branch)


    # Visit a parse tree produced by TyCParser#whileStmt.
    def visitWhileStmt(self, ctx:TyCParser.WhileStmtContext):
        """whileStmt: WHILE conditions innerBody;"""
        return WhileStmt(self.visit(ctx.conditions()), self.visit(ctx.innerBody()))


    # Visit a parse tree produced by TyCParser#forStmt.
    def visitForStmt(self, ctx:TyCParser.ForStmtContext):
        """forStmt: FOR forHeader innerBody;"""
        init, conditions, update = self.visit(ctx.forHeader())
        body = self.visit(ctx.innerBody())
        return ForStmt(init, conditions, update, body)

    # Visit a parse tree produced by TyCParser#forHeader.
    def visitForHeader(self, ctx:TyCParser.ForHeaderContext):
        """forHeader: LP forOne forTwo forThree RP;"""
        return self.visit(ctx.forOne()), self.visit(ctx.forTwo()), self.visit(ctx.forThree())


    # Visit a parse tree produced by TyCParser#forOne.
    def visitForOne(self, ctx:TyCParser.ForOneContext):
        """forOne: forInit? SEMICOLON;"""
        return self.visit(ctx.forInit()) if ctx.forInit() else None

    # Visit a parse tree produced by TyCParser#forInit.
    def visitForInit(self, ctx:TyCParser.ForInitContext):
        """forInit: variableType? ID ASSIGN expr;"""
        id = ctx.ID().getText()
        if ctx.variableType():
            return VarDecl(self.visit(ctx.variableType()), id, self.visit(ctx.expr()))
        return ExprStmt(AssignExpr(Identifier(id), self.visit(ctx.expr())))

    # Visit a parse tree produced by TyCParser#forTwo.
    def visitForTwo(self, ctx:TyCParser.ForTwoContext):
        """forTwo: expr? SEMICOLON;"""
        return self.visit(ctx.expr()) if ctx.expr() else None


    # Visit a parse tree produced by TyCParser#forThree.
    def visitForThree(self, ctx:TyCParser.ForThreeContext):
        """forThree
                    : (assignStmt_
                    | ID INCREMENT
                    | ID DECREMENT
                    | DECREMENT ID
                    | INCREMENT ID)?;"""
        if ctx.assignStmt_():
            return self.visit(ctx.assignStmt_())
        
        if ctx.getChildCount() == 0:
            return None
        
        first = ctx.getChild(0).getText()
        second = ctx.getChild(1).getText()

        if first in ("++", "--"):
            return PrefixOp(first, Identifier(second))
        return PostfixOp(second, Identifier(first))


    # Visit a parse tree produced by TyCParser#returnStmt.
    def visitReturnStmt(self, ctx:TyCParser.ReturnStmtContext):
        """returnStmt: RETURN expr? SEMICOLON;"""
        return ReturnStmt(self.visit(ctx.expr()) if ctx.expr() else None)


    # Visit a parse tree produced by TyCParser#breakStmt.
    def visitBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        """breakStmt: BREAK SEMICOLON;"""
        return BreakStmt()


    # Visit a parse tree produced by TyCParser#continueStmt.
    def visitContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        """continueStmt: CONTINUE SEMICOLON;"""
        return ContinueStmt()


    # Visit a parse tree produced by TyCParser#switchStmt.
    def visitSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        """switchStmt: SWITCH LP expr RP LB switchBody RB;"""
        case_clauses, default_clause = self.visit(ctx.switchBody())
        return SwitchStmt(self.visit(ctx.expr()), case_clauses, default_clause)



    # Visit a parse tree produced by TyCParser#switchBody.
    def visitSwitchBody(self, ctx:TyCParser.SwitchBodyContext):
        """switchBody: caseClause* defaultClause?;"""
        case_clauses = [self.visit(case_ctx) for case_ctx in ctx.caseClause()]
        default_clause = self.visit(ctx.defaultClause()) if ctx.defaultClause() else None
        return case_clauses, default_clause


    # Visit a parse tree produced by TyCParser#caseClause.
    def visitCaseClause(self, ctx:TyCParser.CaseClauseContext):
        """caseClause: CASE expr COLON stmtList;"""
        return CaseStmt(self.visit(ctx.expr()), self.visit(ctx.stmtList()))


    # Visit a parse tree produced by TyCParser#defaultClause.
    def visitDefaultClause(self, ctx:TyCParser.DefaultClauseContext):
        """defaultClause: DEFAULT COLON stmtList;"""
        return DefaultStmt(self.visit(ctx.stmtList()))


    # Visit a parse tree produced by TyCParser#conditions.
    def visitConditions(self, ctx:TyCParser.ConditionsContext):
        """conditions: LP expr RP;"""
        return self.visit(ctx.expr())


    # Visit a parse tree produced by TyCParser#exprStmt.
    def visitExprStmt(self, ctx:TyCParser.ExprStmtContext):
        return ExprStmt(self.visit(ctx.expr()))


    # Visit a parse tree produced by TyCParser#expr.
    def visitExpr(self, ctx:TyCParser.ExprContext):
        """expr: assignmentExpr;"""
        return self.visit(ctx.assignmentExpr())


    # Visit a parse tree produced by TyCParser#assignmentExpr.
    def visitAssignmentExpr(self, ctx:TyCParser.AssignmentExprContext):
        """assignmentExpr: lvalue ASSIGN assignmentExpr | logicalOrExpr;"""
        if ctx.ASSIGN():
            return AssignExpr(self.visit(ctx.lvalue()), self.visit(ctx.assignmentExpr()))
        return self.visit(ctx.logicalOrExpr())


    # Visit a parse tree produced by TyCParser#logicalOrExpr.
    def visitLogicalOrExpr(self, ctx:TyCParser.LogicalOrExprContext):
        """logicalOrExpr: logicalAndExpr (LOGICAL_OR logicalAndExpr)*;"""
        return reduce(lambda x, y: BinaryOp(x, y[0].getText(), self.visit(y[1])), zip(ctx.LOGICAL_OR(), ctx.logicalAndExpr()[1:]), self.visit(ctx.logicalAndExpr(0)))



    # Visit a parse tree produced by TyCParser#logicalAndExpr.
    def visitLogicalAndExpr(self, ctx:TyCParser.LogicalAndExprContext):
        """logicalAndExpr: equalityExpr (LOGICAL_AND equalityExpr)*;"""
        return reduce(lambda x, y: BinaryOp(x, y[0].getText(), self.visit(y[1])), zip(ctx.LOGICAL_AND(), ctx.equalityExpr()[1:]), self.visit(ctx.equalityExpr(0)))

    # Visit a parse tree produced by TyCParser#equalityExpr.
    def visitEqualityExpr(self, ctx:TyCParser.EqualityExprContext):
        """equalityExpr: relationalExpr (equalityRelation relationalExpr)*;"""
        return reduce(lambda x, y: BinaryOp(x, y[0].getText(), self.visit(y[1])), zip(ctx.equalityRelation(), ctx.relationalExpr()[1:]), self.visit(ctx.relationalExpr(0)))

    # Visit a parse tree produced by TyCParser#equalityRelation.
    def visitEqualityRelation(self, ctx:TyCParser.EqualityRelationContext):
        """equalityRelation: EQUAL | NOT_EQUAL;"""
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by TyCParser#relationalExpr.
    def visitRelationalExpr(self, ctx:TyCParser.RelationalExprContext):
        """relationalExpr: additiveExpr (orderingRelation additiveExpr)*;"""
        return reduce(lambda x, y: BinaryOp(x, y[0].getText(), self.visit(y[1])), zip(ctx.orderingRelation(), ctx.additiveExpr()[1:]), self.visit(ctx.additiveExpr(0)))

    # Visit a parse tree produced by TyCParser#orderingRelation.
    def visitOrderingRelation(self, ctx:TyCParser.OrderingRelationContext):
        """orderingRelation: LESS_THAN | GREATER_THAN | LESS_EQUAL | GREATER_EQUAL;"""
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by TyCParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:TyCParser.AdditiveExprContext):
        """additiveExpr: multiplicativeExpr ((PLUS | MINUS) multiplicativeExpr)*;"""
        ops = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount(), 2)]
        return reduce(lambda x, y: BinaryOp(x, y[0], self.visit(y[1])), zip(ops, ctx.multiplicativeExpr()[1:]), self.visit(ctx.multiplicativeExpr(0)))


    # Visit a parse tree produced by TyCParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:TyCParser.MultiplicativeExprContext):
        """multiplicativeExpr: unaryExpr ((MUL | DIV | MOD) unaryExpr)*;"""
        ops = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount(), 2)]
        return reduce(lambda x, y: BinaryOp(x, y[0], self.visit(y[1])), zip(ops, ctx.unaryExpr()[1:]), self.visit(ctx.unaryExpr(0)))


    # Visit a parse tree produced by TyCParser#unaryExpr.
    def visitUnaryExpr(self, ctx:TyCParser.UnaryExprContext):
        """unaryExpr
                    : LOGICAL_NOT unaryExpr
                    | INCREMENT unaryExpr
                    | DECREMENT unaryExpr
                    | PLUS unaryExpr
                    | MINUS unaryExpr
                    | postfixExpr
                    ;"""
        if ctx.postfixExpr():
            return self.visit(ctx.postfixExpr())
        
        op = ctx.getChild(0).getText()
        return PrefixOp(op, self.visit(ctx.unaryExpr()))


    # Visit a parse tree produced by TyCParser#postfixExpr.
    def visitPostfixExpr(self, ctx:TyCParser.PostfixExprContext):
        """postfixExpr: memberAccessExpr (INCREMENT | DECREMENT)*;"""
        ops = [ctx.getChild(i).getText() for i in range(1, ctx.getChildCount()) if ctx.getChild(i).getText() in ("++", "--")]
        return reduce(lambda x, op: PostfixOp(op, x), ops, self.visit(ctx.memberAccessExpr()))

    # Visit a parse tree produced by TyCParser#memberAccessExpr.
    def visitMemberAccessExpr(self, ctx:TyCParser.MemberAccessExprContext):
        """memberAccessExpr: primaryExpr (DOT ID)*;"""
        base = self.visit(ctx.primaryExpr())
        member_names = [ctx.getChild(i).getText() for i in range(2, ctx.getChildCount(), 2)]
        return reduce(lambda x, y: MemberAccess(x, y), member_names, base)

    # Visit a parse tree produced by TyCParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:TyCParser.PrimaryExprContext):
        """primaryExpr
                    : INTLIT
                    | FLOATLIT
                    | STRING_LIT
                    | ID
                    | LP expr RP
                    | functionCall
                    | structLiteral
                    ;"""
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.ID():
            return Identifier(ctx.ID().getText())
        elif ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        else:
            return self.visit(ctx.structLiteral())


    # Visit a parse tree produced by TyCParser#structLiteral.
    def visitStructLiteral(self, ctx:TyCParser.StructLiteralContext):
        """structLiteral: LB (expr (COMMA expr)*)? RB;"""
        return StructLiteral([self.visit(x) for x in ctx.expr()])

    # Visit a parse tree produced by TyCParser#functionCall.
    def visitFunctionCall(self, ctx:TyCParser.FunctionCallContext):
        """functionCall: ID LP (expr (COMMA expr)*)? RP;"""
        func_name = ctx.ID().getText()
        args = [self.visit(x) for x in ctx.expr()]
        return FuncCall(func_name, args)

    # Visit a parse tree produced by TyCParser#varDecl.
    def visitVarDecl(self, ctx:TyCParser.VarDeclContext):
        """varDecl: variableType ID (ASSIGN expr)? SEMICOLON;"""
        var_type = self.visit(ctx.variableType())
        var_name = ctx.ID().getText()
        init_expr = self.visit(ctx.expr()) if ctx.expr() else None
        return VarDecl(var_type, var_name, init_expr)


    # Visit a parse tree produced by TyCParser#variableType.
    def visitVariableType(self, ctx:TyCParser.VariableTypeContext):
        """variableType: explicitType | AUTO;"""
        return self.visit(ctx.explicitType()) if ctx.explicitType() else None


    # Visit a parse tree produced by TyCParser#returnType.
    def visitReturnType(self, ctx:TyCParser.ReturnTypeContext):
        """returnType: explicitType | VOID;"""
        return self.visit(ctx.explicitType()) if ctx.explicitType() else VoidType()


    # Visit a parse tree produced by TyCParser#explicitType.
    def visitExplicitType(self, ctx:TyCParser.ExplicitTypeContext):
        """explicitType: primitiveType | structType;"""
        return self.visit(ctx.primitiveType()) if ctx.primitiveType() else StructType(ctx.structType().getText())


    # Visit a parse tree produced by TyCParser#structType.
    def visitStructType(self, ctx:TyCParser.StructTypeContext):
        """structType: ID;"""
        return StructType(ctx.ID().getText())


    # Visit a parse tree produced by TyCParser#primitiveType.
    def visitPrimitiveType(self, ctx:TyCParser.PrimitiveTypeContext):
        """primitiveType: INT | FLOAT | STRING;"""
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        else:
            return StringType()