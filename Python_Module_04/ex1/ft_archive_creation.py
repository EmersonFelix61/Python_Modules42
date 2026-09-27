#!/usr/bin/env python3

import sys


def ft_ancient_text() -> str | None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return None
    print("=== Cyber Archives Recovery & Preservation ===")
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
        return None
    finally:
        if archive is not None:
            archive.close()
            print(f"File '{sys.argv[1]}' closed.\n")
    return content


def ft_transform_data(content: str) -> None:
    lines = content.splitlines()
    new_lines = []

    for line in lines:
        line += "#"
        new_lines.append(line)

    new_content = "\n".join(new_lines) + "\n"
    print("Transform data:")
    print("---\n")
    print(new_content)
    print("---")
    file_name = input("Enter new file name (or empty): ")
    new_file = None

    if file_name != "":
        try:
            new_file = open(file_name, "w")
            print(f"Saving data to '{file_name}'.")
            new_file.write(new_content)
            print(f"Data saved in file '{file_name}'.")
        except PermissionError as e:
            print(e)
        finally:
            if new_file is not None:
                new_file.close()
    else:
        print("Not saving data.")


def main() -> None:
    content = ft_ancient_text()
    if content is None:
        return
    ft_transform_data(content)


if __name__ == "__main__":
    main()
