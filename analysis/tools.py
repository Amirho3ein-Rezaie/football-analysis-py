from data.data import data
from tools.func import select_str_option


def select_league() -> str:
    "gets leagues from the dataset and user can select one."

    dataframe = data.get_data()

    leagues = dataframe["League"].unique()

    return select_str_option(leagues)
