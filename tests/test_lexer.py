"""
Lexer test cases for TyC compiler
TODO: Implement 100 test cases for lexer
"""

import pytest
from tests.utils import Tokenizer


def test_keyword_auto():
    """1. Keyword - auto"""
    tokenizer = Tokenizer("auto")
    assert tokenizer.get_tokens_as_string() == "auto,<EOF>"

def test_keyword_break():
    """2. Keyword - break"""
    tokenizer = Tokenizer("break")
    assert tokenizer.get_tokens_as_string() == "break,<EOF>"

def test_keyword_case():
    """3. Keyword - case"""
    tokenizer = Tokenizer("case")
    assert tokenizer.get_tokens_as_string() == "case,<EOF>"

def test_keyword_continue():
    """4. Keyword - continue"""
    tokenizer = Tokenizer("continue")
    assert tokenizer.get_tokens_as_string() == "continue,<EOF>"

def test_keyword_default():
    """5. Keyword - default"""
    tokenizer = Tokenizer("default")
    assert tokenizer.get_tokens_as_string() == "default,<EOF>"

def test_keyword_else():
    """6. Keyword - else"""
    tokenizer = Tokenizer("else")
    assert tokenizer.get_tokens_as_string() == "else,<EOF>"

def test_keyword_float():
    """7. Keyword - float"""
    tokenizer = Tokenizer("float")
    assert tokenizer.get_tokens_as_string() == "float,<EOF>"

def test_keyword_for():
    """8. Keyword - for"""
    tokenizer = Tokenizer("for")
    assert tokenizer.get_tokens_as_string() == "for,<EOF>"

def test_keyword_ifElse():
    """9. Keyword - if else"""
    tokenizer = Tokenizer("if else")
    assert tokenizer.get_tokens_as_string() == "if,else,<EOF>"

def test_keyword_int():
    """10. Keyword - int"""
    tokenizer = Tokenizer("int")
    assert tokenizer.get_tokens_as_string() == "int,<EOF>"

def test_keyword_return():
    """11. Keyword - return"""
    tokenizer = Tokenizer("return")
    assert tokenizer.get_tokens_as_string() == "return,<EOF>"

def test_keyword_string():
    """12. Keyword - string"""
    tokenizer = Tokenizer("string")
    assert tokenizer.get_tokens_as_string() == "string,<EOF>"

def test_keyword_struct():
    """13. Keyword - struct"""
    tokenizer = Tokenizer("struct")
    assert tokenizer.get_tokens_as_string() == "struct,<EOF>"

def test_keyword_switch():
    """14. Keyword - switch"""
    tokenizer = Tokenizer("switch")
    assert tokenizer.get_tokens_as_string() == "switch,<EOF>"

def test_keyword_void():
    """15. Keyword - void"""
    tokenizer = Tokenizer("void")
    assert tokenizer.get_tokens_as_string() == "void,<EOF>"

def test_keyword_while():
    """16. Keyword - while"""
    tokenizer = Tokenizer("while")
    assert tokenizer.get_tokens_as_string() == "while,<EOF>"

def test_operator_plus():
    """17. Operator - plus"""
    tokenizer = Tokenizer("+")
    assert tokenizer.get_tokens_as_string() == "+,<EOF>"

def test_operator_minus():
    """18. Operator - minus"""
    tokenizer = Tokenizer("-")
    assert tokenizer.get_tokens_as_string() == "-,<EOF>"

def test_operator_multiply():
    """19. Operator - multiply"""
    tokenizer = Tokenizer("*")
    assert tokenizer.get_tokens_as_string() == "*,<EOF>"

def test_operator_divide():
    """20. Operator - divide"""
    tokenizer = Tokenizer("/")
    assert tokenizer.get_tokens_as_string() == "/,<EOF>"

def test_operator_modulus():
    """21. Operator - modulus"""
    tokenizer = Tokenizer("%")
    assert tokenizer.get_tokens_as_string() == "%,<EOF>"

