from main.func import select_analysis, select_sub_analysis, GO_BACK_OPTION, perform
from tools.func import splitter, run_command, press_enter_to_continue

# varialbes
LIST_ANALYSIS = [
    "League Overview",
    "League Standings",
    "Team Performance Analysis",
    "Home & Away Performance",
    "Goal Statistics",
    "Team Form Analysis",
    "Season Comparison",
]
SUB_ANALYSIS = [
    # 1. League Overview
    [
        "Matches Played",
        "Total Goals",
        "Average Goals per Match",
        "Home Wins",
        "Away Wins",
        "Draws",
    ],
    # 2. League Standings
    [
        "Team Rankings",
        "Points",
        "Wins",
        "Draws",
        "Losses",
        "Goals Scored",
        "Goals Conceded",
        "Goal Difference",
    ],
    # 3. Team Performance Analysis
    [
        "Wins, Draws and Losses",
        "Average Points",
        "Average Goals Scored",
        "Average Goals Conceded",
        "Team Performance Comparison",
    ],
    # 4. Home & Away Performance
    [
        "Home vs Away Results",
        "Home Wins vs Away Wins",
        "Home vs Away Goals Scored",
        "Home vs Away Goals Conceded",
        "Home Performance Rankings",
        "Away Performance Rankings",
    ],
    # 5. Goal Statistics
    [
        "Top Scoring Teams",
        "Teams with Fewest Goals Conceded",
        "Average Goals per Team",
        "Highest Scoring Matches",
        "Goal Distribution",
    ],
    # 6. Team Form Analysis
    [
        "Recent Match Results",
        "Wins, Draws and Losses Trend",
        "Points in Recent Matches",
        "Recent Team Form Comparison",
    ],
    # 7. Season Comparison
    [
        "Team Performance Across Seasons",
        "League Average Goals Comparison",
        "Team Points Comparison Across Seasons",
        "Team Ranking Changes Across Seasons",
    ],
]
FUNC_LIST = [  # test list in dev will be full of functions
    # 1. League Overview
    [
        "Matches Played",
        "Total Goals",
        "Average Goals per Match",
        "Home Wins",
        "Away Wins",
        "Draws",
    ],
    # 2. League Standings
    [
        "Team Rankings",
        "Points",
        "Wins",
        "Draws",
        "Losses",
        "Goals Scored",
        "Goals Conceded",
        "Goal Difference",
    ],
    # 3. Team Performance Analysis
    [
        "Wins, Draws and Losses",
        "Average Points",
        "Average Goals Scored",
        "Average Goals Conceded",
        "Team Performance Comparison",
    ],
    # 4. Home & Away Performance
    [
        "Home vs Away Results",
        "Home Wins vs Away Wins",
        "Home vs Away Goals Scored",
        "Home vs Away Goals Conceded",
        "Home Performance Rankings",
        "Away Performance Rankings",
    ],
    # 5. Goal Statistics
    [
        "Top Scoring Teams",
        "Teams with Fewest Goals Conceded",
        "Average Goals per Team",
        "Highest Scoring Matches",
        "Goal Distribution",
    ],
    # 6. Team Form Analysis
    [
        "Recent Match Results",
        "Wins, Draws and Losses Trend",
        "Points in Recent Matches",
        "Recent Team Form Comparison",
    ],
    # 7. Season Comparison
    [
        "Team Performance Across Seasons",
        "League Average Goals Comparison",
        "Team Points Comparison Across Seasons",
        "Team Ranking Changes Across Seasons",
    ],
]


def main() -> None:

    while True:

        # clear the terminal
        run_command(r"cls")

        # main
        analysis_number = select_analysis(LIST_ANALYSIS)
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
