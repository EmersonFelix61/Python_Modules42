class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        GardenError.__init__(self, message)


def plant_error(plant_name: str) -> None:
    raise PlantError(f"The {plant_name} plant is wilting!")


def water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def tester() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing PlantError...")
        plant_error("Tomato")
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    try:
        print("Testing WaterError...")
        water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")

    try:
        plant_error("Tomato")
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        water_error()
    except GardenError as error:
        print(f"Caught GardenError: {error}\n")


if __name__ == "__main__":
    tester()
    print("All custom error types work correctly")
