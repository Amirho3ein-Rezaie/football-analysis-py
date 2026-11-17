from data.data import data
from pandas import DataFrame
from tools.func import dataframe_as_table


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

        # condirions
        team_con = (dataframe["Home-Team"] == team) | (dataframe["Away-Team"] == team)

        # gets the stats of the table
        # # get the wins data
        home_wins = dataframe.loc[
            condition & (dataframe["Home-Team"] == team) & (dataframe["Winner"] == "H")
        ].__len__()
        away_wins = dataframe.loc[
            condition & (dataframe["Away-Team"] == team) & (dataframe["Winner"] == "A")
        ].__len__()
        wins = home_wins + away_wins

        # # get the positive goals
        positive_goal = sum(
            dataframe.loc[condition & (dataframe["Home-Team"] == team), "Home-Goals"]
        ) + sum(
            dataframe.loc[condition & (dataframe["Away-Team"] == team), "Away-Goals"]
        )
        # # get the negative goals
        negative_goal = sum(
            dataframe.loc[condition & (dataframe["Home-Team"] == team), "Away-Goals"]
        ) + sum(
            dataframe.loc[condition & (dataframe["Away-Team"] == team), "Home-Goals"]
        )

        # # get the draws and loses data
        draws = dataframe.loc[
            condition & team_con & (dataframe["Winner"] == "D")
        ].__len__()

        matches = dataframe.loc[condition & team_con].__len__()
        loses = matches - (wins + draws)
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
