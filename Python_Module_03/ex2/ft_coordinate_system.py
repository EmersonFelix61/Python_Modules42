#!/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        param = ""
        try:
            inputs = input(
                "Enter new coordinates as floats in format 'x,y,z': "
            ).split(",")
            try:
                inputs[3]
                print("Invalid syntax")
            except Exception:
                param0, param1, param2 = inputs[0], inputs[1], inputs[2]
                param = param0
                param0f = float(param)
                param = param1
                param1f = float(param)
                param = param2
                param2f = float(param)
                return param0f, param1f, param2f

        except IndexError:
            print("Invalid syntax")
        except ValueError as e:
            print(f"Error on parameter '{param}':", e)


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")

    pos = get_player_pos()
    x1, y1, z1 = pos
    print("Got a first tuple:", pos)
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(distance, 4)}")

    print("Get a second set of coordenates")
    x2, y2, z2 = get_player_pos()
    print(f"Got a second tuple: {x2, y2, z2}")
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance2 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(
        f"Distance between the 2 sets of cooredenates: {round(distance2, 4)}"
    )


if __name__ == "__main__":
    main()
