#!/bin/env python3

import sys


def inventory_system() -> None:
    args = sys.argv[1:]
    inventory: dict[str, int] = {}
    for item in args:
        try:
            key_value = item.split(":")
            item_name = key_value[0]
            quantity = key_value[1]

            if item_name not in inventory:
                inventory[item_name] = int(quantity)
            else:
                print(f"Redundant item {item_name} - discarding")
        except IndexError as e:
            print(f"Error - invalid parameter {e}")
        except ValueError as e:
            print(f"Quantity error for {item_name}: {e}")

    total_values = sum(inventory.values())
    print("Got inventory:", inventory)
    print("Item list:", list(inventory.keys()))
    print(f"Total quantity of the {len(inventory)} items: {total_values}")

    most_item = ""
    most_quantity = 0
    least_item = ""
    least_quantity = total_values
    for item in inventory:
        if inventory[item] > most_quantity:
            most_quantity = inventory[item]
            most_item = item
        if inventory[item] < least_quantity:
            least_quantity = inventory[item]
            least_item = item
        print(
            f"Item {item} represents "
            f"{round(inventory[item] / total_values * 100, 1)}%"
        )
    print(
        f"Item most abundant: {most_item} "
        f"with quantity {most_quantity}"
    )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {least_quantity}"
    )
    inventory.update({"Magic_tem": 1})
    print("Update inventory: ", inventory)


if __name__ == "__main__":
    inventory_system()
