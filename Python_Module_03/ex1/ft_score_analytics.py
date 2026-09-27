#!/bin/env python3
import sys


def score_analytic() -> None:
    int_scores: list[int] = []
    for score in sys.argv[1:]:
        try:
            int_scores = int_scores + [int(score)]
        except ValueError:
            print(f"Invalid parameter: {score}")

    total_players = len(int_scores)
    total_score = sum(int_scores)
    if total_players > 0:
        print(f"Scores processed: {int_scores}")
        print(f"Total players: {total_players}")
        print(f"Total score: {total_score}")
        print(f"Average score: {total_score / total_players}")
        print(f"High score: {max(int_scores)}")
        print(f"Low score: {min(int_scores)}")
        print(f"Score range: {max(int_scores) - min(int_scores)}")
    else:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )


score_analytic()
