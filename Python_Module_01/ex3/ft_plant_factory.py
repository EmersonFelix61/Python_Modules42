class Plant:
    def __init__(self, name: str, height: float, age_: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_: int = age_

    def grow(self) -> None:
        if self.name == "Amorphophallus titanum":
            self.height -= 1
        elif self.name == "Clitoria fairchildiana":
            self.height += 1000000
        elif self.name == "Styela clava":
            self.height += 10
        elif self.name == "Dracunculus vulgaris":
            self.height += 20
        elif self.name == "Ginkgo biloba":
            self.height += 30

    def age(self) -> None:
        if self.name == "Amorphophallus titanum":
            self.age_ -= 1
        elif self.name == "Clitoria fairchildiana":
            self.age_ += 19
        elif self.name == "Styela clava":
            self.age_ += 11
        elif self.name == "Dracunculus vulgaris":
            self.age_ += 23
        elif self.name == "Ginkgo biloba":
            self.age_ += 8

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_} days old")


def main() -> None:
    plants = [
        Plant("Amorphophallus titanum", 1, 1),
        Plant("Clitoria fairchildiana", 11, 10),
        Plant("Styela clava", 6, 14),
        Plant("Dracunculus vulgaris", 23, 14),
        Plant("Ginkgo biloba", 3, 89),
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
