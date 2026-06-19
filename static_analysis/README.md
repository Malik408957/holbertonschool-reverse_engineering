# Holberton School - Reverse Engineering: Static Analysis

This repository contains the first challenge of the static analysis and reverse engineering module.

## Challenge 0: main0
* **Objective:** Find the hidden password/flag inside the statically linked binary `./main0`.
* **Solution Method:** Extracted the "Stack String" by analyzing the `check_flag` function using GDB (`disassemble check_flag`).
* **Flag discovered:** `HOLB{Reverse_Engineering_is_Fun}`
EOF
