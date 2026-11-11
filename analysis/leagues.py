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
