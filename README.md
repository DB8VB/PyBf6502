# PyBf6502

Welcome to PyBf6502, a Brainf\*ck cross-compiler for the 6502, written in Python. It translates Brainf\*ck source code into 6502 assembly syntax of CrossPy6502. The program generates a BASIC stub so that the compiled file can be executed on the C64.

Translate Brainf\*uck code to assembly:
```bash
python3 PyBf6502.py example.bf
```
This will create `example.asm` that can be compiled in CrossPy6502 (see [https://github.com/DB8VB/crosspy6502](https://github.com/DB8VB/crosspy6502)):

```bash
python3 main.py example.asm example.bin
```

