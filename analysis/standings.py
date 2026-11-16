from data.data import data
from pandas import DataFrame


def team_ranking(league: str, season: int, show: bool = True) -> DataFrame:
    "Calculating the points of each team and show the table of the league in the season"

    dataframe = data.get_data()

    condition = (dataframe["League"] == league) & (dataframe["Season"] == season)

    dataframe.loc[condition].groupby("Home-Team")
