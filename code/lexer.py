import re

class Token:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, line={self.line}, col={self.column})"


class LexerError(Exception):
    def __init__(self, message, line, column):
        super().__init__(
            f"Lexer Error pada baris {line}, kolom {column}: {message}"
        )
        self.line = line
        self.column = column


class Lexer:

    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.line = 1

    def tokenize(self):

        rules = [

            # Operator Perbandingan
            ('T_EQ', r'=='),
            ('T_NEQ', r'!='),
            ('T_LTE', r'<='),
            ('T_GTE', r'>='),

            # Operator
            ('T_LT', r'<'),
            ('T_GT', r'>'),
            ('T_ASSIGN', r'='),
            ('T_PLUS', r'\+'),
            ('T_MINUS', r'-'),
            ('T_MUL', r'\*'),
            ('T_DIV', r'/'),
            ('T_MOD', r'%'),

            # Tanda Baca
            ('T_LPAREN', r'\('),
            ('T_RPAREN', r'\)'),
            ('T_LBRACE', r'\{'),
            ('T_RBRACE', r'\}'),
            ('T_COMMA', r','),

            # Literal
            ('T_NUMBER', r'\d+(\.\d+)?'),
            ('T_STRING', r'"([^"\\]|\\.)*"'),

            # Identifier
            ('T_IDENT', r'[a-zA-Z_][a-zA-Z0-9_]*'),

            # Abaikan
            ('SKIP', r'[ \t\r]+'),
            ('NEWLINE', r'\n'),
            ('COMMENT', r'#[^\n]*'),
        ]

        regex_parts = []

        for name, pattern in rules:
            regex_parts.append(
                f'(?P<{name}>{pattern})'
            )

        master_regex = re.compile(
            '|'.join(regex_parts)
        )

        keywords = {

            # Keyword Betawi
            'ngomong': 'T_NGOMONG',
            'tanya': 'T_TANYA',

            'kalo': 'T_KALO',
            'selaen': 'T_SELAEN',
            'selagi': 'T_SELAGI',

            'bener': 'T_BENER',
            'salah': 'T_SALAH',

            'ama': 'T_AMA',
            'atawa': 'T_ATAWA',
            'kaga': 'T_KAGA'
        }

        pos = 0

        while pos < len(self.text):

            match = master_regex.match(
                self.text,
                pos
            )

            if not match:

                last_newline = self.text.rfind(
                    '\n',
                    0,
                    pos
                )

                column = (
                    pos - last_newline
                    if last_newline != -1
                    else pos + 1
                )

                raise LexerError(
                    f"Karakter tidak dikenal: {self.text[pos]}",
                    self.line,
                    column
                )

            token_type = match.lastgroup
            token_value = match.group(token_type)

            last_newline = self.text.rfind(
                '\n',
                0,
                pos
            )

            column = (
                pos - last_newline
                if last_newline != -1
                else pos + 1
            )

            # New Line
            if token_type == "NEWLINE":

                self.line += 1
                pos = match.end()
                continue

            # Skip Space / Comment
            if token_type in ("SKIP", "COMMENT"):

                pos = match.end()
                continue

            # Keyword
            if token_type == "T_IDENT":

                if token_value in keywords:

                    token_type = keywords[
                        token_value
                    ]

            # String Processing
            if token_type == "T_STRING":

                token_value = (
                    token_value[1:-1]
                    .replace('\\"', '"')
                    .replace('\\n', '\n')
                    .replace('\\t', '\t')
                    .replace('\\\\', '\\')
                )

            self.tokens.append(

                Token(
                    token_type,
                    token_value,
                    self.line,
                    column
                )
            )

            pos = match.end()

        self.tokens.append(

            Token(
                "T_EOF",
                None,
                self.line,
                1
            )
        )

        return self.tokens