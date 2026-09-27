#!/usr/bin/env python3

import sys


def ft_ancient_text() -> str | None:
    if len(sys.argv) != 2:
        sys.stdout.write("Usage: ft_stream_management.py <file>\n")
        return None

    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{sys.argv[1]}'\n")

    archive = None

    try:
        archive = open(sys.argv[1])
        content = archive.read()

        sys.stdout.write("---\n")
        sys.stdout.write(content)

        if not content.endswith("\n"):
            sys.stdout.write("\n")

        sys.stdout.write("---\n")

    except (FileNotFoundError, PermissionError) as e:
        sys.stderr.write(f"[ERROR] Error opening file '{sys.argv[1]}': {e}\n")
        return None

    finally:
        if archive is not None:
            archive.close()
            sys.stdout.write(f"File '{sys.argv[1]}' closed.\n")

    return content


def ft_transform_data(content: str) -> None:
    lines = content.splitlines()
    new_lines = []

    for line in lines:
        line += "#"
        new_lines.append(line)

    new_content = "\n".join(new_lines) + "\n"

    sys.stdout.write("Transform data:\n")
    sys.stdout.write("---\n")
    sys.stdout.write(new_content)
    sys.stdout.write("---\n")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    file_name = sys.stdin.readline().strip()

    if file_name == "":
        sys.stdout.write("Not saving data.\n")
        return

    new_file = None

    try:
        new_file = open(file_name, "w")

        sys.stdout.write(f"Saving data to '{file_name}'.\n")
        new_file.write(new_content)
        sys.stdout.write(f"Data saved in file '{file_name}'.\n")

    except PermissionError as e:
        sys.stderr.write(f"[ERROR] Error saving file '{file_name}': {e}\n")

    finally:
        if new_file is not None:
            new_file.close()


def main() -> None:
    content = ft_ancient_text()

    if content is None:
        return

    ft_transform_data(content)


if __name__ == "__main__":
    main()
