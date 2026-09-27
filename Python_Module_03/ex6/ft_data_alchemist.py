#!/bin/env python3

import random

players: list[str] = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Eve",
    "frank"
]


def main() -> None:
    print("Initial list of players: ", players)
    capitalized = [player.capitalize() for player in players]
    print("New list with all names capitalized: ", capitalized)
    before_capitalize = [
        player for player in players if player == player.capitalize()
    ]
    print("New list of capitalized names only: ", before_capitalize)
    score: dict[str, int] = {
        player: random.randint(0, 100)
        for player in capitalized
    }
    print("Score dict: ", score)
    average = sum(score.values()) / len(score)
    average_score = {
        player: score[player] for player in score if score[player] > average
    }
    print("Score average is ", round(average, 2))
    print("High scores: ", average_score)


if __name__ == "__main__":
    main()
