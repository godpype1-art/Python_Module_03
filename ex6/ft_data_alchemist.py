import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    l_names: list[str] = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Inicial list of players: {l_names}")
    l_all_capitalized: list[str] = [name.capitalize() for name in l_names]
    print(f"New list with all names capitalized: {l_all_capitalized}")
    l_only_capitalized: list[str] = [
        name for name in l_names if name[0].isupper()
        ]
    print(f"New list of capitalized names only: {l_only_capitalized}")
    print()
    d_scores: dict[str, int] = {
        name: random.randint(1, 999) for name in l_all_capitalized
        }
    print(f"Score dict: {d_scores}")
    average: float = sum(d_scores.values()) / len(d_scores)
    print(f"Score average is {round(average, 2)}")
    d_high_scores: dict[str, int] = {
        name: value for name, value in d_scores.items() if value > average
        }
    print(f"High cores: {d_high_scores}")


if __name__ == "__main__":
    main()
