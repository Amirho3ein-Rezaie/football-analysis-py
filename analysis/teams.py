from data.data import data
from .tools import team_info
from tools.func import dataframe_as_table
from pandas import DataFrame


def team_win_draw_lose_compare() -> DataFrame:
    "Get name teams, season year for comparing the number of wins, draws and loses."

    # variables
    dataframe = data.get_data()
    dataframe = dataframe.loc[dataframe["Season"] == 20]

    print(team_info("Liverpool", 20))

    pass
