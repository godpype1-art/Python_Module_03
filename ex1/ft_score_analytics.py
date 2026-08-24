import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    total: int = len(sys.argv)
    if total == 1:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
        return
    l_scores: list[int] = []
    i: int = 1
    while i < total:
        try:
            score: int = int(sys.argv[i])
            l_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    if len(l_scores) == 0:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
        return
    print(f"Score processed: {l_scores}")
    player_count: int = len(l_scores)
    print(f"Total players: {player_count}")
    total_score: int = sum(l_scores)
    print(f"Total score: {total_score}")
    print(f"Average score: {float(total_score) / player_count}")
    max_score: int = max(l_scores)
    min_score: int = min(l_scores)
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    main()
