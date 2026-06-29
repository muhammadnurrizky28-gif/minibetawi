from ast_node import *

class CodeGenerator:

    def generate(self, node, indent=0):
        if isinstance(node, Program):
            code = ""
            for stmt in node.statements:
                code += self.generate(stmt, indent)
            return code

        if isinstance(node, Assignment):
            return (
                f"{'    ' * indent}{node.name} = {self.generate(node.value)}\n"
            )

        if isinstance(node, Print):
            return (
                f"{'    ' * indent}print({self.generate(node.expr)})\n"
            )

        if isinstance(node, If):
            code = f"{'    ' * indent}if {self.generate(node.condition)}:\n"
            code += self._generate_block(node.then_body, indent + 1)
            if node.else_body:
                code += f"{'    ' * indent}else:\n"
                code += self._generate_block(node.else_body, indent + 1)
            return code

        if isinstance(node, While):
            code = f"{'    ' * indent}while {self.generate(node.condition)}:\n"
            code += self._generate_block(node.body, indent + 1)
            return code

        if isinstance(node, BinaryOp):
            return (
                f"({self.generate(node.left)} {node.op} {self.generate(node.right)})"
            )

        if isinstance(node, UnaryOp):
            if node.op == "-":
                return f"(-{self.generate(node.operand)})"
            return f"(not {self.generate(node.operand)})"

        if isinstance(node, Input):
            return f"input({repr(node.prompt)})"

        if isinstance(node, String):
            return repr(node.value)

        if isinstance(node, Boolean):
            return "True" if node.value else "False"

        if isinstance(node, Number):
            return str(node.value)

        if isinstance(node, Identifier):
            return node.name

        return ""

    def _generate_block(self, statements, indent):
        if not statements:
            return f"{'    ' * indent}pass\n"
        code = ""
        for stmt in statements:
            code += self.generate(stmt, indent)
        return code