def test_operator_equal():
    """22. Operator - equal"""
    tokenizer = Tokenizer("==")
    assert tokenizer.get_tokens_as_string() == "==,<EOF>"

def test_operator_not_equal():
    """23. Operator - not equal"""
    tokenizer = Tokenizer("!=")
    assert tokenizer.get_tokens_as_string() == "!=,<EOF>"

def test_operator_less_than():
    """24. Operator - less than"""
    tokenizer = Tokenizer("<")
    assert tokenizer.get_tokens_as_string() == "<,<EOF>"

def test_operator_greater_than():
    """25. Operator - greater than"""
    tokenizer = Tokenizer(">")
    assert tokenizer.get_tokens_as_string() == ">,<EOF>"

def test_operator_less_equal():
    """26. Operator - less or equal"""
    tokenizer = Tokenizer("<=")
    assert tokenizer.get_tokens_as_string() == "<=,<EOF>"

def test_operator_greater_equal():
    """27. Operator - greater or equal"""
    tokenizer = Tokenizer(">=")
    assert tokenizer.get_tokens_as_string() == ">=,<EOF>"

def test_operator_logical_or():
    """28. Operator - logical or"""
    tokenizer = Tokenizer("||")
    assert tokenizer.get_tokens_as_string() == "||,<EOF>"

def test_operator_logical_and():
    """29. Operator - logical and"""
    tokenizer = Tokenizer("&&")
    assert tokenizer.get_tokens_as_string() == "&&,<EOF>"

def test_operator_logical_not():
    """30. Operator - logical not"""
    tokenizer = Tokenizer("!")
    assert tokenizer.get_tokens_as_string() == "!,<EOF>"

def test_operator_increment():
    """31. Operator - increment"""
    tokenizer = Tokenizer("++")
    assert tokenizer.get_tokens_as_string() == "++,<EOF>"

def test_operator_decrement():
    """32. Operator - decrement"""
    tokenizer = Tokenizer("--")
    assert tokenizer.get_tokens_as_string() == "--,<EOF>"

def test_operator_assign():
    """33. Operator - assign"""
    tokenizer = Tokenizer("=")
    assert tokenizer.get_tokens_as_string() == "=,<EOF>"

def test_operator_dot():
    """34. Operator - dot (member access)"""
    tokenizer = Tokenizer(".")
    assert tokenizer.get_tokens_as_string() == ".,<EOF>"

def test_separator_semi():
    """35. Separator - semicolon"""
    tokenizer = Tokenizer(";")
    assert tokenizer.get_tokens_as_string() == ";,<EOF>"

def test_separator_comma():
    """36. Separator - comma"""
    tokenizer = Tokenizer(",")
    assert tokenizer.get_tokens_as_string() == ",,<EOF>"

def test_separator_colon():
    """37. Separator - colon"""
    tokenizer = Tokenizer(":")
    assert tokenizer.get_tokens_as_string() == ":,<EOF>"

def test_separator_parentheses():
    """38. Separator - parentheses"""
    tokenizer = Tokenizer("()")
    assert tokenizer.get_tokens_as_string() == "(,),<EOF>"

def test_separator_braces():
    """39. Separator - braces"""
    tokenizer = Tokenizer("{}")
    assert tokenizer.get_tokens_as_string() == "{,},<EOF>"

def test_separator_brackets():
    """40. Separator - brackets as error"""
    tokenizer = Tokenizer("[]")
    assert tokenizer.get_tokens_as_string() == "Error Token ["

def test_whitespace_only():
    """41. Whitespace only"""
    tokenizer = Tokenizer("   \t  \n  ")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_symbol_invalid_1():
    """42. Invalid symbol - @"""
    tokenizer = Tokenizer("@")
    assert tokenizer.get_tokens_as_string() == "Error Token @"

