from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from optimizer import Optimizer
from code_generator import CodeGenerator

with open(
    "sample.bt",
    "r",
    encoding="utf-8"
) as file:

    source = file.read()

print("SOURCE CODE")
print(source)

lexer = Lexer(source)

tokens = lexer.tokenize()

print("\nTOKEN")

for token in tokens:
    print(token)

parser = Parser(tokens)

ast = parser.parse()

print("\nPARSING SELESAI")

semantic = SemanticAnalyzer()

semantic.analyze(ast)

print("SEMANTIC ANALYSIS SELESAI")

optimizer = Optimizer()

ast = optimizer.optimize(ast)

generator = CodeGenerator()

python_code = generator.generate(ast)

with open(
    "output.py",
    "w",
    encoding="utf-8"
) as file:

    file.write(python_code)

print("\nHASIL PYTHON")

print(python_code)

print("\noutput.py berhasil dibuat")