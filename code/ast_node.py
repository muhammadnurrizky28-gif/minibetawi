class Program:
    def __init__(self, statements):
        self.statements = statements


class Number:
    def __init__(self, value):
        self.value = value


class String:
    def __init__(self, value):
        self.value = value


class Boolean:
    def __init__(self, value):
        self.value = value


class Identifier:
    def __init__(self, name):
        self.name = name


class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Print:
    def __init__(self, expr):
        self.expr = expr


class Input:
    def __init__(self, prompt):
        self.prompt = prompt


class BinaryOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class UnaryOp:
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand


class If:
    def __init__(self, condition, then_body, else_body):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body


class While:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
