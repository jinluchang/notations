#!/usr/bin/env python3

import glob
import os

num_header_line = 13

def process_file(fn):
    with open(fn) as f:
        lines = f.readlines()
    fn_new = fn + ".new"
    with open(fn_new, 'w') as f:
        f.writelines(lines)
    os.rename(fn_new, fn)

fn_list = glob.glob("*.md")

for fn in fn_list:
    process_file(fn)
