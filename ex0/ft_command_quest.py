import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    total: int = len(sys.argv)
    if total == 1:
        print("No arguments provided!")
    else:
        i: int = 1
        print(f"Arguments received: {total - 1}")
        while i < total:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {total}")


if __name__ == "__main__":
    main()
