from data.data import data
from .tools import team_info, select_team, select_league
from tools.func import dataframe_as_table, ask_yes_no
from pandas import DataFrame


def team_win_draw_lose_compare(season: int) -> DataFrame:
    "Get name teams, season year for comparing the number of wins, draws and loses."

    # variables
    teams = []

    # select the teams that we want to compare them with each other
    while True:

        print(f"Selecting the team ({teams.__len__() + 1})")

        teams.append(select_team(select_league()))

        print()
        if not ask_yes_no("Wants to enter team's name ? "):
            break
        print()

    # data the data of teams
    result = {"Team": [], "Wins": [], "Draws": [], "Loses": []}
    for team in teams:
        result["Wins"].append(team_info(team, season)["wins"])
        result["Draws"].append(team_info(team, season)["draws"])
        result["Loses"].append(team_info(team, season)["loses"])
        result["Team"].append(team)
    dataframe_result = DataFrame(result)

    # show table result
    dataframe_as_table(dataframe_result)

    return dataframe_result
