import sys


class Invalid(Exception):
    ...


class Duplicate(Exception):
    ...


class NoQuantity(Exception):
    ...


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        try:
            l_arg: list[str] = arg.split(":")
            if len(l_arg) != 2:
                raise Invalid(f"Invalid parameter: '{l_arg[0]}'")
            if l_arg[1] == "0":
                raise NoQuantity(f"Invalid quantity: '{l_arg[1]}'")
            item: str = l_arg[0]
            quantity: int = int(l_arg[1])
            if item in inventory:
                raise Duplicate(f"Redundant item '{item}' - discarding")
        except Invalid as error:
            print(f"{error}")
        except Duplicate as error:
            print(f"{error}")
        except NoQuantity as error:
            print(f"{error}")
        except ValueError as error:
            print(f"Quantity error for {item}: {error}")
        else:
            inventory[item] = quantity
    print(f"Got inventory: {inventory}")
    all_items: list[str] = list(inventory.keys())
    item_count: int = len(all_items)
    total_items: int = sum(inventory.values())
    print(f"Item list: {all_items}")
    print(f"Total quantity of the {item_count} item: {total_items}")
    max_item: str = ""
    max_qty: int | None = None
    min_item: str = ""
    min_qty: int | None = None
    for item in inventory:
        quantity = inventory[item]
        percent: float = round((quantity / total_items) * 100, 1)
        print(f"Item {item} represents {percent}%")
        if max_qty is None or quantity > max_qty:
            max_qty = quantity
            max_item = item
        if min_qty is None or quantity < min_qty:
            min_qty = quantity
            min_item = item
    print(f"Item most abundant: {max_item} with quantity {max_qty}")
    print(f"Item least abundant: {min_item} with quantity {min_qty}")
    inventory.update({"magic item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
