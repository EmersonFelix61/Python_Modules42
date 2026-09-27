def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    return temperature


def test_temperature() -> None:
    inputs = [
        "25",
        "100",
        "-50",
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


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
