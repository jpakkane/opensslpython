#!/usr/bin/env python3

import os, sys, subprocess

original = 'original.asm'
output = 'output.asm'

pc = subprocess.Popen(['./aes_x86_64.py'], stdout=subprocess.PIPE)

if pc.returncode != 0:
    sys.exit(pc.returncode)

open(output, 'wb').write(pc.stdout)

original_lines = open(original).read_lines()
output_lines = open(output).read_lines()

if len(original_lines) != len(output_lines):
    sys.exit('Output files have different amount of lines.')

for i in range(len(original_lines)):
    if original_lines[i] != output_lines[i]:
        print('Mismatch on line', i+1)
        print('Original:')
        print(original_lines[i])
        print('Generated:')
        print(output_lines[i])
        sys.exit(1)

print('Files are identical.')
