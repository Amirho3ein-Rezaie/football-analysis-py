from main.func import (
    select_analysis,
    select_sub_analysis,
    perform,
    get_filename,
    is_prepared_dataset,
)
from main.variables import GO_BACK_OPTION, FUNC_LIST, ANALYSIS, SUB_ANALYSIS
from tools.func import splitter, run_command, press_enter_to_continue
from data.load import read_data_file
from data.prepare import prepare_dataset


def main() -> None:

    loaded_data_flag = False

    while True:

        # clear the terminal and start
        run_command(r"cls")
        print("=== Welcome to analysis football league data ===")
        splitter()

        # load the data
        if not loaded_data_flag:
            dataset_file = get_filename()  # get dataset filename
            prepared_dataset_flag = is_prepared_dataset(dataset_file)  # is it prepared

            # load data
            rload = read_data_file(dataset_file, prepared_dataset_flag)  # load data

            if rload == 0:
                loaded_data_flag = True
                print("Data successfully Loaded ... !!!")

            # if it is prepared, not will prepare it
            if not prepared_dataset_flag and rload == 0:

                if prepare_dataset():
                    print("Dataset successfully Prepared ... !!!")

            press_enter_to_continue()
            continue

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
