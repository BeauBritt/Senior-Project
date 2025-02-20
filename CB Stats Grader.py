import pandas as pd

def grade_stat(value, thresholds):
    """
    Assigns a grade between 60-99 based on defined thresholds.
    :param value: The statistical value to be graded.
    :param thresholds: A list of (stat_value, grade) pairs, ordered from highest to lowest.
    :return: The corresponding grade.
    """
    for threshold, grade in thresholds:
        if value >= threshold:
            return grade
    return 60  # Minimum grade

def grade_ncaa_stats():
    csv_filename = "ncaa_player_stats.csv"  # Ensure correct file name
    
    # Load data
    df = pd.read_csv(csv_filename)
    
    # Define grading thresholds for different stats (to be manually inputted)
    ppg_thresholds = [
        (20, 99),
        (19.5, 98),
        (19, 97),
        (18.5, 96),
        (18, 95),
        (17.5, 90),
        (17, 89),
        (16.5, 88),
        (16, 87),
        (15.5, 86),
        (15, 85),
        (14.5, 84),
        (14, 83),
        (13.5, 82),
        (13, 81),
        (12.5, 80),
        (12, 79),
        (11.5, 78),
        (11, 77),
        (10.5, 76),
        (10, 75),
        (9.5, 74),
        (9, 73),
        (8.5, 72),
        (8, 71),
        (7.5, 70),
        (7, 69),
        (6.5, 68),
        (6, 67),
        (5.5, 66),
        (5, 65),
        (4.5, 64),
        (4, 63),
        (3.5, 62),
        (3, 61),
        (2.5, 60)
    ]

    fg_thresholds = [  # Example thresholds for field goal percentage
        (0.60, 99),  # 60%+ FG = 99
        (0.58, 98),
        (0.55, 97),
        (0.52, 96),
        (0.50, 95),
        (0.48, 94),
        (0.47, 93),
        (0.46, 92),
        (0.45, 91),
        (0.44, 90),
        (0.42, 89),
        (0.40, 88),
        (0.39, 87),
        (0.38, 86),
        (0.37, 85),
        (0.36, 84),
        (0.35, 83),
        (0.34, 82),
        (0.33, 81),
        (0.32, 80),
        (0.31, 79),
        (0.30, 78),
        (0.29, 77),
        (0.28, 76),
        (0.27, 75),
        (0.26, 74),
        (0.25, 73),
        (0.24, 72),
        (0.22, 71),
        (0.21, 60),
    ]   

    ftpg_thresholds = [
        (1, 99),  # 100%+ FTA/FGA
        (0.99, 98),
        (0.98, 97),
        (0.97, 96),
        (0.96, 95),
        (0.95, 94),
        (0.94, 93),
        (0.93, 92),
        (0.92, 91),
        (0.91, 90),
        (0.90, 89),
        (0.89, 88),
        (0.88, 87),
        (0.87, 86),
        (0.86, 85),
        (0.85, 84),
        (0.84, 83),
        (0.83, 82),
        (0.82, 81),
        (0.81, 80),
        (0.80, 79),
        (0.79, 78),
        (0.78, 77),
        (0.77, 76),
        (0.76, 75),
        (0.75, 74),
        (0.74, 73),
        (0.73, 72),
        (0.72, 71),
        (0.71, 70),
        (0.70, 69),
        (0.69, 68),
        (0.68, 67),
        (0.67, 66),
        (0.66, 65),
        (0.65, 64),
        (0.64, 63),
        (0.63, 62),
        (0.62, 61),
        (0.61, 60),
    ]

    threepg_thresholds = [
        (0.5, 99),
        (0.49, 98),
        (0.48, 97),
        (0.47, 96),
        (0.46, 95),
        (0.45, 94),
        (0.44, 93),
        (0.43, 92),
        (0.42, 91),
        (0.41, 90),
        (0.40, 89),
        (0.39, 88),
        (0.38, 87),
        (0.37, 86),
        (0.36, 85),
        (0.35, 84),
        (0.34, 83),
        (0.33, 82),
        (0.32, 81),
        (0.31, 80),
        (0.30, 79),
        (0.29, 78),
        (0.28, 77),
        (0.27, 76),
        (0.26, 75),
        (0.25, 74),
        (0.24, 73),
        (0.23, 72),
        (0.22, 71),
        (0.21, 70),
        (0.20, 69),
        (0.19, 68),
        (0.18, 67),
        (0.17, 66),
        (0.16, 65),
        (0.15, 64),
        (0.14, 63),
        (0.13, 62),
        (0.12, 61),
        (0.11, 60),
    ]
    rpg_thresholds = [  # Example thresholds for rebounds per game
        (10, 99),
        (9.8, 98),
        (9.7, 97),
        (9.6, 96),
        (9.5, 95),
        (9.4, 94),
        (9.3, 93),
        (9.2, 92),
        (9.1, 91),
        (9.0, 90),
        (8.9, 89),
        (8.8, 88),
        (8.7, 87),
        (8.6, 86),
        (8.5, 85),
        (8.4, 84),
        (8.3, 83),
        (8.2, 82),
        (8.1, 81),
        (8.0, 80),
        (7.5, 79),
        (7.3, 78),
        (7.1, 77),
        (6.8, 76),
        (6.4, 75),
        (6.0, 74),
        (5.6, 73),
        (5.2, 72),
        (4.8, 71),
        (4.4, 70),
        (4.0, 69),
        (3.6, 68),
        (3.2, 67),
        (2.8, 66),
        (2.4, 65),
        (2.0, 64),
        (1.6, 63),
        (1.2, 62),
        (0.8, 61),
        (0.4, 60),
    ]
    
    apg_thresholds = [  # Example thresholds for assists per game
        (7, 99),
        (6.8, 98),
        (6.7, 97),
        (6.6, 96),
        (6.5, 95),
        (6.4, 94),
        (6.3, 93),
        (6.2, 92),
        (6.1, 91),
        (6.0, 90),
        (5.9, 89),
        (5.8, 88),
        (5.7, 87),
        (5.6, 86),
        (5.5, 85),
        (5.4, 84),
        (5.3, 83),
        (5.2, 82),
        (5.1, 81),
        (5.0, 80),
        (4.9, 79),
        (4.8, 78),
        (4.7, 77),
        (4.6, 76),
        (4.5, 75),
        (4.3, 74),
        (4.1, 73),
        (3.9, 72),
        (3.7, 71),
        (3.5, 70),
        (2.0, 69),
        (1.9, 68),
        (1.8, 67),
        (1.7, 66),
        (1.6, 65),
        (1.5, 64),
        (1.3, 63),
        (1.0, 62),
        (0.5, 61),
        (0.0, 60),
    ]
    spg_thresholds = [
        (3.0, 99),
        (2.9, 98),
        (2.8, 97),
        (2.7, 96),
        (2.6, 95),
        (2.5, 94),
        (2.4, 93),
        (2.3, 92),
        (2.2, 91),
        (2.0, 90),
        (1.9, 89),
        (1.8, 88),
        (1.7, 87),
        (1.6, 86),
        (1.5, 85),
        (1.3, 84),
        (1.2, 83),
        (1.1, 82),
        (1.0, 80),
        (0.9, 78),
        (0.8, 76),
        (0.7, 74),
        (0.6, 72),
        (0.5, 70),
        (0.4, 69),
        (0.3, 66),
        (0.2, 64),
        (0.1, 62),
        (0.0, 60),
    ]

    bpg_thresholds = [
        (3.0, 99),
        (2.8, 98),
        (2.7, 97),
        (2.5, 94),
        (2.1, 91),
        (2.0, 90),
        (1.8, 88),
        (1.6, 85),
        (1.3, 82),
        (1.0, 80),
        (0.9, 79),
        (0.8, 78),
        (0.7, 76),
        (0.6, 74),
        (0.5, 70),
        (0.4, 67),
        (0.3, 65),
        (0.2, 63),
        (0.1, 62),
        (0.0, 60),
    ]
    
    # Apply grading and insert grades next to respective stats
    df.insert(df.columns.get_loc('PPG') + 1, 'PPG_Grade', df['PPG'].apply(lambda x: grade_stat(x, ppg_thresholds)))
    df.insert(df.columns.get_loc('FG%') + 1, 'FG%_Grade', df['FG%'].apply(lambda x: grade_stat(x, fg_thresholds)))
    df.insert(df.columns.get_loc('FT%') + 1, 'FT%_Grade', df['FT%'].apply(lambda x: grade_stat(x, ftpg_thresholds)))
    df.insert(df.columns.get_loc('3P%') + 1, '3P%_Grade', df['3P%'].apply(lambda x: grade_stat(x, threepg_thresholds)))
    df.insert(df.columns.get_loc('RPG') + 1, 'RPG_Grade', df['RPG'].apply(lambda x: grade_stat(x, rpg_thresholds)))
    df.insert(df.columns.get_loc('APG') + 1, 'APG_Grade', df['APG'].apply(lambda x: grade_stat(x, apg_thresholds)))
    df.insert(df.columns.get_loc('SPG') + 1, 'SPG_Grade', df['SPG'].apply(lambda x: grade_stat(x, spg_thresholds)))
    df.insert(df.columns.get_loc('BPG') + 1, 'BPG_Grade', df['BPG'].apply(lambda x: grade_stat(x, bpg_thresholds)))

    grade_columns = [col for col in df.columns if '_Grade' in col]
    
    # Calculate overall grade as the average of all graded stats for each player
    df['OVR_Grade'] = df[grade_columns].mean(axis=1).apply(lambda x: int(x) if x == int(x) else int(x) + 1)
    
    # Save graded data
    df.to_csv("graded_ncaa_player_stats.csv", index=False)
    print("Graded stats saved to 'graded_ncaa_player_stats.csv'")

# Example execution
grade_ncaa_stats()