#!/usr/bin/env python3

def secure_archive(
        filename: str,
        action: int = 1,
        content: str = ""
) -> tuple[bool, str]:
    try:
        if action == 1:
            with open(filename, "r") as file:
                content = file.read()
            return (True, content)

        elif action == 0:
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")

        else:
            return (False, "Invalid action")

    except (FileNotFoundError, PermissionError) as e:
        return (False, f"{e}")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/wrong/file/path"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/sudoers.d/bocal"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    content = secure_archive("create_file.txt")
    print(content)
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("create_file.txt", 0, content[1]))


if __name__ == "__main__":
    main()
