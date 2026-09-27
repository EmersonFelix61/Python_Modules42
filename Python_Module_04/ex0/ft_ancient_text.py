#!/usr/bin/env python3

import sys


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print("Accessing file ", sys.argv[1])

    archive = None
    try:
        archive = open(sys.argv[1])
        content = archive.read()
        print("---\n")
        print(content)
        print("---")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    finally:
        if archive is not None:
            archive.close()
            print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
