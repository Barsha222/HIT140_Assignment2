def tokenize_expression(expr: str):
    
    ##final tokenizer version for the assignment
    ##trying to handle most cases properly now:
    ##numbers, operators, brackets, unary minus, and implicit multiplication
    ##if something weird shows up (like unary +), It will return None

    tokens = []
    index = 0
    length = len(expr)

    ##small helper so I don't repeat the append code everywhere
    def add_token(kind, value):
        tokens.append((kind, value))

    while index < length:
        ch = expr[index]

        ##ignoring spaces completely
        if ch.isspace():
            index += 1
            continue

        ##reading a number (still only whole numbers)
        if ch.isdigit():
            start = index
            while index < length and expr[index].isdigit():
                index += 1

            number_value = expr[start:index]
            add_token("NUM", number_value)

            ##if a number is followed by '(' then it's like 2(3+4) → implicit *
            if index < length and expr[index] == "(":
                add_token("OP", "*")
            continue

        ##forleft bracket
        if ch == "(":
            # if something like "2(" or ")(" happens, treat it as implicit *
            if tokens and (tokens[-1][0] == "NUM" or tokens[-1][0] == "RPAREN"):
                add_token("OP", "*")

            add_token("LPAREN", "(")
            index += 1
            continue

        ##for right bracket
        if ch == ")":
            add_token("RPAREN", ")")
            index += 1
            continue

        ##for operators: + - * / l
        if ch in "+-*/l":

            ##unary + is not allowed in this assignment
            if ch == "+":
                if not tokens or tokens[-1][0] in ("OP", "LPAREN"):
                    return None

            ##unary minus is allowed (e.g. -5 or -(3+2))
            if ch == "-":
                if not tokens or tokens[-1][0] in ("OP", "LPAREN"):
                    add_token("OP", "-")
                    index += 1
                    continue

            ##normal operator
            add_token("OP", ch)
            index += 1
            continue

        ##anything else will be considered invalid
        return None

    ##add end token so parser knows input is finished
    add_token("END", "")
    return tokens
