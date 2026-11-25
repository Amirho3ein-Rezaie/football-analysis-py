from data.data import data
from tools.func import select_type_option, SelectionType, splitter, ask_yes_no


def select_league() -> str:
    "gets leagues from the dataset and user can select one."

    dataframe = data.get_data()

    leagues = dataframe["League"].unique()

    return select_type_option(leagues, SelectionType.STR, "Enter the league : ")


def select_season() -> int:
    "gets seasons from the dataset and user can select one."

    dataframe = data.get_data()
    seasons = dataframe["Season"].unique()

    # select one item by writing
    return select_type_option(seasons, SelectionType.INT, "Enter the Season : ")


def select_result_match() -> str:
    dataframe = data.get_data()
    results = dataframe["Winner"].unique()

    # select one item by writing
    return select_type_option(results, SelectionType.STR, "Enter the Result match : ")


def team_info(team: str, season: int, league: str = "") -> dict:
    "Calculate the number of wins of one team."

    dataframe = data.get_data()

    # condirions
    team_con = (dataframe["Home-Team"] == team) | (dataframe["Away-Team"] == team)

    condition = (dataframe["League"] == league) & (dataframe["Season"] == season)
    if league == "":
        condition = dataframe["Season"] == season

    # wins
    wins = (
        dataframe.loc[
            condition & (dataframe["Home-Team"] == team) & (dataframe["Winner"] == "H")
        ].__len__()
    ) + (
        dataframe.loc[
            condition & (dataframe["Away-Team"] == team) & (dataframe["Winner"] == "A")
        ].__len__()
    )

    # draws
    draws = dataframe.loc[condition & team_con & (dataframe["Winner"] == "D")].__len__()

    # matches
    matches = dataframe.loc[condition & team_con].__len__()

    # loses
    loses = matches - (wins + draws)

    # goals
    p_goal = sum(
        dataframe.loc[condition & (dataframe["Home-Team"] == team), "Home-Goals"]
    ) + sum(dataframe.loc[condition & (dataframe["Away-Team"] == team), "Away-Goals"])
    n_goal = sum(
        dataframe.loc[condition & (dataframe["Home-Team"] == team), "Away-Goals"]
    ) + sum(dataframe.loc[condition & (dataframe["Away-Team"] == team), "Home-Goals"])

    return {
        "wins": wins,
        "draws": draws,
        "loses": loses,
        "matches": matches,
        "s-goals": p_goal,
        "c-goals": n_goal,
    }


def select_team(league: str) -> str:
    "At first select one league and select one team from that at least return team name."

    dataframe = data.get_data()

    teams = dataframe.loc[dataframe["League"] == league, "Home-Team"].unique()

    splitter(length_line=30)  # split teams name with the leagues name

    teams.sort()  # sort the teams name
    return select_type_option(teams, SelectionType.STR, "Enter the Team name : ")


def select_teams() -> list:
    """Select one or more different teams (each team from its own league)."""

    teams = []

    while True:
        print(f"Selecting the team ({len(teams) + 1})")
        team = select_team(select_league())

        if team in teams:
            print(f"{team} is already selected.")
            continue

        teams.append(team)

        print()
        if not ask_yes_no("Do you want to select another team ?"):
            break
        print()

    return teams
