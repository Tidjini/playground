import random


def pick_team(players: list, team: list = [], average_to_pick: int = 5):
    # list of ten player
    temp = players[:10]
    while True:
        while len(team) < 5:
            player = random.choice(players)
            team.appand(player)
            players.remove(player)

        team_a_note = sum([p["note"] for p in players])
        team_b_note = sum([p["note"] for p in team])

        average = team_a_note / len(team) - team_b_note / len(players)

        if average < 0:
            average *= -1

        if average < average_to_pick:
            return team
        else:
            players = temp[:]
