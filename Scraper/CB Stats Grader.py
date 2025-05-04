# Import required libraries for data processing and numerical operations
import pandas as pd
import numpy as np

# Load position-based statistical summary data
summary_file_path = "Position-based_Player_Stats_Summary.csv"
summary_df = pd.read_csv(summary_file_path, header=None)

# Filter and process position-specific maximum values
positions = ["C", "F", "G", "PG"]
position_max_values = summary_df[summary_df[0].isin(positions)].copy()

# Define column names for statistical metrics
position_max_values.columns = [
    "Position", "GP_med", "GP_max", "GP_min",
    "MIN_med", "MIN_max", "MIN_min",
    "PTS_med", "PTS_max", "PTS_min",
    "FGM_med", "FGM_max", "FGM_min",
    "FGA_med", "FGA_max", "FGA_min",
    "FG%_med", "FG%_max", "FG%_min",
    "3PA_med", "3PA_max", "3PA_min",
    "3P%_med", "3P%_max", "3P%_min",
    "FTM_med", "FTM_max", "FTM_min",
    "FTA_med", "FTA_max", "FTA_min",
    "FT%_med", "FT%_max", "FT%_min",
    "REB_med", "REB_max", "REB_min",
    "AST_med", "AST_max", "AST_min",
    "STL_med", "STL_max", "STL_min",
    "BLK_med", "BLK_max", "BLK_min",
    "TO_med", "TO_max", "TO_min"
]

# Select relevant statistical columns for grading
position_max_values = position_max_values[
    ["Position", "PTS_max", "FG%_max", "FT%_max", "3P%_max", "REB_max", "AST_max", "STL_max", "BLK_max"]
]

# Convert position to index and ensure numeric values
position_max_values.set_index("Position", inplace=True)
position_max_values = position_max_values.apply(pd.to_numeric, errors='coerce')

# Load player statistics from ESPN data
player_stats_file_path = "espn_ncaa_player_stats.csv"
player_df = pd.read_csv(player_stats_file_path)

# Function to standardize position categories
def categorize_position(pos):
    position_map = {'PG': 'PG', 'G': 'G', 'F': 'F', 'C': 'C'}
    return position_map.get(pos, 'Unknown')

# Apply position categorization to player data
player_df['Position Group'] = player_df['Pos'].apply(categorize_position)

# Define statistics to be graded and calculate position-based statistics
stats_to_grade = ["PTS", "FG%", "FT%", "3P%", "REB", "AST", "STL", "BLK"]
position_stats = player_df.groupby("Position Group")[stats_to_grade].agg(["mean", "std"])

# Function to grade individual statistics based on position averages
def grade_stat(value, mean, std_dev):
    # Handle missing values
    if pd.isna(value) or pd.isna(mean) or pd.isna(std_dev):
        return 60  
    
    # Define grading scale
    min_grade = 60
    max_grade = 99
    
    # Calculate statistical bounds
    lower_bound = mean - 2 * std_dev  
    upper_bound = mean + 2 * std_dev  

    # Calculate grade based on value's position within bounds
    if value <= lower_bound:
        return min_grade
    elif value >= upper_bound:
        return max_grade
    else:
        return int(np.round(np.interp(value, [lower_bound, upper_bound], [min_grade, max_grade])))

# Calculate grades for each statistical category
grades = {}
for stat in stats_to_grade:
    grades[f"{stat}_Grade"] = player_df.apply(
        lambda row: grade_stat(
            row[stat], 
            position_stats.loc[row["Position Group"], (stat, "mean")],
            position_stats.loc[row["Position Group"], (stat, "std")]
        ) if row["Position Group"] in position_stats.index else 60,
        axis=1
    )

# Create DataFrame for grades
grades_df = pd.DataFrame(grades)

# Organize columns for final output
ordered_columns = []
for stat in stats_to_grade:
    ordered_columns.append(stat)  
    ordered_columns.append(f"{stat}_Grade")  

# Define metadata columns and final column order
metadata_columns = ["Rank", "Player Name", "Team", "Pos", "GP", "MIN", "Position Group"]
ordered_columns = metadata_columns + ordered_columns

# Combine player data with grades and organize columns
formatted_df = pd.concat([player_df, grades_df], axis=1)
formatted_df = formatted_df[ordered_columns]  

# Calculate overall grade as average of individual stat grades
grade_columns = [col for col in formatted_df.columns if '_Grade' in col]
formatted_df["OVR_Grade"] = formatted_df[grade_columns].mean(axis=1).astype(int)

# Save graded statistics to CSV file
output_file = "graded_ncaa_player_stats.csv"
formatted_df.to_csv(output_file, index=False)
print(f"Graded stats saved to {output_file}")








