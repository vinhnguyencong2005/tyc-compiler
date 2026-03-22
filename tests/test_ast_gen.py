"""
AST Generation test cases for TyC compiler.
TODO: Implement 100 test cases for AST generation
"""

import pytest
from tests.utils import ASTGenerator


def test_ast_gen_placeholder():
    """1. Program test"""
    source = """
    void main() {
        int a = 3;
    }

    struct Animal{
        int x;
        int y;
        int z;
    };

    int call() {
        float a;
    }
    """
    # TODO: Add actual test assertions
    # Example:
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a = IntLiteral(3))]), StructDecl(Animal, [MemberDecl(IntType(), x), MemberDecl(IntType(), y), MemberDecl(IntType(), z)]), FuncDecl(IntType(), call, [], [VarDecl(FloatType(), a)])])"
    # expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a = IntLiteral(3))]), StructDecl(Animal, [MemberDecl(IntType(), x), MemberDecl(IntType(), y), MemberDecl(IntType(), z)]), FuncDecl(IntType(), call, [], [VarDecl(FloatType(), a)]))]"
    assert str(ASTGenerator(source).generate()) == expected
    # assert True

def test_ast_gen_empty():
    """2. Empty program test"""
    source = ""
    expected = "Program([])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_struct():
    """3. Struct declaration test"""
    source = """
    struct Point {
        int x;
        int y;
    };
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_struct_2():
    """4. Struct declare with empty body test"""
    source = """
    struct Empty {
    };
    """
    expected = "Program([StructDecl(Empty, [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_ast_struct_3():
    """5. Struct declare with multiple members test"""
    source = """
    struct Person {
        string name;
        int age;
        float height;
        Point location;
    };
    """
    expected = "Program([StructDecl(Person, [MemberDecl(StringType(), name), MemberDecl(IntType(), age), MemberDecl(FloatType(), height), MemberDecl(StructType(Point), location)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_multiple_structs():
    """6. Multiple struct declarations test"""
    source = """
    struct Point {
        int x;
        int y;
    };

    struct Circle {
        Point center;
        float radius;
    };
    """
    expected = "Program([StructDecl(Point, [MemberDecl(IntType(), x), MemberDecl(IntType(), y)]), StructDecl(Circle, [MemberDecl(StructType(Point), center), MemberDecl(FloatType(), radius)])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration():
    """7. Function declaration test"""
    source = """
    int add() {
    }
    """
    expected = "Program([FuncDecl(IntType(), add, [], [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_params():
    """8. Function declaration with parameters test"""
    source = """
    float multiply(int a, float b) {
    }
    """
    expected = "Program([FuncDecl(FloatType(), multiply, [Param(IntType(), a), Param(FloatType(), b)], [])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_body():
    """9. Function declaration with body test"""
    source = """
    void greet(int a, string name) {
        string message = "Hello, " + name + "!";
    }
    """
    expected = "Program([FuncDecl(VoidType(), greet, [Param(IntType(), a), Param(StringType(), name)], [VarDecl(StringType(), message = BinaryOp(BinaryOp(StringLiteral('Hello, '), +, Identifier(name)), +, StringLiteral('!')))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_return():
    """10. Function declaration with return statement test"""
    source = """
    int square(int x) {
        return x * x;
    }
    """
    expected = "Program([FuncDecl(IntType(), square, [Param(IntType(), x)], [ReturnStmt(return BinaryOp(Identifier(x), *, Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_expr():
    """11. Function declaration with expression test"""
    source = """
    int add(int a, int b) {
        return a + b;
    }
    """
    expected = "Program([FuncDecl(IntType(), add, [Param(IntType(), a), Param(IntType(), b)], [ReturnStmt(return BinaryOp(Identifier(a), +, Identifier(b)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_int():
    """12. Function declaration with integer return type test"""
    source = """
    Point get_value() {
        return 42;
    }
    """
    expected = "Program([FuncDecl(StructType(Point), get_value, [], [ReturnStmt(return IntLiteral(42))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_float():
    """13. Function declaration with float return type test"""
    source = """
    float get_pi() {
        return 3.14;
    }
    """
    expected = "Program([FuncDecl(FloatType(), get_pi, [], [ReturnStmt(return FloatLiteral(3.14))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_negative():
    """14. Function declaration with negative integer return type test"""
    source = """
    int get_negative_value() {
        return -42;
    }
    """
    expected = "Program([FuncDecl(IntType(), get_negative_value, [], [ReturnStmt(return PrefixOp(-IntLiteral(42)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_string():
    """15. Function declaration with string return type test"""
    source = """
    string get_greeting() {
        return "Hello, World!";
    }
    """
    expected = "Program([FuncDecl(StringType(), get_greeting, [], [ReturnStmt(return StringLiteral('Hello, World!'))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_struct():
    """16. Function declaration with struct return type test"""
    source = """
    Point get_origin() {
        Point p;
        p.x = 0;
        p.y = 0;
        return p;
    }
    """
    expected = "Program([FuncDecl(StructType(Point), get_origin, [], [VarDecl(StructType(Point), p), ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = IntLiteral(0))), ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = IntLiteral(0))), ReturnStmt(return Identifier(p))])])"
    assert str(ASTGenerator(source).generate()) == expected
    
def test_function_declaration_with_struct_2():
    """17. Function declaration with struct return type and initialization test"""
    source = """
    Point create_point(int x, int y) {
        Point a = {x, y};
        return a;
    }
    """
    expected = "Program([FuncDecl(StructType(Point), create_point, [Param(IntType(), x), Param(IntType(), y)], [VarDecl(StructType(Point), a = StructLiteral({Identifier(x), Identifier(y)})), ReturnStmt(return Identifier(a))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_struct_3():
    """18. Function declaration with struct return type and member access test"""
    source = """
    int get_x(Point p) {
        return p.x;
    }
    """
    expected = "Program([FuncDecl(IntType(), get_x, [Param(StructType(Point), p)], [ReturnStmt(return MemberAccess(Identifier(p).x))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_if():
    """19. Function declaration with if statement test"""
    source = """
    int max(int a, int b) {
        if (a > b) {
            return a;
        }
        return b;
    }
    """
    expected = "Program([FuncDecl(IntType(), max, [Param(IntType(), a), Param(IntType(), b)], [IfStmt(if BinaryOp(Identifier(a), >, Identifier(b)) then BlockStmt([ReturnStmt(return Identifier(a))])), ReturnStmt(return Identifier(b))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_if_else():
    """20. Function declaration with if-else statement test"""
    source = """
    int min(int a, int b) {
        if (a < b) {
            return a;
        } else {
            return b;
        }
    }
    """
    expected = "Program([FuncDecl(IntType(), min, [Param(IntType(), a), Param(IntType(), b)], [IfStmt(if BinaryOp(Identifier(a), <, Identifier(b)) then BlockStmt([ReturnStmt(return Identifier(a))]), else BlockStmt([ReturnStmt(return Identifier(b))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_nested_if():
    """21. Function declaration with nested if statement test"""
    source = """
    int compare(int a, int b) {
        if (a > b) {
            if (a > 0) {
                return 1;
            } else {
                return 0;
            }
            return 1;
        } else {
            return 0;
        }
    }
    """
    expected = "Program([FuncDecl(IntType(), compare, [Param(IntType(), a), Param(IntType(), b)], [IfStmt(if BinaryOp(Identifier(a), >, Identifier(b)) then BlockStmt([IfStmt(if BinaryOp(Identifier(a), >, IntLiteral(0)) then BlockStmt([ReturnStmt(return IntLiteral(1))]), else BlockStmt([ReturnStmt(return IntLiteral(0))])), ReturnStmt(return IntLiteral(1))]), else BlockStmt([ReturnStmt(return IntLiteral(0))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_while():
    """22. Function declaration with while loop test"""
    source = """
    void count_down(int n) {
        while (n > 0) {
            n = n - 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_down, [Param(IntType(), n)], [WhileStmt(while BinaryOp(Identifier(n), >, IntLiteral(0)) do BlockStmt([ExprStmt(AssignExpr(Identifier(n) = BinaryOp(Identifier(n), -, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_declaration_with_while_2():
    """23. Function declaration with while loop and if statement test"""
    source = """
    void count_down(int n) {
        while (n > 0) {
            if (n % 2 == 0) {
                n = n - 2;
            } else {
                n = n - 1;
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_down, [Param(IntType(), n)], [WhileStmt(while BinaryOp(Identifier(n), >, IntLiteral(0)) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(n), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([ExprStmt(AssignExpr(Identifier(n) = BinaryOp(Identifier(n), -, IntLiteral(2))))]), else BlockStmt([ExprStmt(AssignExpr(Identifier(n) = BinaryOp(Identifier(n), -, IntLiteral(1))))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_while_struct():
    """24. While loop with struct member access test"""
    source = """
    void move(Point p) {
        while (p.x < 10) {
            p.x = p.x + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), move, [Param(StructType(Point), p)], [WhileStmt(while BinaryOp(MemberAccess(Identifier(p).x), <, IntLiteral(10)) do BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = BinaryOp(MemberAccess(Identifier(p).x), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_while_struct_2():
    """25. While loop with struct member access and if statement test"""
    source = """
    void move(Point p) {
        while (p.x < 10) {
            if (p.y < 5) {
                p.y = p.y + 1;
            } else {
                p.y = p.y - 1;
            }
            p.x = p.x + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), move, [Param(StructType(Point), p)], [WhileStmt(while BinaryOp(MemberAccess(Identifier(p).x), <, IntLiteral(10)) do BlockStmt([IfStmt(if BinaryOp(MemberAccess(Identifier(p).y), <, IntLiteral(5)) then BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = BinaryOp(MemberAccess(Identifier(p).y), +, IntLiteral(1))))]), else BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = BinaryOp(MemberAccess(Identifier(p).y), -, IntLiteral(1))))])), ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = BinaryOp(MemberAccess(Identifier(p).x), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_while_struct_3():
    """26. While loop with struct member access and nested if statement test"""
    source = """
    void move(Point p) {
        while (p.x < 10) {
            if (p.y < 5) {
                if (p.z < 3) {
                    p.z = p.z + 1;
                } else {
                    p.z = p.z - 1;
                }
                p.y = p.y + 1;
            } else {
                p.y = p.y - 1;
            }
            p.x = p.x + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), move, [Param(StructType(Point), p)], [WhileStmt(while BinaryOp(MemberAccess(Identifier(p).x), <, IntLiteral(10)) do BlockStmt([IfStmt(if BinaryOp(MemberAccess(Identifier(p).y), <, IntLiteral(5)) then BlockStmt([IfStmt(if BinaryOp(MemberAccess(Identifier(p).z), <, IntLiteral(3)) then BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).z) = BinaryOp(MemberAccess(Identifier(p).z), +, IntLiteral(1))))]), else BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).z) = BinaryOp(MemberAccess(Identifier(p).z), -, IntLiteral(1))))])), ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = BinaryOp(MemberAccess(Identifier(p).y), +, IntLiteral(1))))]), else BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = BinaryOp(MemberAccess(Identifier(p).y), -, IntLiteral(1))))])), ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = BinaryOp(MemberAccess(Identifier(p).x), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop():
    """27. For loop test"""
    source = """
    void count_up(int n) {
        for (int i = 0; i < n; i = i + 1) {
            // do nothing
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [Param(IntType(), n)], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop_empty_header():
    """28. For loop with empty header test"""
    source = """
    void count_up() {
        for (;;) {
            // do nothing
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [], [ForStmt(for None; None; None do BlockStmt([]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop_with_if():
    """29. For loop with if statement test"""
    source = """
    void count_up(int n) {
        for (i = 0; i < n; i = i + 1) {
            if (i % 2 == 0) {
                // do nothing
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [Param(IntType(), n)], [ForStmt(for ExprStmt(AssignExpr(Identifier(i) = IntLiteral(0))); BinaryOp(Identifier(i), <, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop_with_nested_if():
    """30. For loop with nested if statement test"""
    source = """
    void count_up(int n) {
        for (int i = 0; i < n; i = i + 1) {
            if (i % 2 == 0) {
                if (i % 3 == 0) {
                    // do nothing
                }
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [Param(IntType(), n)], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(3)), ==, IntLiteral(0)) then BlockStmt([]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop_with_nested_if_else():
    """31. For loop with nested if-else statement test"""
    source = """
    void count_up(int n) {
        for (int i = 0; i < n; i = i + 1) {
            if (i % 2 == 0) {
                if (i % 3 == 0) {
                    // do nothing
                } else {
                    // do nothing
                }
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [Param(IntType(), n)], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(3)), ==, IntLiteral(0)) then BlockStmt([]), else BlockStmt([]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop_with_multiple_statements():
    """32. For loop with multiple statements in body test"""
    source = """
    void count_up(int n) {
        for (int i = 0; i < n; i = i + 1) {
            int square = i * i;
            // do nothing
        }
    }
    """
def test_for_loop_with_multiple_statements_2():
    """33. For loop with multiple statements in body and if statement test"""
    source = """
    void count_up(int n) {
        for (int i = 0; i < n; i = i + 1) {
            int square = i * i;
            if (square % 2 == 0) {
                // do nothing
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [Param(IntType(), n)], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([VarDecl(IntType(), square = BinaryOp(Identifier(i), *, Identifier(i))), IfStmt(if BinaryOp(BinaryOp(Identifier(square), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop_with_multiple_statements_3():
    """34. For loop with multiple statements in body, if statement and nested if statement test"""
    source = """
    void count_up(int n) {
        for (int i = 0; i < n; i = i + 1) {
            int square = i * i;
            if (square % 2 == 0) {
                if (square % 3 == 0) {
                    // do nothing
                }
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [Param(IntType(), n)], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([VarDecl(IntType(), square = BinaryOp(Identifier(i), *, Identifier(i))), IfStmt(if BinaryOp(BinaryOp(Identifier(square), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(square), %, IntLiteral(3)), ==, IntLiteral(0)) then BlockStmt([]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop_nested_for_loop():
    """35. For loop with nested for loop test"""
    source = """
    void count_up(int n) {
        for (int i = 0; i < n; i = i + 1) {
            for (int j = 0; j < i; j = j + 1) {
                // do nothing
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [Param(IntType(), n)], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ForStmt(for VarDecl(IntType(), j = IntLiteral(0)); BinaryOp(Identifier(j), <, Identifier(i)); AssignExpr(Identifier(j) = BinaryOp(Identifier(j), +, IntLiteral(1))) do BlockStmt([]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop_nested_if():
    """36. For loop nested inside if statement test"""
    source = """
    void count_up(int n) {
        if (n > 0) {
            for (int i = 0; i < n; i = i + 1) {
                // do nothing
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [Param(IntType(), n)], [IfStmt(if BinaryOp(Identifier(n), >, IntLiteral(0)) then BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_for_loop_nested_if_else():
    """37. For loop nested inside if-else statement test"""
    source = """
    void count_up(int n) {
        if (n > 0) {
            for (int i = 0; i < n; i = i + 1) {
                // do nothing
            }
        } else {
            for (int i = 0; i > n; i = i - 1) {
                // do nothing
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), count_up, [Param(IntType(), n)], [IfStmt(if BinaryOp(Identifier(n), >, IntLiteral(0)) then BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([]))]), else BlockStmt([ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), >, Identifier(n)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), -, IntLiteral(1))) do BlockStmt([]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_case():
    """38. Switch-case statement test"""
    source = """
    void test(int x) {
        switch (x) {
            case 1:
                // do nothing
                break;
            case 2:
                // do nothing
                break;
            default:
                // do nothing
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), test, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])], default DefaultStmt(default: []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_case_no_defalt():
    """39. Switch-case statement without default case test"""
    source = """
    void test(int x) {
        switch (x) {
            case 1:
                // do nothing
                break;
            case 2:
                // do nothing
                break;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), test, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_case_only_default():
    """40. Switch-case statement with only default case test"""
    source = """
    void test(int x) {
        switch (x) {
            default:
                // do nothing
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), test, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [], default DefaultStmt(default: []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_case_with_nested_if_else():
    """41. Switch-case statement with nested if-else statement test"""
    source = """
    void test(int x) {
        switch (x) {
            case 1:
                if (x > 0) {
                    // do nothing
                } else {
                    // do nothing
                }
                break;
            case 2:
                // do nothing
                break;
            default:
                // do nothing
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), test, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([]), else BlockStmt([])), BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])], default DefaultStmt(default: []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_case_with_nested_switch():
    """42. Switch-case statement with nested switch statement test"""
    source = """
    void test(int x) {
        switch (x) {
            case 1:
                switch (x) {
                    case 1:
                        // do nothing
                        break;
                    case 2:
                        // do nothing
                        break;
                    default:
                        // do nothing
                }
                break;
            case 2:
                // do nothing
                break;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), test, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])], default DefaultStmt(default: [])), BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_case_with_while():
    """43. Switch-case statement with while loop test"""
    source = """
    void test(int x) {
        switch (x) {
            case 1:
                while (x > 0) {
                    // do nothing
                }
                break;
            case 2:
                // do nothing
                break;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), test, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [WhileStmt(while BinaryOp(Identifier(x), >, IntLiteral(0)) do BlockStmt([])), BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_case_with_for():
    """44. Switch-case statement with for loop test"""
    source = """
    void test(int x) {
        switch (x) {
            case 1:
                for (int i = 0; i < x; i = i + 1) {
                    // do nothing
                }
                break;
            case 2:
                // do nothing
                break;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), test, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, Identifier(x)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([])), BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_case_with_function_call():
    """45. Switch-case statement with function call test"""
    source = """
    void test(int x) {
        switch (x) {
            case 1:
                foo();
                break;
            case 2:
                // do nothing
                break;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), test, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(FuncCall(foo, [])), BreakStmt()]), CaseStmt(case IntLiteral(2): [BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_switch_case_with_return():
    """46. Switch-case statement with return statement test"""
    source = """
    int test(int x) {
        switch (x) {
            case 1:
                return 1;
            case 2:
                return 2;
            default:
                return 0;
        }
    }
    """
    expected = "Program([FuncDecl(IntType(), test, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ReturnStmt(return IntLiteral(1))]), CaseStmt(case IntLiteral(2): [ReturnStmt(return IntLiteral(2))])], default DefaultStmt(default: [ReturnStmt(return IntLiteral(0))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_call():
    """47. Function call test"""
    source = """
    void main() {
        foo();
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(foo, []))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_call_with_args():
    """48. Function call with arguments test"""
    source = """
    void main() {
        foo(1, 2.0, "hello");
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(foo, [IntLiteral(1), FloatLiteral(2.0), StringLiteral('hello')]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_call_with_struct_arg():
    """49. Function call with struct argument test"""
    source = """
    void main() {
        Point p;
        foo(p);
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), ExprStmt(FuncCall(foo, [Identifier(p)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_call_with_nested_function_call():
    """50. Function call with nested function call test"""
    source = """
    void main() {
        foo(bar(1, 2), baz(3.0));
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(foo, [FuncCall(bar, [IntLiteral(1), IntLiteral(2)]), FuncCall(baz, [FloatLiteral(3.0)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_call_with_struct_arg_and_nested_function_call():
    """51. Function call with struct argument and nested function call test"""
    source = """
    void main() {
        Point p;
        foo(p, bar(1, 2));
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), ExprStmt(FuncCall(foo, [Identifier(p), FuncCall(bar, [IntLiteral(1), IntLiteral(2)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_function_call_with_args_and_nested_function_call():
    """52. Function call with arguments and nested function call test"""
    source = """
    void main() {
        foo(1, bar(2.0), "hello");
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(foo, [IntLiteral(1), FuncCall(bar, [FloatLiteral(2.0)]), StringLiteral('hello')]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_expression_with_function_call():
    """53. Expression with function call test"""
    source = """
    void main() {
        int x = foo(1, 2) + 3;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = BinaryOp(FuncCall(foo, [IntLiteral(1), IntLiteral(2)]), +, IntLiteral(3)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_expression_with_nested_function_call():
    """54. Expression with nested function call test"""
    source = """
    void main() {
        int x = foo(bar(1, 2), baz(3.0)) + 4;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = BinaryOp(FuncCall(foo, [FuncCall(bar, [IntLiteral(1), IntLiteral(2)]), FuncCall(baz, [FloatLiteral(3.0)])]), +, IntLiteral(4)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_expression_with_function_call_and_struct_arg():
    """55. Expression with function call and struct argument test"""
    source = """
    void main() {
        Point p;
        int x = foo(p) + 5;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), VarDecl(IntType(), x = BinaryOp(FuncCall(foo, [Identifier(p)]), +, IntLiteral(5)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_expression_with_function_call_and_nested_function_call():
    """56. Expression with function call and nested function call test"""
    source = """
    void main() {
        int x = foo(bar(1, 2)) + baz(3.0);
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = BinaryOp(FuncCall(foo, [FuncCall(bar, [IntLiteral(1), IntLiteral(2)])]), +, FuncCall(baz, [FloatLiteral(3.0)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_expression_with_function_call_and_nested_function_call_2():
    """57. Expression with function call and nested function call test 2"""
    source = """
    void main() {
        int x = foo(bar(1, 2) + baz(3.0)) + 6;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = BinaryOp(FuncCall(foo, [BinaryOp(FuncCall(bar, [IntLiteral(1), IntLiteral(2)]), +, FuncCall(baz, [FloatLiteral(3.0)]))]), +, IntLiteral(6)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_expression_with_function_call_and_nested_function_call_3():
    """58. Expression with function call and nested function call test 3"""
    source = """
    void main() {
        int x = foo(bar(1, 2) + baz(3.0) * qux(4)) + 7;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = BinaryOp(FuncCall(foo, [BinaryOp(FuncCall(bar, [IntLiteral(1), IntLiteral(2)]), +, BinaryOp(FuncCall(baz, [FloatLiteral(3.0)]), *, FuncCall(qux, [IntLiteral(4)])))]), +, IntLiteral(7)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_expression_with_function_call_and_nested_function_call_4():
    """59. Expression with function call and nested function call test 4"""
    source = """
    void main() {
        int x = foo(bar(1, 2) + baz(3.0) * qux(4) - quux(5)) + 8;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = BinaryOp(FuncCall(foo, [BinaryOp(BinaryOp(FuncCall(bar, [IntLiteral(1), IntLiteral(2)]), +, BinaryOp(FuncCall(baz, [FloatLiteral(3.0)]), *, FuncCall(qux, [IntLiteral(4)]))), -, FuncCall(quux, [IntLiteral(5)]))]), +, IntLiteral(8)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_string_expression():
    """60. String expression test"""
    source = """
    void main() {
        string s = "Hello, " + "World!";
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StringType(), s = BinaryOp(StringLiteral('Hello, '), +, StringLiteral('World!')))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_string_expression_with_function_call():
    """61. String expression with function call test"""
    source = """
    void main() {
        string s = "Hello, " + foo();
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StringType(), s = BinaryOp(StringLiteral('Hello, '), +, FuncCall(foo, [])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_structlit_expression():
    """62. Struct literal expression test"""
    source = """
    void main() {
        Point p = {1, 2};
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)}))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_member_access_expression():
    """63. Member access expression test"""
    source = """
    void main() {
        Point p;
        int x = p.x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), VarDecl(IntType(), x = MemberAccess(Identifier(p).x))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_member_access_expression_2():
    """64. Member access expression with function call test"""
    source = """
    void main() {
        Point p;
        int x = p.x.y;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), VarDecl(IntType(), x = MemberAccess(MemberAccess(Identifier(p).x).y))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_postfix_expression():
    """65. Postfix expression test"""
    source = """
    void main() {
        int x = 0;
        x++;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), ExprStmt(PostfixOp(Identifier(x)++))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_postfix_expression_2():
    """66. Postfix expression test 2"""
    source = """
    void main() {
        int x = 0;
        x--;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), ExprStmt(PostfixOp(Identifier(x)--))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_prefix_expression():
    """67. Prefix expression test"""
    source = """
    void main() {
        int x = 0;
        ++x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), ExprStmt(PrefixOp(++Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_prefix_expression_2():
    """68. Prefix expression test 2"""
    source = """
    void main() {
        int x = 0;
        --x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), ExprStmt(PrefixOp(--Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_prefix_expression_3():
    """69. Prefix expression with function call test"""
    source = """
    void main() {
        int x = 5;
        int a = -x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), a = PrefixOp(-Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_prefix_expression_4():
    """70. Prefix expression with function call test 2"""
    source = """
    void main() {
        int x = 5;
        int a = !x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), a = PrefixOp(!Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_prefix_expression_5():
    """71. Prefix expression with function call test 3"""
    source = """
    void main() {
        int x = 5;
        int a = +x;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), a = PrefixOp(+Identifier(x)))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_logical_expression():
    """72. Logical expression test"""
    source = """
    void main() {
        int x = 5;
        int y = 10;
        bool b = (x < y) && (y > 0);
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = IntLiteral(10)), VarDecl(StructType(bool), b = BinaryOp(BinaryOp(Identifier(x), <, Identifier(y)), &&, BinaryOp(Identifier(y), >, IntLiteral(0))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_logical_expression_2():
    """73. Logical expression with function call test"""
    source = """
    void main() {
        int x = 5;
        int y = 10;
        bool b = (x <= y) || (y >= 0) && (x != y);
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = IntLiteral(10)), VarDecl(StructType(bool), b = BinaryOp(BinaryOp(Identifier(x), <=, Identifier(y)), ||, BinaryOp(BinaryOp(Identifier(y), >=, IntLiteral(0)), &&, BinaryOp(Identifier(x), !=, Identifier(y)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_logical_expression_3():
    """74. Logical expression with nested logical expression test"""
    source = """
    void main() {
        int x = 5;
        int y = 10;
        bool b = (x < y) && ((y > 0) || (x == y));
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = IntLiteral(10)), VarDecl(StructType(bool), b = BinaryOp(BinaryOp(Identifier(x), <, Identifier(y)), &&, BinaryOp(BinaryOp(Identifier(y), >, IntLiteral(0)), ||, BinaryOp(Identifier(x), ==, Identifier(y)))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_logical_expression_4():
    """75. Logical expression with nested logical expression and function call test"""
    source = """
    void main() {
        int x = 5;
        int y = 10;
        bool b = (x < y) && ((y > 0) || (foo() == bar()));
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = IntLiteral(10)), VarDecl(StructType(bool), b = BinaryOp(BinaryOp(Identifier(x), <, Identifier(y)), &&, BinaryOp(BinaryOp(Identifier(y), >, IntLiteral(0)), ||, BinaryOp(FuncCall(foo, []), ==, FuncCall(bar, [])))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_logical_expression_5():
    """76. Logical expression with nested logical expression, function call and member access test"""
    source = """
    void main() {
        int x = 5;
        int y = 10;
        Point p;
        bool b = (x < y) && ((y > 0) || (foo(p.x) == bar()));
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = IntLiteral(10)), VarDecl(StructType(Point), p), VarDecl(StructType(bool), b = BinaryOp(BinaryOp(Identifier(x), <, Identifier(y)), &&, BinaryOp(BinaryOp(Identifier(y), >, IntLiteral(0)), ||, BinaryOp(FuncCall(foo, [MemberAccess(Identifier(p).x)]), ==, FuncCall(bar, [])))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_1():
    """77. Mixed test 1"""
    source = """
    void main() {
        int x = 5;
        int y = 10;
        Point p;
        bool b = (x < y) && ((y > 0) || (foo(p.x) == bar()));
        if (b) {
            x++;
        } else {
            x--;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = IntLiteral(10)), VarDecl(StructType(Point), p), VarDecl(StructType(bool), b = BinaryOp(BinaryOp(Identifier(x), <, Identifier(y)), &&, BinaryOp(BinaryOp(Identifier(y), >, IntLiteral(0)), ||, BinaryOp(FuncCall(foo, [MemberAccess(Identifier(p).x)]), ==, FuncCall(bar, []))))), IfStmt(if Identifier(b) then BlockStmt([ExprStmt(PostfixOp(Identifier(x)++))]), else BlockStmt([ExprStmt(PostfixOp(Identifier(x)--))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_2():
    """78. Mixed test 2"""
    source = """
    void main() {
        int x = 5;
        int y = 10;
        Point p;
        bool b = (x < y) && ((y > 0) || (foo(p.x) == bar()));
        for (int i = 0; i < 10; i = i + 1) {
            if (b) {
                x++;
            } else {
                x--;
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = IntLiteral(10)), VarDecl(StructType(Point), p), VarDecl(StructType(bool), b = BinaryOp(BinaryOp(Identifier(x), <, Identifier(y)), &&, BinaryOp(BinaryOp(Identifier(y), >, IntLiteral(0)), ||, BinaryOp(FuncCall(foo, [MemberAccess(Identifier(p).x)]), ==, FuncCall(bar, []))))), ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(10)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if Identifier(b) then BlockStmt([ExprStmt(PostfixOp(Identifier(x)++))]), else BlockStmt([ExprStmt(PostfixOp(Identifier(x)--))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_3():
    """79. Mixed test 3"""
    source = """
    void main() {
        int x = 5;
        int y = 10;
        Point p;
        bool b = (x < y) && ((y > 0) || (foo(p.x) == bar()));
        while (b) {
            x++;
            if (x > 100) {
                break;
            }
        }
    }
    """

    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(5)), VarDecl(IntType(), y = IntLiteral(10)), VarDecl(StructType(Point), p), VarDecl(StructType(bool), b = BinaryOp(BinaryOp(Identifier(x), <, Identifier(y)), &&, BinaryOp(BinaryOp(Identifier(y), >, IntLiteral(0)), ||, BinaryOp(FuncCall(foo, [MemberAccess(Identifier(p).x)]), ==, FuncCall(bar, []))))), WhileStmt(while Identifier(b) do BlockStmt([ExprStmt(PostfixOp(Identifier(x)++)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(100)) then BlockStmt([BreakStmt()]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_4():
    """80. Mixed test 4"""
    source = """
    void main() {
        Point p;
        for (int i = 0; i < 3; i = i + 1) {
            while (p.x < i) {
                {
                }
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(3)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([WhileStmt(while BinaryOp(MemberAccess(Identifier(p).x), <, Identifier(i)) do BlockStmt([BlockStmt([])]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_5():
    """81. Mixed test 5"""
    source = """
    int eval(int x) {
        switch (x) {
            case 0:
                for (int i = 0; i < 2; i = i + 1) {
                    x = x + i;
                }
                break;
            default:
                return x;
        }
        return x;
    }
    """
    expected = "Program([FuncDecl(IntType(), eval, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(0): [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(2)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, Identifier(i))))])), BreakStmt()])], default DefaultStmt(default: [ReturnStmt(return Identifier(x))])), ReturnStmt(return Identifier(x))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_6():
    """82. Mixed test 6"""
    source = """
    void main() {
        int y = foo(1);
        if (y > 0) {
            y = y - 1;
        } else {
            y = y + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), y = FuncCall(foo, [IntLiteral(1)])), IfStmt(if BinaryOp(Identifier(y), >, IntLiteral(0)) then BlockStmt([ExprStmt(AssignExpr(Identifier(y) = BinaryOp(Identifier(y), -, IntLiteral(1))))]), else BlockStmt([ExprStmt(AssignExpr(Identifier(y) = BinaryOp(Identifier(y), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_7():
    """83. Mixed test 7"""
    source = """
    void main() {
        Point p = {0, 0};
        for (int i = 0; i < 2; i = i + 1) {
            p.x = p.x + i;
            p.y = p.y + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p = StructLiteral({IntLiteral(0), IntLiteral(0)})), ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(2)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = BinaryOp(MemberAccess(Identifier(p).x), +, Identifier(i)))), ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = BinaryOp(MemberAccess(Identifier(p).y), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_8():
    """84. Mixed test 8"""
    source = """
    void main() {
        int x = 0;
        while (x < 5) {
            switch (x) {
                case 1:
                    x = x + 1;
                    break;
                default:
                    x = x + 2;
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(x), <, IntLiteral(5)) do BlockStmt([SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1)))), BreakStmt()])], default DefaultStmt(default: [ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(2))))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_9():
    """85. Mixed test 9"""
    source = """
    int inc(int a) {
        return a + 1;
    }

    void main() {
        int x = inc(inc(1));
    }
    """
    expected = "Program([FuncDecl(IntType(), inc, [Param(IntType(), a)], [ReturnStmt(return BinaryOp(Identifier(a), +, IntLiteral(1)))]), FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = FuncCall(inc, [FuncCall(inc, [IntLiteral(1)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_10():
    """86. Mixed test 10"""
    source = """
    void main() {
        Point p;
        if (p.x == 0) {
            foo(p);
        } else {
            bar();
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p), IfStmt(if BinaryOp(MemberAccess(Identifier(p).x), ==, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(foo, [Identifier(p)]))]), else BlockStmt([ExprStmt(FuncCall(bar, []))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_11():
    """87. Mixed test 11"""
    source = """
    void main() {
        int x = 0;
        int y = 10;
        while ((x < 10) && (y > 0)) {
            x = x + 1;
            y = y - 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), VarDecl(IntType(), y = IntLiteral(10)), WhileStmt(while BinaryOp(BinaryOp(Identifier(x), <, IntLiteral(10)), &&, BinaryOp(Identifier(y), >, IntLiteral(0))) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1)))), ExprStmt(AssignExpr(Identifier(y) = BinaryOp(Identifier(y), -, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_12():
    """88. Mixed test 12"""
    source = """
    void main() {
        int x = 0;
        switch (x) {
            default:
                while (x < 3) {
                    x = x + 1;
                }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), SwitchStmt(switch Identifier(x) cases [], default DefaultStmt(default: [WhileStmt(while BinaryOp(Identifier(x), <, IntLiteral(3)) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_13():
    """89. Mixed test 13"""
    source = """
    void main() {
        for (int i = 0; i < 5; i = i + 1) {
            if (i % 2 == 0) {
                foo(i);
            } else {
                bar(i);
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(5)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([IfStmt(if BinaryOp(BinaryOp(Identifier(i), %, IntLiteral(2)), ==, IntLiteral(0)) then BlockStmt([ExprStmt(FuncCall(foo, [Identifier(i)]))]), else BlockStmt([ExprStmt(FuncCall(bar, [Identifier(i)]))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_14():
    """90. Mixed test 14"""
    source = """
    int sum_point(Point p) {
        p.x = p.x + p.y;
        return p.x;
    }
    """
    expected = "Program([FuncDecl(IntType(), sum_point, [Param(StructType(Point), p)], [ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = BinaryOp(MemberAccess(Identifier(p).x), +, MemberAccess(Identifier(p).y)))), ReturnStmt(return MemberAccess(Identifier(p).x))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_15():
    """91. Mixed test 15: relational precedence edge case"""
    source = """
    void main() {
        int a = 1;
        int b = 2;
        int c = 3;
        int d = 4;
        int e = a < b == c > d;
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), a = IntLiteral(1)), VarDecl(IntType(), b = IntLiteral(2)), VarDecl(IntType(), c = IntLiteral(3)), VarDecl(IntType(), d = IntLiteral(4)), VarDecl(IntType(), e = BinaryOp(BinaryOp(Identifier(a), <, Identifier(b)), ==, BinaryOp(Identifier(c), >, Identifier(d))))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_16():
    """92. Mixed test 16"""
    source = """
    void main() {
        int x = 0;
        ++x;
        if (x == 1) {
            x--;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), ExprStmt(PrefixOp(++Identifier(x))), IfStmt(if BinaryOp(Identifier(x), ==, IntLiteral(1)) then BlockStmt([ExprStmt(PostfixOp(Identifier(x)--))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_17():
    """93. Mixed test 17"""
    source = """
    void main() {
        foo(bar(1), baz(2));
        int x = qux(foo(3));
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ExprStmt(FuncCall(foo, [FuncCall(bar, [IntLiteral(1)]), FuncCall(baz, [IntLiteral(2)])])), VarDecl(IntType(), x = FuncCall(qux, [FuncCall(foo, [IntLiteral(3)])]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_18():
    """94. Mixed test 18"""
    source = """
    int test2(int x) {
        switch (x) {
            case 1:
                if (x > 0) {
                    return 1;
                }
                break;
            default:
                return 0;
        }
        return 2;
    }
    """
    expected = "Program([FuncDecl(IntType(), test2, [Param(IntType(), x)], [SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(1): [IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([ReturnStmt(return IntLiteral(1))])), BreakStmt()])], default DefaultStmt(default: [ReturnStmt(return IntLiteral(0))])), ReturnStmt(return IntLiteral(2))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_19():
    """95. Mixed test 19"""
    source = """
    void main() {
        for (int i = 0; i < 3; i = i + 1) {
            int j = i;
            while (j > 0) {
                j = j - 1;
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(3)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([VarDecl(IntType(), j = Identifier(i)), WhileStmt(while BinaryOp(Identifier(j), >, IntLiteral(0)) do BlockStmt([ExprStmt(AssignExpr(Identifier(j) = BinaryOp(Identifier(j), -, IntLiteral(1))))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_20():
    """96. Mixed test 20"""
    source = """
    void logx(Point p) {
        print(p.x);
    }
    """
    expected = "Program([FuncDecl(VoidType(), logx, [Param(StructType(Point), p)], [ExprStmt(FuncCall(print, [MemberAccess(Identifier(p).x)]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_21():
    """97. Mixed test 21"""
    source = """
    void main() {
        int x = 20;
        if (x > 0) {
            if (x > 10) {
                x = x - 10;
            } else {
                x = x + 10;
            }
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(20)), IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(0)) then BlockStmt([IfStmt(if BinaryOp(Identifier(x), >, IntLiteral(10)) then BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), -, IntLiteral(10))))]), else BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(10))))]))]))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_22():
    """98. Mixed test 22"""
    source = """
    int calc() {
        return foo(1) + bar(2);
    }
    """
    expected = "Program([FuncDecl(IntType(), calc, [], [ReturnStmt(return BinaryOp(FuncCall(foo, [IntLiteral(1)]), +, FuncCall(bar, [IntLiteral(2)])))])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_23():
    """99. Mixed test 23"""
    source = """
    void main() {
        int x = 0;
        switch (x) {
            case 0:
                for (int i = 0; i < 2; i = i + 1) {
                    x = x + 1;
                }
                break;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(IntType(), x = IntLiteral(0)), SwitchStmt(switch Identifier(x) cases [CaseStmt(case IntLiteral(0): [ForStmt(for VarDecl(IntType(), i = IntLiteral(0)); BinaryOp(Identifier(i), <, IntLiteral(2)); AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))) do BlockStmt([ExprStmt(AssignExpr(Identifier(x) = BinaryOp(Identifier(x), +, IntLiteral(1))))])), BreakStmt()])])])])"
    assert str(ASTGenerator(source).generate()) == expected

def test_mixed_24():
    """100. Mixed test 24"""
    source = """
    void main() {
        Point p = {1, 2};
        int i = 0;
        while (i < 3) {
            if (p.x < p.y) {
                p.x = p.x + foo(i);
            } else {
                p.y = p.y + 1;
            }
            i = i + 1;
        }
    }
    """
    expected = "Program([FuncDecl(VoidType(), main, [], [VarDecl(StructType(Point), p = StructLiteral({IntLiteral(1), IntLiteral(2)})), VarDecl(IntType(), i = IntLiteral(0)), WhileStmt(while BinaryOp(Identifier(i), <, IntLiteral(3)) do BlockStmt([IfStmt(if BinaryOp(MemberAccess(Identifier(p).x), <, MemberAccess(Identifier(p).y)) then BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).x) = BinaryOp(MemberAccess(Identifier(p).x), +, FuncCall(foo, [Identifier(i)]))))]), else BlockStmt([ExprStmt(AssignExpr(MemberAccess(Identifier(p).y) = BinaryOp(MemberAccess(Identifier(p).y), +, IntLiteral(1))))])), ExprStmt(AssignExpr(Identifier(i) = BinaryOp(Identifier(i), +, IntLiteral(1))))]))])])"
    assert str(ASTGenerator(source).generate()) == expected