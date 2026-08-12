import random


ALL_ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer"
    ]


def gen_player_achievements() -> set[str]:
    achievements: list[str] = random.sample(
        ALL_ACHIEVEMENTS, random.randint(3, 8)
        )
    return set(achievements)


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice: set[str] = gen_player_achievements()
    bob: set[str] = gen_player_achievements()
    charlie: set[str] = gen_player_achievements()
    dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distint achievements: {(alice | bob | charlie | dylan)}")
    print()
    print(f"Common achievements: {alice & bob & charlie & dylan}")
    print()
    print(f"Only alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - alice - bob - dylan}")
    print(f"Only Dylan has: {dylan - alice - bob - charlie}")
    print()
    print(f"Alice is missing {set(ALL_ACHIEVEMENTS) - alice}")
    print(f"Bob is missing {set(ALL_ACHIEVEMENTS) - bob}")
    print(f"Charlie is missing {set(ALL_ACHIEVEMENTS) - charlie}")
    print(f"Dylan is missing {set(ALL_ACHIEVEMENTS) - dylan}")


if __name__ == "__main__":
    main()
