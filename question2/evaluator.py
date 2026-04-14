##Importing the tokenizer and parser so this file can run the whole program.
##tokenize_expression turns the input into tokens, and P builds the parse tree.

from tokenizer import tokenize_expression
from parser import P



###Evaluator Part
##This function takes the parse tree and works out the final answer.
def eval_tree(t):
    # number
    if isinstance(t, int):
        return t

    # unary neg
    if isinstance(t, tuple) and t[0] == "neg":
        v = eval_tree(t[1])
        if v is None:
            return None
        return -v

    # binary ops
    if isinstance(t, tuple) and len(t) == 3:
        op, a, b = t
        x = eval_tree(a)
        y = eval_tree(b)
        if x is None or y is None:
            return None

        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "l":   # division
            if y == 0:
                return None
            return x / y

    return None



##Output Formatting (Barsha)
##Functions to format the tree, tokens, and result

def format_tree(node):
    
    ##Turns the parse tree into prefix form.
    ##Handles numbers, unary negative, and normal operators
    
    if node is None:
        return "ERROR"

    ##Number
    if isinstance(node, int):
        return str(node)

    ##Unary negation
    if isinstance(node, tuple) and node[0] == "neg":
        return f"(neg {format_tree(node[1])})"

    ##Binary operator
    if isinstance(node, tuple) and len(node) == 3:
        op, left, right = node
        return f"({op} {format_tree(left)} {format_tree(right)})"

    return "ERROR"


def format_tokens(tokens):
    
    ##Formats the token list like:[NUM:3] [OP:+] [END]
    
    if tokens is None:
        return "ERROR"

    parts = []
    for kind, value in tokens:
        parts.append(f"[{kind}]" if value == "" else f"[{kind}:{value}]")
    return " ".join(parts)


def format_result(value):
    
    
    ##Whole numbers are printed without decimals.
    ##Floating values are rounded to 4 decimal places.
    
    if value is None:
        return "ERROR"

    ##Whole number
    if isinstance(value, int) or value.is_integer():
        return str(int(value))

    ##Decimal number
    return f"{value:.4f}"


def process_line(expr, tokenizer, parser_class, evaluator):
    
    ##Runs one expression through: tokenize,parse,evaluate and format.
    ##Returns the 4 output lines for that expression.
    
    tokens = tokenizer(expr)
    if tokens is None:
        return f"Input: {expr}\nTree: ERROR\nTokens: ERROR\nResult: ERROR\n"

    parser = parser_class(tokens)
    tree = parser.parse()
    if tree is None:
        return f"Input: {expr}\nTree: ERROR\nTokens: {format_tokens(tokens)}\nResult: ERROR\n"

    result = evaluator(tree)

    return (
        f"Input: {expr}\n"
        f"Tree: {format_tree(tree)}\n"
        f"Tokens: {format_tokens(tokens)}\n"
        f"Result: {format_result(result)}\n"
    )


