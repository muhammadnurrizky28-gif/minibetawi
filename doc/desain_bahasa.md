# Desain Bahasa BetawiCode

## Deskripsi

BetawiCode adalah bahasa pemrograman sederhana yang dirancang menggunakan kosakata Bahasa Betawi sebagai pengganti keyword Python. Bahasa ini dibuat untuk memenuhi tugas Mini Compiler dengan tahapan Lexer, Parser, AST, Semantic Analysis, Code Optimization, dan Code Generation.

## Tujuan

Bahasa BetawiCode dirancang untuk:

* Menampilkan output ke layar.
* Menerima input dari pengguna.
* Melakukan operasi aritmatika.
* Melakukan percabangan.
* Melakukan perulangan.
* Diterjemahkan menjadi kode Python.

## Daftar Keyword

| Keyword Betawi | Fungsi             | Python |
| -------------- | ------------------ | ------ |
| ngomong        | Menampilkan output | print  |
| tanya          | Menerima input     | input  |
| kalo           | Percabangan jika   | if     |
| selaen         | Percabangan selain | else   |
| selagi         | Perulangan         | while  |
| bener          | Nilai benar        | True   |
| salah          | Nilai salah        | False  |
| ama            | Operator AND       | and    |
| atawa          | Operator OR        | or     |
| kaga           | Operator NOT       | not    |

## Contoh Program

```betawi
nama = tanya("Siape nama lu?")

ngomong("Halo")
ngomong(nama)
```

Hasil Translasi Python:

```python
nama = input("Siape nama lu?")

print("Halo")
print(nama)
```
