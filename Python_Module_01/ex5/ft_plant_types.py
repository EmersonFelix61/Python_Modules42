class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def grow(self) -> None:
        self._height += 1

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return

        self._age = age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height cant't be negative")
            print("Height update rejected")
            return

        self._height = height

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._bloom = False
        self._color = color

    def bloom(self) -> None:
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

        if self._bloom:
            print(f"{self._name} is blooming beatifully")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shad of "
            f"{self._height}cm long and " f"{self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow_days(self, days: int) -> None:
        for _ in range(days):
            super().grow()
        self._nutritional_value += days * 1

    def age_days(self, days: int) -> None:
        for _ in range(days):
            super().age()
        self._nutritional_value += days * 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def main() -> None:
    sunflower = Flower("Sunflower", 80, 60, "Yellow")
    sunflower.show()
    print("[asking the sunflower bloom]")
    sunflower.bloom()
    sunflower.show()
    print("\n")
    ficuslyaria = Tree("Ficus", 10.5, 365, 3.5)
    ficuslyaria.show()
    print("[asking the Ficus to produce shade]")
    ficuslyaria.produce_shade()
    print(end="\n")
    eggplant = Vegetable("Eggplant", 22, 28, "May", 80)
    eggplant.show()
    print("[Make Eggplant gorow and age for 20 days]")
    eggplant.grow_days(20)
    eggplant.age_days(20)
    eggplant.show()


if __name__ == "__main__":
    main()