def test_symbol_invalid_2():
    """43. Invalid symbol - #"""
    tokenizer = Tokenizer("#")
    assert tokenizer.get_tokens_as_string() == "Error Token #"

def test_symbol_invalid_3():
    """44. Invalid symbol - $"""
    tokenizer = Tokenizer("$")
    assert tokenizer.get_tokens_as_string() == "Error Token $"

def test_integer_single_digit():
    """45. Integer literal"""
    tokenizer = Tokenizer("5")
    assert tokenizer.get_tokens_as_string() == "5,<EOF>"

def test_integer_multiple_digits_1():
    """46. Integer literal with multiple digits"""
    tokenizer = Tokenizer("12345")
    assert tokenizer.get_tokens_as_string() == "12345,<EOF>"

def test_integer_multiple_digits_2():
    """47. Integer literal with multiple digits"""
    tokenizer = Tokenizer("298752789")
    assert tokenizer.get_tokens_as_string() == "298752789,<EOF>"

def test_integer_zero():
    """48. Integer literal zero"""
    tokenizer = Tokenizer("0")
    assert tokenizer.get_tokens_as_string() == "0,<EOF>"

def test_integer_negative():
    """49. Negative integer literal"""
    tokenizer = Tokenizer("-42")
    assert tokenizer.get_tokens_as_string() == "-,42,<EOF>"

def test_integer_with_leading_zeros():
    """50. Integer literal with leading zeros"""
    tokenizer = Tokenizer("00042")
    assert tokenizer.get_tokens_as_string() == "00042,<EOF>"

def test_float_decimal():
    """51. Float literal"""
    tokenizer = Tokenizer("3.14")
    assert tokenizer.get_tokens_as_string() == "3.14,<EOF>"

def test_float_no_leading():
    """52. Float literal without leading digit"""
    tokenizer = Tokenizer(".75")
    assert tokenizer.get_tokens_as_string() == ".75,<EOF>"

def test_float_no_trailing():
    """53. Float literal without trailing digit"""
    tokenizer = Tokenizer("2.")
    assert tokenizer.get_tokens_as_string() == "2.,<EOF>"

def test_float_negative():
    """54. Negative float literal"""
    tokenizer = Tokenizer("-0.001")
    assert tokenizer.get_tokens_as_string() == "-,0.001,<EOF>"

def test_float_negative_2():
    """55. Negative float literal"""
    tokenizer = Tokenizer("-3.5")
    assert tokenizer.get_tokens_as_string() == "-,3.5,<EOF>"

def test_float_exponent():
    """56. Float literal with exponent"""
    tokenizer = Tokenizer("-1.5e10")
    assert tokenizer.get_tokens_as_string() == "-,1.5e10,<EOF>"

def test_float_exponent_negative():
    """57. Float literal with negative exponent"""
    tokenizer = Tokenizer("2.3e-4")
    assert tokenizer.get_tokens_as_string() == "2.3e-4,<EOF>"

def test_float_exponent_no_leading():
    """58. Float literal with exponent and no leading digit"""
    tokenizer = Tokenizer(".5e2")
    assert tokenizer.get_tokens_as_string() == ".5e2,<EOF>"

def test_float_exponent_no_trailing():
    """59. Float literal with exponent and no trailing digit"""
    tokenizer = Tokenizer("3.e3")
    assert tokenizer.get_tokens_as_string() == "3.e3,<EOF>"

def test_float_only_exponent_error():
    """60. Float literal with only exponent"""
    tokenizer = Tokenizer(".e4")
    assert tokenizer.get_tokens_as_string() == ".,e4,<EOF>"

def test_string_simple():
    """61. String literal"""
    tokenizer = Tokenizer('"hello"')
    assert tokenizer.get_tokens_as_string() == "hello,<EOF>"

def test_string_with_newline_char():
    """62. String literal with escape sequences"""
    tokenizer = Tokenizer('"Line1\nLine2"')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: Line1"

