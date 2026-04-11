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
