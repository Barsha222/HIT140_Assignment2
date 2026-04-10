def tokenize_expression(expr):

    ##second attempt at tokenizer
    ##trying to fix unary minus and trying to make tokens a bit more consistent

    tokens = []
    i = 0

    while i < len(expr):
        ch = expr[i]

        ##skipping spaces
        if ch == " ":
            i += 1
            continue

        ##still only integers

        if ch.isdigit():
            num = ch
            i += 1
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(("NUM", num))
            continue

        ##handling unary minus but still not properly

        if ch == "-":
            if not tokens or tokens[-1][0] in ("OP", "LPAREN"):
                tokens.append(("OP", "UNARY_MINUS"))
            else:
                tokens.append(("OP", "-"))
            i += 1
            continue

        ##other operators and parentheses
        if ch in "+*/()":
            if ch == "(":
                tokens.append(("LPAREN", ch))
            elif ch == ")":
                tokens.append(("RPAREN", ch))
            else:
                tokens.append(("OP", ch))
            i += 1
            continue

        ##still ignoring unknown characters for now
        i += 1

    tokens.append(("END", ""))
    return tokens
