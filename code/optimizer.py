from ast_node import *

class Optimizer:

    def optimize(self, node):
        if isinstance(node, Program):
            statements = []
            for stmt in node.statements:
                optimized = self.optimize(stmt)
                if optimized is None:
                    continue
                if isinstance(optimized, list):
                    statements.extend(optimized)
                else:
                    statements.append(optimized)
            return Program(statements)

        elif isinstance(node, Assignment):
            return Assignment(node.name, self.optimize(node.value))

        elif isinstance(node, Print):
            return Print(self.optimize(node.expr))

        elif isinstance(node, BinaryOp):
            left = self.optimize(node.left)
            right = self.optimize(node.right)

            if isinstance(left, Number) and isinstance(right, Number):
                folded = self._fold_number(left.value, node.op, right.value)
                if folded is not None:
                    return folded

            if isinstance(left, Boolean) and isinstance(right, Boolean):
                folded = self._fold_boolean(left.value, node.op, right.value)
                if folded is not None:
                    return Boolean(folded)

            if isinstance(left, String) and isinstance(right, String) and node.op == "+":
                return String(left.value + right.value)

            return BinaryOp(left, node.op, right)

        elif isinstance(node, UnaryOp):
            operand = self.optimize(node.operand)
            if isinstance(operand, Number) and node.op == "-":
                return Number(-operand.value)
            if isinstance(operand, Boolean) and node.op == "not":
                return Boolean(not operand.value)
            return UnaryOp(node.op, operand)

        elif isinstance(node, If):
            condition = self.optimize(node.condition)
            then_body = []
            for stmt in node.then_body:
                optimized = self.optimize(stmt)
                if optimized is None:
                    continue
                if isinstance(optimized, list):
                    then_body.extend(optimized)
                else:
                    then_body.append(optimized)

            else_body = []
            for stmt in node.else_body:
                optimized = self.optimize(stmt)
                if optimized is None:
                    continue
                if isinstance(optimized, list):
                    else_body.extend(optimized)
                else:
                    else_body.append(optimized)

            if isinstance(condition, (Number, Boolean)):
                return then_body if bool(condition.value) else else_body

            return If(condition, then_body, else_body)

        elif isinstance(node, While):
            condition = self.optimize(node.condition)
            body = []
            for stmt in node.body:
                optimized = self.optimize(stmt)
                if optimized is None:
                    continue
                if isinstance(optimized, list):
                    body.extend(optimized)
                else:
                    body.append(optimized)

            if isinstance(condition, (Number, Boolean)) and not bool(condition.value):
                return None

            return While(condition, body)

        elif isinstance(node, Input):
            return node

        elif isinstance(node, String):
            return node

        elif isinstance(node, Number):
            return node

        elif isinstance(node, Boolean):
            return node

        elif isinstance(node, Identifier):
            return node

        return node

    def _fold_number(self, left_value, op, right_value):
        try:
            if op == "+":
                return Number(left_value + right_value)
            if op == "-":
                return Number(left_value - right_value)
            if op == "*":
                return Number(left_value * right_value)
            if op == "/":
                if right_value == 0:
                    return None
                return Number(left_value / right_value)
            if op == "%":
                if right_value == 0:
                    return None
                return Number(left_value % right_value)
            if op == "==":
                return Number(int(left_value == right_value))
            if op == "!=":
                return Number(int(left_value != right_value))
            if op == "<":
                return Number(int(left_value < right_value))
            if op == ">":
                return Number(int(left_value > right_value))
            if op == "<=":
                return Number(int(left_value <= right_value))
            if op == ">=":
                return Number(int(left_value >= right_value))
        except Exception:
            return None
        return None

    def _fold_boolean(self, left_value, op, right_value):
        try:
            if op == "and":
                return left_value and right_value
            if op == "or":
                return left_value or right_value
            if op == "==":
                return left_value == right_value
            if op == "!=":
                return left_value != right_value
        except Exception:
            return None
        return None