def test_string_with_tab_char():
    """63. String literal with escape sequences"""
    tokenizer = Tokenizer('"Column1\tColumn2"')
    assert tokenizer.get_tokens_as_string() == "Column1\tColumn2,<EOF>"

def test_string_empty():
    """64. Empty string literal"""
    tokenizer = Tokenizer('""')
    assert tokenizer.get_tokens_as_string() == ",<EOF>"

def test_string_escape_backslash():
    """65. String with escaped backslash"""
    tokenizer = Tokenizer('"Path: C:\\\\Users"')
    assert tokenizer.get_tokens_as_string() == "Path: C:\\\\Users,<EOF>"

def test_string_escape_quote():
    """66. String with escaped double quote"""
    tokenizer = Tokenizer(r'"He said \"Hello\""')
    assert tokenizer.get_tokens_as_string() == 'He said \\"Hello\\",<EOF>'

def test_string_escape_newline():
    """67. String with escaped newline"""
    tokenizer = Tokenizer(r'"Line1\nLine2"')
    assert tokenizer.get_tokens_as_string() == r"Line1\nLine2,<EOF>"

def test_string_escape_tab():
    """68. String with escaped tab"""
    tokenizer = Tokenizer(r'"Col1\tCol2"')
    assert tokenizer.get_tokens_as_string() == r"Col1\tCol2,<EOF>"

def test_string_escape_carriage_return():
    """69. String with escaped carriage return"""
    tokenizer = Tokenizer(r'"Text\rOverwrite"')
    assert tokenizer.get_tokens_as_string() == r"Text\rOverwrite,<EOF>"

def test_string_escape_backspace():
    """70. String with escaped backspace"""
    tokenizer = Tokenizer(r'"ABC\b"')
    assert tokenizer.get_tokens_as_string() == r"ABC\b,<EOF>"

def test_string_escape_formfeed():
    """71. String with escaped form feed"""
    tokenizer = Tokenizer(r'"Page1\fPage2"')
    assert tokenizer.get_tokens_as_string() == r"Page1\fPage2,<EOF>"

def test_string_all_escapes():
    """72. String with all valid escape sequences"""
    tokenizer = Tokenizer(r'"Escapes: \b\f\r\n\t\"\\End"')
    assert tokenizer.get_tokens_as_string() == r'Escapes: \b\f\r\n\t\"\\End,<EOF>'

def test_string_illegal_escape_x():
    """73. String with illegal escape sequence \\x"""
    tokenizer = Tokenizer(r'"Bad\xEscape"')
    assert tokenizer.get_tokens_as_string() == r"Illegal Escape In String: Bad\x"

def test_string_illegal_escape_a():
    """74. String with illegal escape sequence \\a"""
    tokenizer = Tokenizer(r'"Bad\aEscape"')
    assert tokenizer.get_tokens_as_string() == r"Illegal Escape In String: Bad\a"

def test_string_illegal_escape_digit():
    """75. String with illegal escape sequence \\1"""
    tokenizer = Tokenizer(r'"Bad\1Escape"')
    assert tokenizer.get_tokens_as_string() == r"Illegal Escape In String: Bad\1"

def test_string_illegal_escape_v():
    """76. String with illegal escape sequence \\v"""
    tokenizer = Tokenizer(r'"Bad\vEscape"')
    assert tokenizer.get_tokens_as_string() == r"Illegal Escape In String: Bad\v"

def test_string_unclosed_newline():
    """77. Unclosed string with newline"""
    tokenizer = Tokenizer('"Not closed\n')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: Not closed"

def test_string_unclosed_eof():
    """78. Unclosed string at EOF"""
    tokenizer = Tokenizer('"Not closed')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: Not closed"

def test_string_unclosed_carriage_return():
    """79. Unclosed string with carriage return"""
    tokenizer = Tokenizer('"Not closed\r')
    assert tokenizer.get_tokens_as_string() == "Unclosed String: Not closed"

