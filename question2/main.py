from tokenizer import tokenize_expression
from parser import P
from evaluator import eval_tree

expr = "4 + 2"
expr = "2"
tokens = tokenize_expression(expr)

new_parser = P(tokens)
parsed = new_parser.parse()
print(eval_tree(parsed))