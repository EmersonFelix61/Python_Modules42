def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    inputs = [
        "25",
        "abc"
    ]
    print("=== Garden Temperature ===")
    for temp in inputs:
        print(f"Input data is '{temp}'")
        try:
            temperature = input_temperature(temp)
            print(f"Temperature is now: {temperature}°C\n")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
