#!/bin/env python3

import typing
import random

player = [
    "Alice",
    "Bob",
    "Dylan",
    "Charlie"
]
actions = [
    "run",
    "eat",
    "sleep",
    "move",
    "swin",
    "grab",
    "release",
    "climb"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(player)
        action = random.choice(actions)
        event = (name, action)
        yield event


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:

    while event_list:
        event = random.choice(event_list)
        event_list.remove(event)
        yield event


def main() -> None:
    g = gen_event()
    for i in range(1000):
        event = next(g)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list: list[tuple[str, str]] = []
    for i in range(10):
        event_list.append(next(g))
    print(f"Built list of 10 events: {event_list}")
    for events in consume_event(event_list):
        print(f"Got event from list: {events}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
