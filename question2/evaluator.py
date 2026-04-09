def tokenize_expression(expr):


    ##first attempt at tokenizer
    ##still need to handle unary minus and many other cases
    ##also haven't added implicit multiplication yet


    tokens = []
    i = 0

    while i < len(expr):
        ch = expr[i]

 ##skipping spaces

        if ch == " ":
            i += 1
            continue
        
        ##only integers for now
        
        if ch.isdigit():
            num = ch
            i += 1
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(("NUM", num))
            continue
        if ch in "+-*/()":

            ##unary minus not handled properly yet
            if ch == "(":
                tokens.append(("LPAREN", ch))
            elif ch == ")":
                tokens.append(("RPAREN", ch))
            else:
                tokens.append(("OP", ch))
            i += 1
            continue

        ##ignoring unknown characters
        i += 1

    tokens.append(("END", ""))
    return tokens
