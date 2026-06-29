# Grammar Bahasa BetawiCode

## Token

### Keyword

```text
T_NGOMONG
T_TANYA
T_KALO
T_SELAEN
T_SELAGI
T_BENER
T_SALAH
T_AMA
T_ATAWA
T_KAGA
```

### Operator

```text
=
+
-
*
/
%
==
!=
<
>
<=
>=
```

## Grammar BNF

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

<expression> ::= <term>
               | <expression> "+" <term>
               | <expression> "-" <term>
               | <expression> "*" <term>
               | <expression> "/" <term>

<term> ::= NUMBER
         | STRING
         | IDENTIFIER
         | "bener"
         | "salah"
         | "tanya" "(" STRING ")"
```

## Contoh Parse Tree

Source Code:

```betawi
ngomong("Halo Dunia")
```

Parse Tree:

```text
Program
│
└── PrintStatement
    │
    ├── ngomong
    ├── (
    ├── "Halo Dunia"
    └── )
```

## Contoh AST

```text
PrintNode
│
└── "Halo Dunia"
```
