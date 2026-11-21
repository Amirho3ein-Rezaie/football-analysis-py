from analysis import leagues
from analysis import standings
from analysis import teams
from analysis.tools import select_league, select_season, select_result_match

# varialbes
DEBUG = True
TEST_DATASET_NAME = "leagues.csv"

GO_BACK_OPTION = 0

ANALYSIS = [
    "League Overview",
    "League Standings",
    "Team Performance Analysis",
    "Home & Away Performance",
    "Goal Statistics",
    # "Team Form Analysis",
    "Season Comparison",
]
SUB_ANALYSIS = [
    # 1. League Overview
    [
        "Matches Played",  # Total number of matches played in the league.
        "Total Goals",  # Total number of goals scored in all matches.
        "Average Goals per Match",  # Average number of goals scored per match.
        "Number Result Matches (Number)",  # Number of matches won by home teams.
    ],
    # 2. League Standings
    [
        "Team Rankings",  # Ranking of teams based on their points.
    ],
    # 3. Team Performance Analysis
    [
        "Wins, Draws and Losses",  # Comparison of wins, draws and losses for each team.
        "Average Points",  # Average points earned per match by each team.
        "Average Goals Scored",  # Average goals scored per match by each team.
        "Average Goals Conceded",  # Average goals conceded per match by each team.
        "Team Performance Comparison",  # Comparison of overall performance between teams.
    ],
    # 4. Home & Away Performance
    [
        "Home vs Away Results",  # Comparison of teams' results at home and away.
        "Home Wins vs Away Wins",  # Comparison of home wins and away wins.
        "Home vs Away Goals Scored",  # Comparison of goals scored at home and away.
        "Home vs Away Goals Conceded",  # Comparison of goals conceded at home and away.
        "Home Performance Rankings",  # Ranking of teams based on their home performance.
        "Away Performance Rankings",  # Ranking of teams based on their away performance.
    ],
    # 5. Goal Statistics
    [
        "Top Scoring Teams",  # Teams with the highest number of goals scored.
        "Teams with Fewest Goals Conceded",  # Teams that conceded the fewest goals.
        "Average Goals per Team",  # Average total goals scored by each team.
        "Highest Scoring Matches",  # Matches with the highest total number of goals.
        "Goal Distribution",  # Distribution of goals scored across matches.
    ],
    # # 6. Team Form Analysis
    # [
    #     "Recent Match Results",  # Results of each team's most recent matches.
    #     "Wins, Draws and Losses Trend",  # Trend of wins, draws and losses in recent matches.
    #     "Points in Recent Matches",  # Points earned by each team in recent matches.
    #     "Recent Team Form Comparison",  # Comparison of teams based on their recent performance.
    # ],
    # 7. Season Comparison
    [
        "Team Performance Across Seasons",  # Comparison of team performance across different seasons.
        "League Average Goals Comparison",  # Comparison of average goals per match across seasons.
        "Team Points Comparison Across Seasons",  # Comparison of team points across different seasons.
        "Team Ranking Changes Across Seasons",  # Changes in team rankings across different seasons.
    ],
]
FUNC_LIST = [  # test list in dev will be full of functions
    # 1. League Overview
    [
        lambda: leagues.total_matches_played(select_league()),
        lambda: leagues.total_goals(select_league(), select_season()),
        lambda: leagues.avrg_total_per_league(select_league(), select_season()),
        lambda: leagues.match_result_number(
            select_league(), select_season(), select_result_match()
        ),
    ],
    # 2. League Standings
    [
        lambda: standings.team_ranking(select_league(), select_season()),
    ],
    # 3. Team Performance Analysis
    [
        lambda: teams.team_win_draw_lose_compare(select_season()),
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
    # # 6. Team Form Analysis
    # [
    #     "Recent Match Results",
    #     "Wins, Draws and Losses Trend",
    #     "Points in Recent Matches",
    #     "Recent Team Form Comparison",
    # ],
    # 7. Season Comparison
    [
        "Team Performance Across Seasons",
        "League Average Goals Comparison",
        "Team Points Comparison Across Seasons",
        "Team Ranking Changes Across Seasons",
    ],
]
