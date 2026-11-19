from data.data import data
from pandas import DataFrame
from tools.func import dataframe_as_table
from .tools import team_info


def team_ranking(league: str, season: int, show: bool = True) -> DataFrame:
    "Calculating the points of each team and show the table of the league in the season"

    dataframe = data.get_data()

    condition = (dataframe["League"] == league) & (dataframe["Season"] == season)

    teams = dataframe.loc[condition, "Home-Team"].unique()

    temp_table = {
        "Team": [],
        "Matches": [],
        "Wins": [],
        "Draws": [],
        "Loses": [],
        "+/-": [],
        "GD": [],
        "Points": [],
    }

    for team in teams:

        # gets the stats of the table
        # # get the wins data
        wins = team_info(team, league=league, season=season)["wins"]

        # # get the positive goals
        positive_goal = team_info(team, league=league, season=season)["s-goals"]
        negative_goal = team_info(team, league, season)["c-goals"]

        # # get the draws and loses data
        draws = team_info(team, league=league, season=season)["draws"]

        matches = team_info(team, league=league, season=season)["matches"]
        loses = team_info(team, league=league, season=season)["loses"]

        point = wins * 3 + draws

        # add stats to the dictionary
        temp_table["Team"].append(team)
        temp_table["Matches"].append(matches)
        temp_table["Wins"].append(wins)
        temp_table["Draws"].append(draws)
        temp_table["Loses"].append(loses)
        temp_table["+/-"].append(f"{positive_goal}-{negative_goal}")
        temp_table["GD"].append(positive_goal - negative_goal)
        temp_table["Points"].append(point)

    dataframe = DataFrame(temp_table)

    if show:
        dataframe_as_table(dataframe.sort_values("Points", ascending=False))

    return dataframe
