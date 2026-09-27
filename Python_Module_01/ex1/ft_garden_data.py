class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    plants: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Tomato", 10, 20),
        Plant("Viscus", 23, 11)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()
    print("=== End of Program ===")


if __name__ == "__main__":
    main()
