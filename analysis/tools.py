from data.data import data
from tools.func import select_type_option, SelectionType


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
