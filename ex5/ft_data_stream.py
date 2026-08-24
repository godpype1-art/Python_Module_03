from typing import Generator
import random


ALL_PLAYERS: list[str] = [
    "alice", "bob", "dylan", "charlie"
    ]


ALL_ACTIONS: list[str] = [
    "run", "eat", "sleep", "grab", "move", "climb", "swim", "release"
    ]


def consume_event(
        l_events: list[tuple[str, str]]
        ) -> Generator[tuple[str, str], None, None]:
    event: tuple[str, str] = random.choice(l_events)
    l_events.remove(event)
    print(f"Got event from list: {event}")
    print(f"Remains in list: {l_events}")
    yield event


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player: str = random.choice(ALL_PLAYERS)
        action: str = random.choice(ALL_ACTIONS)
        yield (player, action)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    for count in range(0, 1000):
        event: tuple[str, str] = next(gen_event())
        player, action = event
        print(f"Event {count}: Player {player} did action {action}")
    l_events: list[tuple[str, str]] = []
    for count in range(0, 10):
        l_events.append(next(gen_event()))
    print(f"Built list of 10 events: {l_events}")
    for count in range(0, 10):
        next(consume_event(l_events))


if __name__ == "__main__":
    main()
