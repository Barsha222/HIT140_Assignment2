class P:
    def __init__(self, toks):
        self.t = toks
        self.i = 0

    def cur(self):
        return self.t[self.i]

    def eat(self, k=None):
        c = self.cur()
        if k and c[0] != k:
            return None
        self.i += 1
        return c

    def parse(self):
        r = self.expr()
        if r is None:
            return None
        if self.cur()[0] != "END":
            return None
        return r

    # expr → term ((+|-) term)*
    def expr(self):
        x = self.term()
        if x is None:
            return None
        while self.cur()[0] == "OP" and self.cur()[1] in "+-":
            op = self.eat("OP")[1]
            y = self.term()
            if y is None:
                return None
            x = (op, x, y)
        return x

    # term → factor ((*|/|l) factor)*
    def term(self):
        x = self.factor()
        if x is None:
            return None
        while self.cur()[0] == "OP" and self.cur()[1] in "*/l":
            op = self.eat("OP")[1]
            y = self.factor()
            if y is None:
                return None
            x = (op, x, y)
        return x

    # factor → NUM | (expr) | -factor
    def factor(self):
        c = self.cur()

        # unary minus
        if c[0] == "OP" and c[1] == "-":
            self.eat("OP")
            f = self.factor()
            if f is None:
                return None
            return ("neg", f)

        # number
        if c[0] == "NUM":
            v = self.eat("NUM")[1]
            return int(v)

        # parentheses
        if c[0] == "LPAREN":
            self.eat("LPAREN")
            x = self.expr()
            if x is None:
                return None
            if self.cur()[0] != "RPAREN":
                return None
            self.eat("RPAREN")
            return x

        return None