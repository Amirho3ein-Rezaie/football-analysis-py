from data.data import data
from tools.func import display_result


def total_matches_played(league: str, show: bool = True) -> int:
    "Gets one league and returns the number of matches played."

    dataframe = data.get_data()

    result = dataframe[dataframe["League"] == league]["League"].count()

    if show:  # show the result if it's needed
        print()
        display_result(
            field=league, stats="Total Number of Matches", rst=result, frt_number=1
        )

    return result


def total_goals(league: str, season: int, show: bool = True) -> dict:
    "Gets the all goals in the all matches in every league."

    dataframe = data.get_data()

    # calculate the stats
    mask = (dataframe["League"] == league) & (dataframe["Season"] == season)
    list_goals = dataframe.loc[mask, "Total-Goals"].tolist()

    total_goal = sum(list_goals)
    matches = len(list_goals)

    # show result if it's needed
    if show == True:
        display_result(
            field="Total-Goals",
            stats=f"All matches : {matches:,.0f}",
            rst=total_goal,
        )

    return {"number_matches": matches, "sum_goals": total_goal}


def avrg_total_per_league(league: str, season: int, show: bool = True) -> float:
    "Calculate the average goals per leagues."

    # get datas
    data = total_goals(league, season, False)

    avrg = data["sum_goals"] / data["number_matches"]

    if show:
        print()
        display_result(  # make correc the display result
            f"Total Goals: {data["sum_goals"]}",
            f"Total goals in {data["number_matches"]} matches",
            avrg,
            f"Average goals per matches in ({league},{season})",
        )

    return avrg
