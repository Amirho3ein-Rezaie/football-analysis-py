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


def average_stats(season: int, show: bool = True) -> DataFrame:
    "Calculate the average stats of many teams (average points, goals scored, goals conceded)"

    # datas
    teams = select_teams()
    dataframe = data.get_data()

    # calculate
    result_dict = {
        "Team(s)": [],
        "League(s)": [],
        "Season(s)": [],
        "Average_Points": [],
        "Average_Goals_Scored": [],
        "Average_Goals_Conceded": [],
    }
    for team in teams:
        # get the team's data
        league = dataframe.loc[dataframe["Home-Team"] == team, "League"].iloc[0]

        league_data = team_ranking(league=league, season=season, show=False)
        team_data = (league_data.loc[league_data["Team"] == team]).reset_index().iloc[0]

        # calculate the stats
        goals_s = int(team_data["+/-"].split("-")[0])
        goals_c = int(team_data["+/-"].split("-")[1])

        result_dict["Team(s)"].append(team)
        result_dict["League(s)"].append(league)
        result_dict["Season(s)"].append(season)

        result_dict["Average_Points"].append(team_data["Points"] / team_data["Matches"])
        result_dict["Average_Goals_Scored"].append(goals_s / team_data["Matches"])
        result_dict["Average_Goals_Conceded"].append(goals_c / team_data["Matches"])

    result = DataFrame(result_dict)

    # show the table result if it is needed
    if show:
        dataframe_as_table(result)

    return result