def test_string_with_spaces():
    """80. String with multiple spaces"""
    tokenizer = Tokenizer('"   spaces   "')
    assert tokenizer.get_tokens_as_string() == "   spaces   ,<EOF>"

def test_string_with_special_chars():
    """81. String with special characters"""
    tokenizer = Tokenizer('"Hello @#$%^&*()!"')
    assert tokenizer.get_tokens_as_string() == "Hello @#$%^&*()!,<EOF>"

def test_string_with_numbers():
    """82. String with numbers"""
    tokenizer = Tokenizer('"Code: 12345"')
    assert tokenizer.get_tokens_as_string() == "Code: 12345,<EOF>"

def test_identifier_simple():
    """83. Identifier"""
    tokenizer = Tokenizer("x")
    assert tokenizer.get_tokens_as_string() == "x,<EOF>"

def test_identifier_multiple_chars():
    """84. Identifier with multiple characters"""
    tokenizer = Tokenizer("variableName")
    assert tokenizer.get_tokens_as_string() == "variableName,<EOF>"

def test_identifier_with_underscores():
    """85. Identifier with underscores"""
    tokenizer = Tokenizer("var_name_test")
    assert tokenizer.get_tokens_as_string() == "var_name_test,<EOF>"

def test_identifier_starting_with_underscore():
    """86. Identifier starting with underscore"""
    tokenizer = Tokenizer("_hiddenVar")
    assert tokenizer.get_tokens_as_string() == "_hiddenVar,<EOF>"

def test_identifier_with_digits():
    """87. Identifier with digits"""
    tokenizer = Tokenizer("var123")
    assert tokenizer.get_tokens_as_string() == "var123,<EOF>"

def test_identifier_invalid_1():
    """88. Long identifier"""
    tokenizer = Tokenizer("0987variable")
    assert tokenizer.get_tokens_as_string() == "0987,variable,<EOF>"

def test_line_comment():
    """89. Line comment"""
    tokenizer = Tokenizer("// This is a comment")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_line_comment_with_code():
    """90. Line comment with code after"""
    tokenizer = Tokenizer("int x; // variable declaration")
    assert tokenizer.get_tokens_as_string() == "int,x,;,<EOF>"

def test_block_comment_single_line():
    """91. Block comment in single line"""
    tokenizer = Tokenizer("/* This is a block comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comment_multi_line():
    """92. Block comment in multiple lines"""
    tokenizer = Tokenizer("/* This is a\n multi-line \n block comment */")
    assert tokenizer.get_tokens_as_string() == "<EOF>"

def test_block_comment_with_code():
    """93. Block comment with code before and after"""
    tokenizer = Tokenizer("int x; /* comment */ float y;")
    assert tokenizer.get_tokens_as_string() == "int,x,;,float,y,;,<EOF>"

def test_integer_in_expression():
    """94. Mixed: integers and operator"""
    tokenizer = Tokenizer("5+10")
    assert tokenizer.get_tokens_as_string() == "5,+,10,<EOF>"

def test_float_in_expression():
    """95. Mixed: floats and operator"""
    tokenizer = Tokenizer("3.5*2.0")
    assert tokenizer.get_tokens_as_string() == "3.5,*,2.0,<EOF>"

def test_string_in_expression():
    """96. Mixed: string concatenation"""
    tokenizer = Tokenizer('"Hello, " + "World!"')
    assert tokenizer.get_tokens_as_string() == "Hello, ,+,World!,<EOF>"

def test_identifier_in_expression():
    """97. Mixed: identifiers and operators"""
    tokenizer = Tokenizer("a && b || c")
    assert tokenizer.get_tokens_as_string() == "a,&&,b,||,c,<EOF>"
def test_mixed_tokens():
    """98. Mixed: various tokens"""
    tokenizer = Tokenizer("int x = 10; // variable")
    assert tokenizer.get_tokens_as_string() == "int,x,=,10,;,<EOF>"

def test_complex_expression():
    """99. Complex: variable declaration"""
    tokenizer = Tokenizer("auto x = 5 + 3 * 2;")
    assert tokenizer.get_tokens_as_string() == "auto,x,=,5,+,3,*,2,;,<EOF>"

def test_complex_statement():
    """100. Complex: if statement with block"""
    tokenizer = Tokenizer("if (x > 0) { printInt(x); }")
    assert tokenizer.get_tokens_as_string() == "if,(,x,>,0,),{,printInt,(,x,),;,},<EOF>"

def test_complex_function():
    """101. Complex: function declaration"""
    tokenizer = Tokenizer("void greet(string name) { printString(name); }")
    assert tokenizer.get_tokens_as_string() == "void,greet,(,string,name,),{,printString,(,name,),;,},<EOF>"

def test_complex_struct():
    """102. Complex: struct declaration"""
    tokenizer = Tokenizer("struct Point { int x; int y; };")
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,int,y,;,},;,<EOF>"

