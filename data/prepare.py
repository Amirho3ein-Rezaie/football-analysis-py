from data.data import data
from data.load import PREPARED_DATA_DIR
from pathlib import Path


def change_columns() -> int:
    "Get cleaned dataframe and change some columns."

    dataframe = data.get_data()

    try:
        # drop extra columns
        dataframe.drop(
            columns=[
                "Over 2,5",
                "Under 2,5",
                "Code 1",
                "Code 2",
            ],
            inplace=True,
        )

        # change name of columns
        dataframe.rename(
            columns={
                "Home Team": "Home-Team",
                "Away Team": "Away-Team",
                "Home Goals": "Home-Goals",
                "Away Goals": "Away-Goals",
                "Home FH": "Home-FHG",
                "Away FH": "Away-FHG",
                "Home Win": "Home-WP",
                "Draw": "Draw-P",
                "Away Win": "Away-WP",
                "Total Goals": "Total-Goals",
                "FH Goals": "FH-Goals",
                "HT Winner": "HT-Winner",
            },
            inplace=True,
        )
    except Exception as e:
        print(e)
        return 1

    data.set_data(dataframe)
    return 0


def clean_valid_dataset() -> None:
    "Get dataset from the data instance and clean it."

    # do not need to clean data. it is cleaned


def save_prepared_data() -> int:
    "save dataframe in own datafile in prepared folder."

    dataframe = data.get_data()
    type = Path(data.filename).suffix

    save_functions = {
        ".csv": lambda path: dataframe.to_csv(path, index=False),
        ".json": lambda path: dataframe.to_json(
            path, force_ascii=False, orient="records"
        ),
        ".xlsx": lambda path: dataframe.to_excel(path, index=False),
    }

    try:
        save_functions[type](PREPARED_DATA_DIR + data.filename)
    except Exception as e:
        print(e)
        return 1

    return 0


def prepare_dataset() -> bool:
    "Prepare dataset by cleaning dataset and change the columns."

    return change_columns() == 0 and save_prepared_data() == 0
