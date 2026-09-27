#!/bin/env python3

import random

ALL_ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "untouchable",
    "Boss Slayer",
    "Sharp Mind",
    "Survivor",
    "Unstoppable",
    "First Steps",
    "Strategist",
    "Treasure Hunter"
]


def gen_player_achievements() -> set[str]:
    amount = random.randint(1, 5)
    return set(random.sample(ALL_ACHIEVEMENTS, amount))


def main() -> None:
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print("=== Achievement Tracker System ===\n")
    print("Player Alice: ", alice)
    print("Player Bob: ", bob)
    print("Player Charlie: ", charlie)
    print("Player Dylan: ", dylan)
    print()
    print("All distinct achievements: ", set.union(alice, bob, charlie, dylan))
    print()
    print("Common achievements:", set.intersection(alice, bob, charlie, dylan))
    print()
    print("Only Alice has: ", set.difference(alice, bob, charlie, dylan))
    print("Only Bob has: ", set.difference(bob, alice, charlie, dylan))
    print("Only Charlie has: ", set.difference(charlie, bob, alice, dylan))
    print("Only Dylan has: ", set.difference(dylan, bob, charlie, alice))
    print()
    print("Alice is missing: ", set(ALL_ACHIEVEMENTS).difference(alice))
    print("Bob is missing: ", set(ALL_ACHIEVEMENTS).difference(bob))
    print("Charlie is missing: ", set(ALL_ACHIEVEMENTS).difference(charlie))
    print("Dylan is missing: ", set(ALL_ACHIEVEMENTS).difference(dylan))


if __name__ == "__main__":
    main()
