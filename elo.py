import sys
import math

from basketball_reference_web_scraper import client


def expect(elo1, elo2):
    return 1 / (1 + math.pow(10, (elo2 - elo1) / 400))


def adjust(expected, actual, team1, team2):
    elochange = (800 / 41) * (actual - expected)
    team1["elo"], team2["elo"] = team1["elo"] + elochange, team2["elo"] - elochange


def play():
    for game in games:
        team1, team2, actual = {}, {}, 0.5
        for team in teams:
            if ("Team." + team["name"].upper()).replace(" ", "_") == str(
                game["home_team"]
            ):
                team1 = team
            elif ("Team." + team["name"].upper()).replace(" ", "_") == str(
                game["away_team"]
            ):
                team2 = team
        if (game["home_team_score"] - game["away_team_score"]) > 0:
            actual = 1
        elif (game["home_team_score"] - game["away_team_score"]) < 0:
            actual = 0
        elif (game["home_team_score"] - game["away_team_score"]) == 0:
            actual = 0.5
        adjust(expect(team1["elo"], team2["elo"]), actual, team1, team2)


def rank():
    for x in range(15):
        east.append(teams[x])
    for x in range(15, 30):
        west.append(teams[x])
    ladder, eastladder, westladder = (
        sorted(teams, key=lambda k: k["elo"], reverse=True),
        sorted(east, key=lambda k: k["elo"], reverse=True),
        sorted(west, key=lambda k: k["elo"], reverse=True),
    )
    print()
    for x in range(15):
        print(
            str(x + 1)
            + ". "
            + westladder[x]["name"]
            + " ("
            + str(int(westladder[x]["elo"]))
            + ")"
            + (
                " "
                * (
                    36
                    - len(
                        str(x + 1)
                        + ". "
                        + westladder[x]["name"]
                        + " ("
                        + str(int(westladder[x]["elo"]))
                        + ")"
                    )
                )
            )
            + str(x + 1)
            + ". "
            + eastladder[x]["name"]
            + " ("
            + str(int(eastladder[x]["elo"]))
            + ")"
        )
    print()


games, teams, east, west = (
    client.season_schedule(season_end_year=sys.argv[1])[:1230],
    [],
    [],
    [],
)
for name in [
    "Boston Celtics",
    "Brooklyn Nets",
    "New York Knicks",
    "Philadelphia 76ers",
    "Toronto Raptors",
    "Chicago Bulls",
    "Cleveland Cavaliers",
    "Detroit Pistons",
    "Indiana Pacers",
    "Milwaukee Bucks",
    "Atlanta Hawks",
    "Charlotte Hornets",
    "Miami Heat",
    "Orlando Magic",
    "Washington Wizards",
    "Dallas Mavericks",
    "Houston Rockets",
    "Memphis Grizzlies",
    "New Orleans Pelicans",
    "San Antonio Spurs",
    "Denver Nuggets",
    "Minnesota Timberwolves",
    "Oklahoma City Thunder",
    "Portland Trail Blazers",
    "Utah Jazz",
    "Golden State Warriors",
    "Los Angeles Clippers",
    "Los Angeles Lakers",
    "Phoenix Suns",
    "Sacramento Kings",
]:
    teams.append(dict(name=name, elo=1200, diff=0))
play()
rank()
