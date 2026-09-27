def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        2 / 0
    elif operation_number == 2:
        open("something.txt")
    elif operation_number == 3:
        "abc" + 123
    else:
        return


def test_error_types() -> None:
    operations = [
        0,
        1,
        2,
        3,
        4
    ]

    print("=== Garden Error Type Demo ===")
    for operation in operations:
        try:
            print(f"Testing operation {operation}...")
            garden_operations(operation)
            print("Operation completed successfully!\n")
        except (
                ValueError,
                ZeroDivisionError,
                FileNotFoundError,
                TypeError
        ) as error:
            print(f"Caught {error.__class__.__name__}: {error}")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
