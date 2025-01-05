# PyBf6502 - Translates Brainf*ck to 6502 Assembly syntax for CrossPy6502
# by DB8VB
# v0.1
# 2025-01-05
# License: BSD 2-Clause License

import sys

def brainfuck_to_6502(bf_code):

    assembly = []
    label_counter = 0
    loop_stack = []

    def new_label():
        nonlocal label_counter
        label = f"label_{label_counter}"
        label_counter += 1
        return label


    assembly.append("; 6502 Assembly for CrossPy6502 generated from PyBf6502")
    assembly.append("; Code for C64 PRG-executable file\n")

    assembly.append(".org $07FF ; Start address")
    assembly.append(".byte $01, $08, $0C, $08, $0A, $00, $9E, $20, $32, $30, $36, $34, $00, $00, $00\n\n")

    assembly.append("   LDX #$00")
    assembly.append("   LDA #$00")

    
    for char in bf_code:
        if char == '>':
            assembly.append("   INX")
        elif char == '<':
            assembly.append("   DEX")
        elif char == '+':
            assembly.append("   INC buffer,X")
        elif char == '-':
            assembly.append("   DEC buffer,X")
        elif char == '.':
            assembly.append("   LDA buffer,X")
            assembly.append("   JSR $FFD2")
        elif char == ',':
            assembly.append("   JSR $FFE4")
            assembly.append("   STA buffer,X")
        elif char == '[':
            start_label = new_label()
            end_label = new_label()
            loop_stack.append((start_label, end_label))
            assembly.append(f"{start_label}: ")
            assembly.append(f"   LDA buffer,X")
            assembly.append(f"   BEQ {end_label}")
        elif char == ']':
            if not loop_stack:
                raise SyntaxError("Mismatched closing bracket ]")
            start_label, end_label = loop_stack.pop()
            assembly.append(f"   JMP {start_label}")
            assembly.append(f"{end_label}:")

    if loop_stack:
        raise SyntaxError("Mismatched opening bracket [")

    assembly.append("   RTS")
    assembly.append("\nbuffer:")
    assembly.append(".res 1000   ; Allocate 1000 bytes Brainfuck memory - change if necessary")

    return '\n'.join(assembly)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Converts Brainfuck code to 6502 Assembly for CrossPy6502")
        print("Usage: python PyBf6502.py <brainfuck_file>")
        sys.exit(1)

    bf_file = sys.argv[1]
    try:
        with open(bf_file, 'r') as f:
            bf_code = f.read()
            asm_code = brainfuck_to_6502(bf_code)
            asm_file = bf_file.rsplit('.', 1)[0] + '.asm'
            with open(asm_file, 'w') as asm_f:
                asm_f.write(asm_code)
            print(f"6502 Assembly written to {asm_file}")
    except FileNotFoundError:
        print(f"File not found: {bf_file}")
        sys.exit(1)