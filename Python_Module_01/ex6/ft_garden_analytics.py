class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._statistics = Plant.Statistics()

    class Statistics:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def register_grow(self) -> None:
            self._grow_calls += 1

        def register_age(self) -> None:
            self._age_calls += 1

        def register_show(self) -> None:
            self._show_calls += 1

        def display(self, plant_name: str) -> None:
            print(
                f"[statistics for {plant_name}]\n"
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, "
                f"{self._show_calls} show"
            )

    def display_statistics(self) -> None:
        self._statistics.display(self._name)

    def grow(self) -> None:
        self._height += 1
        self._statistics.register_grow()

    def age(self) -> None:
        self._age += 1
        self._statistics.register_age()

    def show(self) -> None:
        self._statistics.register_show()
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

    @staticmethod
    def check_age(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(
            self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self._bloom = False
        self._color = color

    def bloom(self) -> None:
        self._bloom = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloom:
            print(f"{self._name} is blooming beautifully")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(
            self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._height += 1.5
        self._seeds += 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    def __init__(
            self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._produce_shade_calls = 0

    def produce_shade(self) -> None:
        self._produce_shade_calls += 1

        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and "
            f"{self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def display_statistics(self) -> None:
        super().display_statistics()
        print(f"{self._produce_shade_calls} shade")


def display_plant_statistics(plant: Plant) -> None:
    plant.display_statistics()


def main() -> None:
    print("=== Garden statistics === ")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print()

    print("=== Flower")
    clitoria = Flower("Amorphophallus titanum", 25.5, 50, "Red")

    clitoria.show()
    display_plant_statistics(clitoria)

    print("[asking the Amorphophallus titanum to grow and bloom]")
    clitoria.grow()
    clitoria.age()
    clitoria.bloom()
    clitoria.show()

    display_plant_statistics(clitoria)
    print()

    print("=== Tree")
    bugreiro = Tree("Lithraea brasiliensis", 120.5, 1095, 5)

    bugreiro.show()
    display_plant_statistics(bugreiro)
    print("[asking the Lithraea brasiliensi to produce shade]")
    bugreiro.produce_shade()
    display_plant_statistics(bugreiro)
    print()

    print("=== Seed")
    sunflower = Seed("Helianthus annuus", 3.5, 127, "Yellow")
    sunflower.show()
    print("[asking Helianthus annuus to grow and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()

    sunflower.show()
    display_plant_statistics(sunflower)
    print()

    random = Plant.anonymous()
    random.show()
    display_plant_statistics(random)


if __name__ == "__main__":
    main()
