class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age: int = age

    def grow(self) -> None:
        if self._name == "Nephrolepis exaltata":
            self._height += 0.8
        elif self._name == "Erythroxylum vacciniifolium":
            self._height += 10000

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 2)}cm, {self._age} days old"
        )


def main() -> None:
    pot = Plant("Nephrolepis exaltata", 25, 11)
    pot.show()
    initial_height = pot._height
    print("=== Garden Plant Growth ===")
    for day in range(7):
        print(f"=== Day {day} ===")
        pot.grow()
        pot.age()
        pot.show()

    growth_week = pot._height - initial_height
    print(f"Growth this week: {round(growth_week, 2)}")


if __name__ == "__main__":
    main()
