class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = 0
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height
        self._age: int = 0
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age
        print(
            f"Plant created: "
            f"{self._name}: {self._height}cm, {self._age} days old"
        )

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return

        self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return

        self._age = new_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> str:
        return f"{self._name}: {self._height}cm, {self._age} days old"


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 11, 2)
    print("")

    rose.set_age(365)
    rose.set_height(10.5)
    print("")
    print(f"Height update: {rose.get_height()}")
    print(f"Age update: {rose.get_age()}")
    print("")
    rose.set_age(-366)
    rose.set_height(-11)
    print("")
    rose.show()
    print(f"Current state: {rose.show()}")


if __name__ == "__main__":
    main()
