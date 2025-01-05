# PyBf6502

Welcome to PyBf6502, a Brainf\*ck cross-compiler for the 6502 processor, developed in Python. This tool translates Brainf\*ck source code into 6502 assembly code compatible with the CrossPy6502 assembler (see: [https://github.com/DB8VB/crosspy6502](https://github.com/DB8VB/crosspy6502)). It also generates a BASIC stub, enabling the compiled file to run directly on a Commodore 64 (C64).

## How to Use PyBf6502

To translate Brainf\*ck code into 6502 assembly, run the following command:
```bash
python3 PyBf6502.py example.bf
```
This will create `example.asm`, an assembly file that can be compiled for the C64 using CrossPy6502:

```bash
python3 main.py example.asm example.prg
```