def test_complex_loop():
    """103. Complex: for loop"""
    tokenizer = Tokenizer("for (auto i = 0; i < 10; ++i) { printInt(i); }")
    assert tokenizer.get_tokens_as_string() == "for,(,auto,i,=,0,;,i,<,10,;,++,i,),{,printInt,(,i,),;,},<EOF>"

def test_random_keywords_place():
    """104. Random: keywords in various places"""
    tokenizer = Tokenizer("nothing void something struct else")
    assert tokenizer.get_tokens_as_string() == "nothing,void,something,struct,else,<EOF>"

def test_random_operators_place():
    """105. Random: operators in various places"""
    tokenizer = Tokenizer("a + b - c * d / e % f == g != h < i > j <= k >= l && m || n !o ++p --q = r .s")
    assert tokenizer.get_tokens_as_string() == "a,+,b,-,c,*,d,/,e,%,f,==,g,!=,h,<,i,>,j,<=,k,>=,l,&&,m,||,n,!,o,++,p,--,q,=,r,.,s,<EOF>"

def test_random_separators_place():
    """106. Random: separators in various places"""
    tokenizer = Tokenizer("func(a,b); {x:y, z;}")
    assert tokenizer.get_tokens_as_string() == "func,(,a,,,b,),;,{,x,:,y,,,z,;,},<EOF>"

def test_mixed_comments_code():
    """107. Mixed: comments and code"""
    tokenizer = Tokenizer("int x; // comment\n/* block comment */ float y;")
    assert tokenizer.get_tokens_as_string() == "int,x,;,float,y,;,<EOF>"

def test_complex_expression_2():
    """108. Complex: nested expressions"""
    tokenizer = Tokenizer("((a + b) * (c - d)) / e")
    assert tokenizer.get_tokens_as_string() == "(,(,a,+,b,),*,(,c,-,d,),),/,e,<EOF>"

def test_complex_string():
    """109. Complex: string with multiple escapes"""
    tokenizer = Tokenizer(r'"Line1\nLine2\tTabbed\\Backslash\""')
    assert tokenizer.get_tokens_as_string() == r'Line1\nLine2\tTabbed\\Backslash\",<EOF>'

def test_complex_program():
    """110. Complex: full program snippet"""
    source = """
    struct Point {
        int x;
        int y;
    };
    void main() {
        auto p = Point();
        p.x = 10;
        p.y = 20;
        if (p.x < p.y) {
            printInt(p.x);
        } else {
            printInt(p.y);
        }
    }
    """
    tokenizer = Tokenizer(source)
    assert tokenizer.get_tokens_as_string() == "struct,Point,{,int,x,;,int,y,;,},;,void,main,(,),{,auto,p,=,Point,(,),;,p,.,x,=,10,;,p,.,y,=,20,;,if,(,p,.,x,<,p,.,y,),{,printInt,(,p,.,x,),;,},else,{,printInt,(,p,.,y,),;,},},<EOF>"
