"""
Parser test cases for TyC compiler
TODO: Implement 100 test cases for parser
"""

import pytest
from tests.utils import Parser


# ========== Simple Test Cases (10 types) ==========
def test_empty_program():
    """1. Empty program"""
    assert Parser("").parse() == "success"


def test_program_with_only_main():
    """2. Program with only main function"""
    assert Parser("void main() {}").parse() == "success"


def test_struct_simple():
    """3. Struct declaration"""
    source = "struct Point { int x; int y; };"
    assert Parser(source).parse() == "success"


def test_function_no_params():
    """4. Function with no parameters"""
    source = "void greet() { printString(\"Hello\"); }"
    assert Parser(source).parse() == "success"


def test_var_decl_auto_with_init():
    """5. Variable declaration"""
    source = "void main() { auto x = 5; }"
    assert Parser(source).parse() == "success"


def test_if_simple():
    """6. If statement"""
    source = "void main() { if (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_while_simple():
    """7. While statement"""
    source = "void main() { while (1) printInt(1); }"
    assert Parser(source).parse() == "success"


def test_for_simple():
    """8. For statement"""
    source = "void main() { for (auto i = 0; i < 10; ++i) printInt(i); }"
    assert Parser(source).parse() == "success"


def test_switch_simple():
    """9. Switch statement"""
    source = "void main() { switch (1) { case 1: printInt(1); break; } }"
    assert Parser(source).parse() == "success"


def test_assignment_simple():
    """10. Assignment statement"""
    source = "void main() { int x; x = 5; }"
    assert Parser(source).parse() == "success"

def test_integer_negative():
    """11. Negative integer literal"""
    source = "void main() { auto x = -42; }"
    assert Parser(source).parse() == "success"

def test_struct_member_access():
    """12. Struct member access"""
    source = """
    struct Point { int x; int y; };
    void main() {
        Point p;
        ++a1.x = 10;
        {1,2,3}.y = 20;
    }
    """
    assert Parser(source).parse() == "Error on line 5 col 15: ="


# ========== Function Tests ==========
def test_function_declaration_void_no_params():
    """13. Function declaration: void return type, no parameters"""
    source = "void initialize() { }"
    assert Parser(source).parse() == "success"


def test_function_declaration_int_no_params():
    """14. Function declaration: int return type, no parameters"""
    source = "int getValue() { return 42; }"
    assert Parser(source).parse() == "success"


def test_function_declaration_with_single_param():
    """15. Function declaration: single parameter"""
    source = "int square(int x) { return x * x; }"
    assert Parser(source).parse() == "success"


def test_function_declaration_with_multiple_params():
    """16. Function declaration: multiple parameters"""
    source = "int add(int a, int b, int c) { return a + b + c; }"
    assert Parser(source).parse() == "success"


def test_function_declaration_float_return():
    """17. Function declaration: float return type"""
    source = "float divide(int a, int b) { return a / b; }"
    assert Parser(source).parse() == "success"


def test_function_call_no_args():
    """18. Function call: no arguments"""
    source = "void main() { initialize(); }"
    assert Parser(source).parse() == "success"


def test_function_call_single_arg():
    """19. Function call: single argument"""
    source = "void main() { auto result = square(5); }"
    assert Parser(source).parse() == "success"


def test_function_call_multiple_args():
    """20. Function call: multiple arguments"""
    source = "void main() { auto sum = add(1, 2, 3); }"
    assert Parser(source).parse() == "success"


def test_function_call_nested():
    """21. Function call: nested function calls"""
    source = "void main() { auto result = add(square(2), square(3), getValue()); }"
    assert Parser(source).parse() == "success"


