# CRUD (Create Read Update Delete) operations


# Database representation
team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 31, "number": 12},
]


list_numb = []
for i in team:
    list_numb.append(i["number"])


# Application source code
def repr_players(players: list[dict]):
    for player in players:
        print(f"\t[Player: {player['number']}]: {player['name']}, {player['age']}")


def player_add(name: str, age: int, number: int) -> dict:
    player: dict = {"name": name, "age": age, "number": number}

    if player["number"] not in list_numb:
        team.append(player)
        return player
    else:
        print("We already have a player with this number, choose another one")


def player_update(name: str, age: int, number: int) -> dict:
    new_data: dict = {"name": name, "age": age, "number": number}

    x = new_data["number"]

    if x in list_numb:
        team[list_numb.index(x)] = new_data
        return new_data
    else:
        print("There is no player with that number")


def player_delete():
    pass


def main():
    operations = ("add", "update", "del", "repr", "exit")

    while True:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print(f"Operation: '{operation}' is not available\n")
            continue

        if operation == "exit":
            print("Bye")
            break

        elif operation == "repr":
            repr_players(team)

        elif operation == "update":
            user_data = input("Enter the player information[name, age, number]: ")
            user_items: list[str] = user_data.split(",")
            name, age, number = user_items
            try:
                player_update(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number of the player must be integers\n\n")
                continue

        elif operation == "del":
            player_delete()

        elif operation == "add":
            user_data = input("Enter new player information[name, age, number]: ")
            user_items: list[str] = user_data.split(",")
            name, age, number = user_items
            try:
                player_add(name=name, age=int(age), number=int(number))
            except ValueError:
                print("Age and number of the player must be integers\n\n")
                continue
        else:
            raise NotImplementedError


if __name__ == "__main__":
    main()
