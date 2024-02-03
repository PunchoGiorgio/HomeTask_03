from typing import Generator


class Player:
    def __init__(self, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


team: list[Player] = [
    Player("John", "Smith"),
    Player("Marry", "Smith"),
    Player("Jack", "Hill"),
    Player("Nick", "Doe"),
    Player("John", "Doe"),
    Player("Marry", "Doe"),
]


for player in team:
    print(player)


def dedup(collection) -> Generator[str, None, None]:
    mydict = {}
    for item in collection:
        mydict.update({item.first_name: item.last_name})

    pairs = [[k, v] for [k, v] in mydict.items()]

    for name, surname in pairs:
        yield f"{name} {surname}"


for player in dedup(team):
    print(player)