def test_function_call_in_expression():
    """22. Function call: used in complex expression"""
    source = """
    void main() {
        auto x = getValue() + square(3) * 2;
        if (getValue() > 0) {
            printInt(square(x));
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_function_without_type():
    """23. Function declaration without return type (should fail)"""
    source = "main() { return 0; }"
    assert Parser(source).parse() == "success"

def test_function_with_nested_function_declare():
    """24. Function declaration with nested function (should fail)"""
    source = """
    void outer() {
        void inner() {
            return;
        }
        inner();
    }
    """ 
    assert Parser(source).parse() == "Error on line 3 col 8: void"

def test_var_declare_global():
    """25. Global variable declaration"""
    source = """
    int globalVar;
    void main() {
        globalVar = 10;
    }
    """
    assert Parser(source).parse() == "Error on line 2 col 17: ;"

def test_var_declare_local():
    """26. Local variable declaration"""
    source = """
    void main() {
        int localVar = 5;
        printInt(localVar);
    }
    """
    assert Parser(source).parse() == "success"

def test_var_declare_multiple():
    """27. Multiple variable declarations"""
    source = """
    nothing foo() {
        int a = 1, b = 2, c = 3;
        printInt(a + b + c);
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 17: ,"

def test_var_declare_without_init():
    """28. Variable declaration without initialization"""
    source = """
    void main() {
        float pi;
        pi = 3.14;
        printFloat(pi);
    }
    """
    assert Parser(source).parse() == "success"

def test_var_declare_with_complex_init():
    """29. Variable declaration with complex initialization"""
    source = """
    void main() {
        int x = 5 + 3 * 2;
        printInt(x);
    }
    """
    assert Parser(source).parse() == "success"

def test_var_declare_with_complex_init_2():
    """30. Variable declaration with complex initialization 2"""
    source = """
    void main() {
        float y = (4.5 / 1.5) + --2.0++;
        printFloat(y);
    }
    """
    assert Parser(source).parse() == "success"

def test_var_assign_simple():
    """31. Simple variable assignment"""
    source = """
    void main() {
        x = 10;
        printInt(x);
    }
    """
    assert Parser(source).parse() == "success"

def test_var_assign_expression():
    """32. Variable assignment with expression"""
    source = """
    void main() {
        x = 5 + 3 * 2;
        printInt(t);
    }
    """
    assert Parser(source).parse() == "success"

def test_var_assign_struct_initialization():
    """33. Variable assignment with struct initialization"""
    source = """
    struct Point { int x; int y; };
    void main() {
        Point p = {10, 20};
        printInt(p.x + p.y);
    }
    """
    assert Parser(source).parse() == "success"

def test_struct_declare_with_methods():
    """34. Struct declaration with methods"""
    source = """
    struct Point {
        int x;
        int y;
        void move(int dx, int dy) {
            x = x + dx;
            y = y + dy;
        }
    };
    """
    assert Parser(source).parse() == "Error on line 5 col 8: void"

def test_struct_declare_with_struct_type():
    """35. Struct declaration with struct type member"""
    source = """
    struct Line {
        Point start;
        Point end;
    };
    """
    assert Parser(source).parse() == "success"

def test_struct_declare_nested():
    """36. Nested struct declaration"""
    source = """
    struct Rectangle {
        struct Point {
            int x;
            int y;
        };
        Point topLeft;
        Point bottomRight;
    };
    """
    assert Parser(source).parse() == "Error on line 3 col 8: struct"

def test_struct_declare_no_semicolon():
    """37. Struct declaration without semicolon (should fail)"""
    source = """
    struct Circle {
        int radius;
    }
    """
    assert Parser(source).parse() == "Error on line 5 col 4: <EOF>"

def test_empty_struct():
    """38. Empty struct declaration"""
    source = "struct Empty { };"
    assert Parser(source).parse() == "success"

def test_for_loop_complex():
    """39. Complex for loop"""
    source = """
    void main() {
        for (auto i = 0; i < 10; i = i + 2) {
            printInt(i);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_for_loop_missing_parts():
    """40. For loop with missing parts"""
    source = """
    void main() {
        for (;;) {
            printInt(1);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_for_loop_nested():
    """41. Nested for loops"""
    source = """
    void main() {
        for (auto i = 0; i < 5; ++i) {
            for (auto j = 0; j < 5; ++j) {
                printInt(i * j);
            }
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_for_loop_with_break_continue():
    """42. For loop with break and continue"""
    source = """
    void main() {
        for (auto i = 0; i < 10; ++i) {
            if (i % 2 == 0) continue;
            if (i > 7) break;
            printInt(i);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_for_loop_missing_parts_2():
    """43. For loop with missing parts 2"""
    source = """
    void main() {
        for (auto i = 0;;) {
            printInt(i);
            ++i;
            if (i >= 10) break;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_for_loop_missing_parts_3():
    """44. For loop with missing parts 3"""
    source = """
    void main() {
        auto i = 0;
        for (; i < 10;) {
            printInt(i);
            ++i;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_for_loop_wrong_syntax():
    """45. For loop with wrong syntax"""
    source = """
    void main() {
        for (auto i = 0 i < 10 ++i) {
            printInt(i);
        }
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 24: i"

def test_for_loop_wrong_syntax_2():
    """46. For loop with wrong syntax 2"""
    source = """
    void main() {
        for (int a = 1;auto i = 0;++a)
            printInt(i);
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 23: auto"

def test_for_loop_wrong_syntax_3():
    """47. For loop with wrong syntax 3"""
    source = """
    void main() {
        for (;;i < 9) printInt(i)
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 17: <"

def test_for_with_expr():
    """48. For loop with no body"""
    source = """
    void main() {
        for (a = 1; 138; --b){
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_for_with_expr_2():
    """49. For loop with no body 2"""
    source = """
    void main() {
        for (a = 1; 0138; --b){
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_while_loop_complex():
    """50. Complex while loop"""
    source = """
    void main() {
        auto i = 0;
        while (i < 10) {
            printInt(i);
            ++i;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_while_empty_body():
    """51. While loop with empty body"""
    source = """
    void main() {
        auto i = 0;
        while (i < 10){}
    }
    """
    assert Parser(source).parse() == "success"

def test_while_empty_condition():
    """52. While loop with empty header (should fail)"""
    source = """
    void main() {
        while () {
            printInt(1);
        }
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 15: )"

def test_while_expr_in_condition():
    """53. While loop with expression in condition"""
    source = """
    void main() {
        auto i = 0;
        while (i < 10 && i % 2 == 0) {
            printInt(i);
            ++i;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_while_nested():
    """54. Nested while loops"""
    source = """
    void main() {
        auto i = 0;
        while (i < 5) {
            auto j = 0;
            while (j < 5) {
                printInt(i * j);
                ++j;
            }
            ++i;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_while_with_break_continue():
    """55. While loop with break and continue"""
    source = """
    void main() {
        auto i = 0;
        while (i < 10) {
            ++i;
            if (i % 2 == 0) continue;
            if (i > 7) break;
            printInt(i);
        }
    }
    """ 
    assert Parser(source).parse() == "success"

def test_while_wrong_syntax():
    """56. While loop with wrong syntax"""
    source = """
    void main() {
        while i < 10 {
            printInt(i);
        }
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 14: i"

def test_while_wrong_syntax_2():
    """57. While loop with wrong syntax 2"""
    source = """
    void main() {
        while (i < 10
            printInt(i);
        }
    }
    """
    assert Parser(source).parse() == "Error on line 4 col 12: printInt"

def test_while_wrong_syntax_3():
    """58. While loop with wrong syntax 3"""
    source = """
    void main() {
        while (i < 10)) {
            printInt(i);
        }
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 22: )"

def test_if_else_complex():
    """59. Complex if-else statement"""
    source = """
    void main() {
        auto x = 10;
        if (x > 0)
            printInt(x);
        else {
            printInt(-x);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_if_nested():
    """60. Nested if statements"""
    source = """
    void main() {
        auto x = 5;
        if (x > 0) {
            if (x < 10) {
                printInt(x);
            }
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_if_without_else():
    """61. If statement without else"""
    source = """
    void main() {
        auto x = 10;
        if (x > 0) {
            printInt(x);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_if_with_else_only():
    """62. If statement with else only"""
    source = """
    void main() {
        auto x = -5;
        else {
            printInt(x);
        }
    }
    """
    assert Parser(source).parse() == "Error on line 4 col 8: else"

def test_if_wrong_syntax():
    """63. If statement with wrong syntax"""
    source = """
    void main() {
        if x > 0 {
            printInt(x);
        }
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 11: x"

def test_if_wrong_syntax_2():
    """64. If statement with wrong syntax 2"""
    source = """
    void main() {
        if (x > 0
            printInt(x);
        }
    """
    assert Parser(source).parse() == "Error on line 4 col 12: printInt"

def test_if_double_parentheses():
    """65. If statement with double closing parentheses"""
    source = """
    void main() {
        if ((x > 0)) {
            printInt(x);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_switch_multiple_cases():
    """66. Switch statement with multiple cases"""
    source = """
    void main() {
        auto x = 2;
        switch (x) {
            case 1:
                printInt(1);
                break;
            case 2:
                printInt(2);
                break;
            case 3:
                printInt(3);
                break;
            default:
                printInt(0);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_without_default_case():
    """67. Switch statement without default case"""
    source = """
    void main() {
        auto x = 1;
        switch (x) {
            case 1:
                printInt(1);
                break;
            case 2:
                printInt(2);
                break;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_switch_nested():
    """68. Nested switch statements"""
    source = """
    void main() {
        auto x = 1;
        auto y = 2;
        switch (x) {
            case 1:
                switch (y) {
                    case 2:
                        printInt(2);
                        break;
                }
                break;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_empty_switch():
    """69. Empty switch statement"""
    source = """
    void main() {
        auto x = 0;
        switch (x) {
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_switch_wrong_syntax():
    """70. Switch statement with wrong syntax"""
    source = """
    void main() {
        auto x = 1;
        switch () {
            case 1:
                printInt(1);
                break;
        }
    }
    """
    assert Parser(source).parse() == "Error on line 4 col 16: )"

def test_switch_wrong_syntax_2():
    """71. Switch statement with wrong syntax 2"""
    source = """
    void main() {
        auto x = 1;
        switch x {
            case 1
                printInt(1);
                break;
        }
    }
    """
    assert Parser(source).parse() == "Error on line 4 col 15: x"

def test_expression_arithmetic():
    """72. Arithmetic expression"""
    source = """
    void main() {
        auto result = (5 + 3) * 2 - 4 / 2;
        printInt(result);
    }
    """
    assert Parser(source).parse() == "success"

def test_expression_logical():
    """73. Logical expression"""
    source = """
    void main() {
        auto flag = (1 < 2) && (3 > 2) || !(0 == 1);
        printInt(flag);
    }
    """
    assert Parser(source).parse() == "success"

def test_expression_mixed():
    """74. Mixed arithmetic and logical expression"""
    source = """
    void main() {
        auto result = ((5 + 3) > 6) && ((2 * 2) == 4);
        printInt(result);
    }
    """
    assert Parser(source).parse() == "success"

def test_expression_with_function_calls():
    """75. Expression with function calls"""
    source = """
    void main() {
        auto result = add(2, 3) * add(4, 5);
        printInt(result);
    }
    """
    assert Parser(source).parse() == "success"

def test_expression_with_struct_members():
    """76. Expression with struct members"""
    source = """
    struct Point { int x; int y; };
    void main() {
        Point p;
        p.x = 10;
        p.y = 20;
        auto sum = p.x + p.y;
        printInt(sum);
    }
    """
    assert Parser(source).parse() == "success"

def test_expression_with_unary_operators():
    """77. Expression with unary operators"""
    source = """
    void main() {
        auto result = -x + ++x - --x + x++;
        printInt(result);
    }
    """
    assert Parser(source).parse() == "success"

def test_expression_with_parentheses():
    """78. Expression with multiple parentheses"""
    source = """
    void main() {
        auto result = (((5 + 3) * (2 - 1)) / (4 / 2));
        printInt(result);
    }
    """
    assert Parser(source).parse() == "success"

def test_expression_wrong_syntax():
    """79. Expression with wrong syntax"""
    source = """
    void main() {
        auto result = 5 + * 3;
        printInt(result);
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 26: *"

def test_expression_wrong_syntax_2():
    """80. Expression with wrong syntax 2"""
    source = """
    void main() {
        auto result = (5 + 3;
        printInt(result);
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 28: ;"

def test_expression_on_block_stament():
    """81. Expression used as a statement (should fail)"""
    source = """
    void main() {
        (5 + 3) * 2;
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_program():
    """82. Complex program combining multiple features"""
    source = """
    struct Point {
        int x;
        int y;
        void move;
    };
    int add(int a, int b) {
        return a + b;
    }
    void main() {
        Point p;
        p.x = 0;
        p.y = 0;
        for (auto i = 0; i < 10; ++i) {
            p.move(1, 2);
        }
        printInt(add(p.x, p.y));
    }
    """
    assert Parser(source).parse() == "Error on line 5 col 8: void"

def test_complex_program_2():
    """83. Another complex program combining multiple features"""
    source = """
    struct Rectangle {
        Point p;
        Point topLeft;
        Point bottomRight;
        int area;
    };
    void main() {
        Rectangle rect;
        rect.topLeft.x = 0;
        rect.topLeft.y = 0;
        rect.bottomRight.x = 10;
        rect.bottomRight.y = 5;
        printInt(rect.area);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_mix_for_if_function():
    """84. Mix for loop, if statement, and function calls"""
    source = """
    int process(int x) {
        return x * 2;
    }
    void main() {
        for (auto i = 0; i < 10; ++i) {
            if (i % 2 == 0) {
                printInt(process(i));
            } else {
                printInt(i);
            }
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_mix_while_switch():
    """85. Mix while loop with switch statement"""
    source = """
    void main() {
        auto count = 0;
        while (count < 5) {
            switch (count) {
                case 0:
                    printString("zero");
                    break;
                case 1:
                    printString("one");
                    break;
                default:
                    printString("other");
            }
            ++count;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_struct_in_loop():
    """86. Struct operations inside loops"""
    source = """
    struct Point {
        int x;
        int y;
    };
    void main() {
        Point p = {0, 0};
        for (auto i = 0; i < 10; ++i) {
            p.x = p.x + i;
            p.y = p.y + i * 2;
            if (p.x > 20) {
                break;
            }
        }
        printInt(p.x);
        printInt(p.y);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_nested_loops_with_struct():
    """87. Nested loops with struct and expressions"""
    source = """
    struct Data {
        int value;
        int sum;
    };
    void main() {
        Data d = {0, 0};
        for (auto i = 0; i < 3; ++i) {
            for (auto j = 0; j < 3; ++j) {
                d.value = i * j;
                d.sum = d.sum + d.value;
            }
        }
        printInt(d.sum);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_function_with_struct_param():
    """88. Function with struct parameter and return"""
    source = """
    struct Point {
        int x;
        int y;
    };
    Point createPoint(int a, int b) {
        Point p = {a, b};
        return p;
    }
    void main() {
        Point myPoint = createPoint(5, 10);
        printInt(myPoint.x);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_switch_in_for():
    """89. Switch statement inside for loop with multiple cases"""
    source = """
    void main() {
        for (auto i = 0; i < 10; i = i + 1) {
            switch (i) {
                case 0:
                case 1:
                    printInt(1);
                    break;
                case 2:
                    printInt(2);
                    break;
                default:
                    printInt(0);
                    break;
            }
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_while_with_function_calls():
    """90. While loop with multiple function calls and expressions"""
    source = """
    int getValue() {
        return 42;
    }
    int compute(int x, int y) {
        return x + y;
    }
    void main() {
        auto counter = 0;
        while (counter < getValue()) {
            auto result = compute(counter, getValue());
            printInt(result);
            counter = counter + 1;
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_if_else_chain_with_expressions():
    """91. Long if-else chain with complex expressions"""
    source = """
    void main() {
        auto x = 15;
        auto y = 20;
        if (x > y && x < 100) {
            printInt(x);
        } else if (x == y || y < 10) {
            printInt(y);
        } else if (x + y > 30) {
            printInt(x + y);
        } else {
            printInt(0);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_mixed_control_flow():
    """92. Mixed control flow: for, while, if, switch"""
    source = """
    void main() {
        for (auto i = 0; i < 5; ++i) {
            auto j = 0;
            while (j < i) {
                if (j % 2 == 0) {
                    switch (j) {
                        case 0:
                            printInt(0);
                            break;
                        case 2:
                            printInt(2);
                            break;
                    }
                }
                ++j;
            }
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_struct_array_simulation():
    """93. Multiple struct variables with operations"""
    source = """
    struct Point {
        int x;
        int y;
    };
    void main() {
        Point p1 = {1, 2};
        Point p2 = {3, 4};
        Point p3;
        p3.x = p1.x + p2.x;
        p3.y = p1.y + p2.y;
        printInt(p3.x);
        printInt(p3.y);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_function_recursion_style():
    """94. Function with recursive-style control flow"""
    source = """
    int factorial(int n) {
        if (n <= 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }
    void main() {
        auto result = factorial(5);
        printInt(result);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_expression_precedence():
    """95. Complex expression with operator precedence"""
    source = """
    void main() {
        auto a = 5;
        auto b = 10;
        auto c = 15;
        auto result = a + b * c - a / b + c % a;
        printInt(result);
        auto logic = a < b && b < c || c == a;
        printInt(logic);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_nested_struct_operations():
    """96. Nested struct with complex operations"""
    source = """
    struct Inner {
        int val;
    };
    struct Outer {
        Inner data;
        int extra;
    };
    void main() {
        Outer obj;
        obj.data.val = 100;
        obj.extra = 200;
        auto sum = obj.data.val + obj.extra;
        printInt(sum);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_for_with_multiple_statements():
    """97. For loop with multiple complex statements"""
    source = """
    void main() {
        auto sum = 0;
        auto product = 1;
        for (auto i = 1; i <= 5; ++i) {
            sum = sum + i;
            product = product * i;
            printInt(i);
            printInt(sum);
            printInt(product);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_while_with_break_continue_conditions():
    """98. While loop with complex break/continue conditions"""
    source = """
    void main() {
        auto i = 0;
        while (i < 20) {
            ++i;
            if (i % 3 == 0 && i % 5 == 0) {
                break;
            }
            if (i % 2 == 0) {
                continue;
            }
            printInt(i);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_switch_with_expressions():
    """99. Switch with expression cases and fall-through"""
    source = """
    void main() {
        auto x = 5;
        auto y = 10;
        switch (x + y) {
            case 10:
                printInt(10);
            case 15:
                printInt(15);
                break;
            case 20:
                printInt(20);
                break;
            default:
                printInt(-1);
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_multiple_functions_interaction():
    """100. Multiple functions calling each other"""
    source = """
    int helper(int x) {
        return x * 2;
    }
    int process(int a, int b) {
        return helper(a) + helper(b);
    }
    void main() {
        auto val1 = 5;
        auto val2 = 10;
        auto result = process(val1, val2);
        printInt(result);
        if (result > 20) {
            printInt(helper(result));
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_struct_with_functions():
    """101. Struct combined with function operations"""
    source = """
    struct Point {
        int x;
        int y;
    };
    int distance(Point p1, Point p2) {
        return (p2.x - p1.x) + (p2.y - p1.y);
    }
    void main() {
        Point origin = {0, 0};
        Point dest = {10, 20};
        auto dist = distance(origin, dest);
        printInt(dist);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_all_features_combined():
    """102. All major features combined in one program"""
    source = """
    struct Data {
        int value;
        int count;
    };
    int calculate(int x, int y) {
        if (x > y) {
            return x - y;
        } else {
            return y - x;
        }
    }
    void main() {
        Data d = {0, 0};
        for (auto i = 0; i < 10; ++i) {
            auto j = 0;
            while (j < 5) {
                switch (j) {
                    case 0:
                        d.value = calculate(i, j);
                        break;
                    case 1:
                    case 2:
                        d.count = d.count + 1;
                        break;
                    default:
                        d.value = d.value + j;
                }
                ++j;
            }
            if (d.value > 15) {
                break;
            }
        }
        printInt(d.value);
        printInt(d.count);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_deeply_nested_control():
    """103. Deeply nested control structures"""
    source = """
    void main() {
        for (auto i = 0; i < 3; ++i) {
            if (i > 0) {
                auto j = 0;
                while (j < 2) {
                    switch (i + j) {
                        case 1:
                            if (j == 0) {
                                printInt(1);
                            }
                            break;
                        case 2:
                            printInt(2);
                            break;
                    }
                    ++j;
                }
            }
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_expressions_in_control():
    """104. Complex expressions in control flow conditions"""
    source = """
    void main() {
        auto x = 10;
        auto y = 20;
        auto z = 30;
        for (auto i = 0; i < x + y; i = i + 1) {
            if ((i > x && i < y) || i == z) {
                while (x < y && y < z) {
                    printInt(x + y + z);
                    ++x;
                }
            }
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_struct_initialization_in_loop():
    """105. Struct initialization and manipulation in loops"""
    source = """
    struct Config {
        int min;
        int max;
        int current;
    };
    void main() {
        Config cfg = {0, 100, 50};
        for (auto i = cfg.min; i < cfg.max; i = i + 10) {
            cfg.current = i;
            if (cfg.current > 50) {
                printInt(cfg.current);
            }
        }
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_function_with_all_types():
    """106. Functions with different parameter types"""
    source = """
    struct Point {
        int x;
        int y;
    };
    int add(int a, int b) {
        return a + b;
    }
    float multiply(float x, float y) {
        return x * y;
    }
    Point makePoint(int x, int y) {
        Point p = {x, y};
        return p;
    }
    void main() {
        auto sum = add(5, 10);
        auto prod = multiply(2.5, 4.0);
        Point p = makePoint(sum, 20);
        printInt(p.x);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_switch_nested_in_while():
    """107. Switch nested in while with complex logic"""
    source = """
    void main() {
        auto counter = 0;
        auto state = 0;
        while (counter < 15) {
            switch (state) {
                case 0:
                    counter = counter + 1;
                    if (counter > 5) {
                        state = 1;
                    }
                    break;
                case 1:
                    counter = counter + 2;
                    state = 2;
                    break;
                default:
                    counter = counter + 3;
                    break;
            }
        }
        printInt(counter);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_multiple_var_declarations():
    """108. Multiple variable declarations with different types"""
    source = """
    struct Point {
        int x;
        int y;
    };
    void main() {
        int a = 10;
        float b = 3.14;
        string msg = "hello";
        auto c = 20;
        auto d = 2.5;
        Point p = {a, c};
        printInt(a + c);
        printFloat(b + d);
        printString(msg);
        printInt(p.x + p.y);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_chained_assignments():
    """109. Chained assignments with expressions"""
    source = """
    void main() {
        int a;
        int b;
        int c;
        a = b == (c == 10);
        printInt(a);
        printInt(b);
        printInt(c);
        a = b + (c == 5);
        printInt(a);
        printInt(c);
    }
    """
    assert Parser(source).parse() == "success"

def test_complex_ultimate_combination():
    """110. Ultimate combination of all features"""
    source = """
    struct Person {
        int age;
        int score;
    };
    struct Team {
        Person member;
        int total;
    };
    int evaluate(int age, int score) {
        if (age > 18 && score > 50) {
            return 100;
        } else if (age > 18 || score > 75) {
            return 75;
        } else {
            return 50;
        }
    }
    void processTeam(Team t) {
        for (auto i = 0; i < 10; ++i) {
            auto result = evaluate(t.member.age, t.member.score);
            switch (result) {
                case 100:
                    t.total = t.total + 10;
                    break;
                case 75:
                    t.total = t.total + 7;
                    break;
                default:
                    t.total = t.total + 5;
            }
            if (t.total > 50) {
                break;
            }
        }
        printInt(t.total);
    }
    void main() {
        Person p = {25, 80};
        Team myTeam;
        myTeam.member = p;
        myTeam.total = 0;
        processTeam(myTeam);
        auto counter = 0;
        while (counter < 5) {
            if (counter % 2 == 0) {
                myTeam.total = myTeam.total + evaluate(20, 60);
            } else {
                myTeam.total = myTeam.total + 1;
            }
            ++counter;
        }
        printInt(myTeam.total);
    }
    """
    assert Parser(source).parse() == "success"

def testParser083():
    source = r"""
    void main() {
        int a;
        (a < 3) = 10;
    }
    """
    assert Parser(source).parse() == "Error on line 4 col 16: ="

def testParser084():
    source = r"""
    void main() {
        1 = 2;
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 10: ="

def testParser088():
    source = r"""
    void main() {
        {1,2} = {3,4};
    }
    """
    assert Parser(source).parse() == "Error on line 3 col 14: ="

def testParser112():
    source = r"""
    struct Point { int x; int y; };
    void main() {
        {1,2} = 5;
    }
    """
    assert Parser(source).parse() == "Error on line 4 col 14: ="

