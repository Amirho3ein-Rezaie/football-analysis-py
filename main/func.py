from tools.func import select_item

# variables
GO_BACK_OPTION = 0


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
