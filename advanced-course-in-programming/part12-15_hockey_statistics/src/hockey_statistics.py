import json


class HockeyPlayer:
    def __init__(self, name: str, nationality: str, assists: int, goals: int,
                 penalties: int, team: str, games: int):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
        self.points = self.assists + self.goals

    def __str__(self):
        return (f"{self.name:<21}{self.team:<4}{self.goals:>3} + "
                f"{self.assists:>2} = {self.points:>3}")


def read_file(file_name: str):
    with open(file_name) as my_file:
        stats = json.load(my_file)

    players = []
    for element in stats:
        players.append(HockeyPlayer(
            element["name"],
            element["nationality"],
            element["assists"],
            element["goals"],
            element["penalties"],
            element["team"],
            element["games"]
        ))
    return players


def interactive_application():
    file_name = input("file name: ")
    hockey_stats = read_file(file_name)
    print(f"read the data of {len(hockey_stats)} players")

    # menu is printed once, not on every loop iteration
    print("\ncommands:\n0 quit\n1 search for player\n2 teams\n3 countries\n"
          "4 players in team\n5 players from country\n6 most points\n7 most goals\n")

    while True:
        command = int(input("command: "))

        if command == 0:
            break

        elif command == 1:
            name = input("name: ")
            print()
            for player in hockey_stats:
                if player.name == name:
                    print(player)

        elif command == 2:
            teams = sorted(set(player.team for player in hockey_stats))
            for team in teams:
                print(team)

        elif command == 3:
            countries = sorted(set(player.nationality for player in hockey_stats))
            for country in countries:
                print(country)

        elif command == 4:
            team = input("team: ")
            print()
            players = sorted(
                filter(lambda p: p.team == team, hockey_stats),
                key=lambda p: p.points,
                reverse=True
            )
            for player in players:
                print(player)

        elif command == 5:
            country = input("country: ")
            print()
            players = sorted(
                filter(lambda p: p.nationality == country, hockey_stats),
                key=lambda p: p.points,
                reverse=True
            )
            for player in players:
                print(player)

        elif command == 6:
            n = int(input("how many: "))
            print()
            players = sorted(
                hockey_stats,
                key=lambda p: (p.points, p.goals),
                reverse=True
            )
            for player in players[:n]:
                print(player)

        elif command == 7:
            n = int(input("how many: "))
            print()
            players = sorted(
                hockey_stats,
                key=lambda p: (-p.goals, p.games)
            )
            for player in players[:n]:
                print(player)


interactive_application()