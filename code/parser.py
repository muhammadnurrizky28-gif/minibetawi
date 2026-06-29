from ast_node import *

class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self, token_type):
        token = self.current()
        if token.type == token_type:
            self.pos += 1
            return token
        raise Exception(
            f"Expected {token_type}, dapat {token.type}"
        )

    def parse(self):
        statements = []
        while self.current().type != "T_EOF":
            statements.append(self.statement())
        return Program(statements)

    def statement(self):
        token = self.current()

        if token.type == "T_NGOMONG":
            return self.print_stmt()

        if token.type == "T_KALO":
            return self.if_stmt()

        if token.type == "T_SELAGI":
            return self.while_stmt()

        if token.type == "T_IDENT":
            return self.assignment()

        raise Exception(
            f"Statement tidak dikenal: {token.type}"
        )

    def assignment(self):
        name = self.eat("T_IDENT").value
        self.eat("T_ASSIGN")

        if self.current().type == "T_TANYA":
            self.eat("T_TANYA")
            self.eat("T_LPAREN")
            prompt = self.eat("T_STRING").value
            self.eat("T_RPAREN")
            return Assignment(name, Input(prompt))

        value = self.expression()
        return Assignment(name, value)

    def if_stmt(self):
        self.eat("T_KALO")
        condition = self.expression()
        self.eat("T_LBRACE")
        then_body = self.statement_list()
        self.eat("T_RBRACE")
        self.eat("T_SELAEN")
        self.eat("T_LBRACE")
        else_body = self.statement_list()
        self.eat("T_RBRACE")
        return If(condition, then_body, else_body)

    def while_stmt(self):
        self.eat("T_SELAGI")
        condition = self.expression()
        self.eat("T_LBRACE")
        body = self.statement_list()
        self.eat("T_RBRACE")
        return While(condition, body)

    def statement_list(self):
        statements = []
        while self.current().type not in ("T_RBRACE", "T_EOF"):
            statements.append(self.statement())
        return statements

    def print_stmt(self):
        self.eat("T_NGOMONG")
        self.eat("T_LPAREN")
        expr = self.expression()
        self.eat("T_RPAREN")
        return Print(expr)

    def expression(self):
        return self.or_expr()

    def or_expr(self):
        node = self.and_expr()
        while self.current().type == "T_ATAWA":
            self.eat("T_ATAWA")
            node = BinaryOp(node, "or", self.and_expr())
        return node

    def and_expr(self):
        node = self.not_expr()
        while self.current().type == "T_AMA":
            self.eat("T_AMA")
            node = BinaryOp(node, "and", self.not_expr())
        return node

    def not_expr(self):
        if self.current().type == "T_KAGA":
            self.eat("T_KAGA")
            return UnaryOp("not", self.not_expr())
        return self.comparison()

    def comparison(self):
        node = self.additive()
        while self.current().type in (
            "T_EQ",
            "T_NEQ",
            "T_LT",
            "T_GT",
            "T_LTE",
            "T_GTE",
        ):
            operator = self.eat(self.current().type).value
            node = BinaryOp(node, operator, self.additive())
        return node

    def additive(self):
        node = self.multiplicative()
        while self.current().type in ("T_PLUS", "T_MINUS"):
            operator = self.eat(self.current().type).value
            node = BinaryOp(node, operator, self.multiplicative())
        return node

    def multiplicative(self):
        node = self.factor()
        while self.current().type in ("T_MUL", "T_DIV", "T_MOD"):
            operator = self.eat(self.current().type).value
            node = BinaryOp(node, operator, self.factor())
        return node

    def factor(self):
        token = self.current()
        if token.type == "T_NUMBER":
            self.eat("T_NUMBER")
            return Number(token.value)
        if token.type == "T_STRING":
            self.eat("T_STRING")
            return String(token.value)
        if token.type == "T_BENER":
            self.eat("T_BENER")
            return Boolean(True)
        if token.type == "T_SALAH":
            self.eat("T_SALAH")
            return Boolean(False)
        if token.type == "T_TANYA":
            self.eat("T_TANYA")
            self.eat("T_LPAREN")
            prompt = self.eat("T_STRING").value
            self.eat("T_RPAREN")
            return Input(prompt)
        if token.type == "T_IDENT":
            self.eat("T_IDENT")
            return Identifier(token.value)
        if token.type == "T_LPAREN":
            self.eat("T_LPAREN")
            node = self.expression()
            self.eat("T_RPAREN")
            return node
        if token.type == "T_MINUS":
            self.eat("T_MINUS")
            return UnaryOp("-", self.factor())
        raise Exception(
            f"Expression tidak valid {token.type}"
        )
