from tools.func import select_item
from .variables import GO_BACK_OPTION
from data.load import PREPARED_DATA_DIR
from os.path import exists


def select_analysis(items: list) -> int:
    "select analysis and returns the number of option"

    return select_item(items, 1, "Analysis ... ")


def select_sub_analysis(analysis: int, items: list) -> int:
    "select one sub analysis and return the number of it"

    return select_item(items[analysis - 1], GO_BACK_OPTION, "Sub Analysis ... ")


def perform(analysis: int, sub_analysis: int, func_list: list) -> None:
    "get analysis and sub analysis and the function list and run the function"

    try:
        func_list[analysis - 1][sub_analysis - 1]()

    except (TypeError, IndexError) as e:
        print(f"Error in running the option's function -> {type(e).__name__}: {e}")


def get_filename() -> str:
    "get the dataset filename and returns it."

    return input("Enter the file name : ")


def prepared_dataset(filename: str) -> bool:
    "gets the dataset filename and define it's prepared or not and returns the it's address."

    return exists(PREPARED_DATA_DIR + filename)
