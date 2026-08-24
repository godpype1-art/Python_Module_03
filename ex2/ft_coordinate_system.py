import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw: str = input(
            "Enter new coordinates as float in format 'x, y, z': "
            )
        parts: list[str] = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            x: float = float(parts[0].strip())
            y: float = float(parts[1].strip())
            z: float = float(parts[2].strip())
            return (x, y, z)
        except ValueError as error:
            for part in parts:
                try:
                    float(part.strip())
                except ValueError:
                    bad: str = part.strip()
                    print(f"Error on parameter '{bad}': {error}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos_1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos_1}")
    print(f"it includes: X={pos_1[0]}, Y={pos_1[1]}, Z={pos_1[2]}")
    distance: float = round(math.sqrt(
        (pos_1[0]-0)**2 +
        (pos_1[1]-0)**2 +
        (pos_1[2]-0)**2), 4)
    print(f"Distance to center: {distance}")
    print()
    print("Get a second set of coordinates")
    pos_2: tuple[float, float, float] = get_player_pos()
    distance = round(math.sqrt(
        (pos_2[0] - pos_1[0])**2 +
        (pos_2[1] - pos_1[1])**2 +
        (pos_2[2] - pos_1[2])**2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    main()
