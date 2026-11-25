from data.data import data
from .tools import team_info, select_team, select_league, select_teams
from tools.func import dataframe_as_table, ask_yes_no, display_result
from pandas import DataFrame
from .standings import team_ranking


def team_win_draw_lose_compare(season: int) -> DataFrame:
    "Get name teams, season year for comparing the number of wins, draws and loses."

    # select teams that we want to compare them
    teams = select_teams()

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


def average_points(league: str, season: int, show: bool = True) -> float:
    "Get the points and number of matches that played by the team and cal the average of points."

    # datas
    team = select_team(league=league)
    league_data = team_ranking(league=league, season=season, show=False)

    # calculating the result
    matches = league_data.loc[league_data["Team"] == team, "Matches"].iloc[0]
    points = league_data.loc[league_data["Team"] == team, "Points"].iloc[0]

    average = points / matches

    # show the result in position that needs
    if show:
        print()
        display_result("points / matches", "average points", average)

    return average
