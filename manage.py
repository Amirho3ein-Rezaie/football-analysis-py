from main.func import select_analysis, select_sub_analysis, perform
from main.variables import GO_BACK_OPTION, FUNC_LIST, ANALYSIS, SUB_ANALYSIS
from tools.func import splitter, run_command, press_enter_to_continue


def main() -> None:

    while True:

        # clear the terminal
        run_command(r"cls")

        # main
        analysis_number = select_analysis(ANALYSIS)
        splitter()

        sub_analysis_number = select_sub_analysis(analysis_number, SUB_ANALYSIS)

        if sub_analysis_number == GO_BACK_OPTION:
            continue

        # run the function for the analysis
        splitter()
        perform(analysis_number, sub_analysis_number, FUNC_LIST)
        splitter()

        press_enter_to_continue()


if __name__ == "__main__":
    main()
