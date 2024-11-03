#!/usr/bin/env python3

import glob
import os

num_header_line = 13

def substitute_macro(line, name, value):
    n_size = len(name)
    start = 0
    while True:
        size = len(line)
        i = line.find(name, start)
        if i < 0:
            break
        j = i + n_size
        assert line[i:j] == name
        if size > j:
             if line[j].isalnum():
                start = i + 1
                continue
        line = line[:i] + value + line[j:]
        start = i
    return line

def process_line(line):
    line_orig = line
    line = substitute_macro(line, r"\nn", r"\nonumber")
    line = substitute_macro(line, r"\ba", r"\begin{align}")
    line = substitute_macro(line, r"\ea", r"\end{align}")
    line = substitute_macro(line, r"\bra", r"\big\ra")
    line = substitute_macro(line, r"\bla", r"\big\la")
    line = substitute_macro(line, r"\Bra", r"\Big\ra")
    line = substitute_macro(line, r"\Bla", r"\Big\la")
    line = substitute_macro(line, r"\ra", r"\rangle")
    line = substitute_macro(line, r"\la", r"\langle")
    line = substitute_macro(line, r"\ud", r"\mathrm{d}")
    if line != line_orig:
        print(f"process_line '{line_orig}' -> '{line}'")
    return line

def process_file(fn):
    print(f"Process '{fn}'.")
    with open(fn) as f:
        line_list = f.readlines()
    fn_new = fn + ".new"
    line_new_list = line_list[:num_header_line]
    for line in line_list[num_header_line:]:
        l_new = process_line(line)
        line_new_list.append(l_new)
    with open(fn_new, 'w') as f:
        f.writelines(line_new_list)
    os.rename(fn_new, fn)

fn_list = glob.glob("*.md")

for fn in fn_list:
    process_file(fn)
