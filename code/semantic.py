from ast_node import *

class SemanticAnalyzer:

    def __init__(self):
        self.symbol_table = {}

    def analyze(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.analyze(stmt)

        elif isinstance(node, Assignment):
            self.analyze(node.value)
            self.symbol_table[node.name] = True

        elif isinstance(node, Print):
            self.analyze(node.expr)

        elif isinstance(node, If):
            self.analyze(node.condition)
            for stmt in node.then_body:
                self.analyze(stmt)
            for stmt in node.else_body:
                self.analyze(stmt)

        elif isinstance(node, While):
            self.analyze(node.condition)
            for stmt in node.body:
                self.analyze(stmt)

        elif isinstance(node, BinaryOp):
            self.analyze(node.left)
            self.analyze(node.right)

        elif isinstance(node, UnaryOp):
            self.analyze(node.operand)

        elif isinstance(node, Identifier):
            if node.name not in self.symbol_table:
                raise Exception(
                    f"Variabel '{node.name}' belum dibuat"
                )

        elif isinstance(node, (Input, Number, String, Boolean)):
            return
