#!/bin/env python3
import sys


def print_program() -> None:
    print("=== Command Quest ===")
    total_args = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {total_args - 1}")
    if total_args == 1:
        print("No arguments provided!")
    i = 0
    for args in sys.argv[1:]:
        i += 1
        print(f"Argument {i}: {args}")
    print(f"Total arguments: {total_args}")


print_program()
