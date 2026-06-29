# BetawiCode Compiler

## Deskripsi

BetawiCode Compiler adalah Mini Compiler yang dibuat menggunakan bahasa Python untuk memenuhi tugas UAS Mata Kuliah Compiler.

Compiler ini menggunakan Bahasa Betawi sebagai bahasa pemrograman sumber (source language) dan menerjemahkannya menjadi kode Python.

---

## Fitur

- Lexer
- Parser
- Parse Tree
- Abstract Syntax Tree (AST)
- Semantic Analysis
- Code Optimization
- Code Generation
- Generate Python Code
- Build menjadi File EXE

---

## Struktur Project

```text
BetawiCompiler/
│
├── lexer.py
├── parser.py
├── parse_tree.py
├── ast_nodes.py
├── semantic.py
├── optimizer.py
├── code_generator.py
├── main.py
│
├── sample.bt
├── output.py
│
└── README.md
```

---

## Keyword Bahasa Betawi

| Betawi | Python |
|---------|---------|
| ngomong | print |
| tanya | input |
| kalo | if |
| selaen | else |
| selagi | while |
| bener | True |
| salah | False |
| ama | and |
| atawa | or |
| kaga | not |

---

## Contoh Program BetawiCode

```betawi
nama = tanya("Siape nama lu?")

ngomong("Halo")
ngomong(nama)
```

---

## Hasil Translasi Python

```python
nama = input("Siape nama lu?")

print("Halo")
print(nama)
```

---

## Grammar

```bnf
<program> ::= <statement_list>

<statement_list> ::= <statement>
                   | <statement> <statement_list>

<statement> ::= <assignment>
              | <print_stmt>
              | <if_stmt>
              | <while_stmt>

<assignment> ::= IDENTIFIER "=" <expression>

<print_stmt> ::= "ngomong"
                 "(" <expression> ")"

<if_stmt> ::= "kalo"
              <expression>
              "{"
              <statement_list>
              "}"
              "selaen"
              "{"
              <statement_list>
              "}"

<while_stmt> ::= "selagi"
                 <expression>
                 "{"
                 <statement_list>
                 "}"
```

---

## Cara Menjalankan Compiler

1. Clone atau Download Project

```bash
git clone https://github.com/username/BetawiCompiler.git
```

atau download ZIP.

---

2. Jalankan Compiler

```bash
python main.py
```

Compiler akan:

1. Membaca file `.bt`
2. Melakukan tokenisasi (Lexer)
3. Membentuk Parse Tree
4. Membentuk AST
5. Melakukan Semantic Analysis
6. Melakukan Code Optimization
7. Menghasilkan kode Python

---

### 3. Jalankan Hasil Generate

```bash
python output.py
```

---

## Contoh Output

```text
SOURCE CODE
nama = tanya("Siape nama lu?")

TOKEN
Token(T_IDENT,'nama')
Token(T_ASSIGN,'=')
Token(T_TANYA,'tanya')
...

PARSE TREE BERHASIL

SEMANTIC ANALYSIS BERHASIL

CODE OPTIMIZATION BERHASIL

CODE GENERATION BERHASIL

output.py berhasil dibuat
```

---

## Code Optimization

Compiler menggunakan beberapa teknik optimasi:

### Constant Folding

Sebelum:

```betawi
hasil = 10 + 5
```

Sesudah:

```python
hasil = 15
```

---

### Constant Propagation

Sebelum:

```betawi
a = 10
b = a
```

Sesudah:

```python
a = 10
b = 10
```

---

### Dead Code Elimination

Sebelum:

```betawi
kalo bener {
    ngomong("Masuk")
}
selaen {
    ngomong("Tidak")
}
```

Sesudah:

```python
print("Masuk")
```

---

## Build Menjadi EXE

Install PyInstaller:

```bash
pip install pyinstaller
```

Generate EXE:

```bash
pyinstaller --onefile main.py
```

Hasil EXE:

```text
dist/
└── main.exe
```

---

## Teknologi

- Python 3.x
- Regular Expression (Regex)
- PyInstaller

---

## Tahapan Compiler

```text
Source Code (.bt)
        │
        ▼
      Lexer
        │
        ▼
      Parser
        │
        ▼
    Parse Tree
        │
        ▼
       AST
        │
        ▼
Semantic Analysis
        │
        ▼
Code Optimization
        │
        ▼
Code Generation
        │
        ▼
    output.py
```
