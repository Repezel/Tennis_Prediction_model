import pandas as pd
import glob
import os

# 📁 Your folder path
folder_path = r"C:\Users\rohan\Downloads\new"

# 📄 Get all CSV files
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# 🎯 Required columns
required_columns = [
    "tourney_id", "tourney_name", "surface", "draw_size", "tourney_level",
    "tourney_date", "match_num",
    "winner_id", "winner_seed", "winner_entry", "winner_name", "winner_hand",
    "winner_ht", "winner_ioc", "winner_age",
    "loser_id", "loser_seed", "loser_entry", "loser_name", "loser_hand",
    "loser_ht", "loser_ioc", "loser_age",
    "score", "best_of", "round"
]

all_data = []

for file in csv_files:
    try:
        df = pd.read_csv(file, low_memory=False)

        # Keep only required columns safely
        df = df[[col for col in required_columns if col in df.columns]]

        all_data.append(df)

        print(f"✅ Processed: {file}")

    except Exception as e:
        print(f"❌ Error in {file}: {e}")

# 🔗 Combine all files
final_df = pd.concat(all_data, ignore_index=True)

# 💾 Save output
output_file = os.path.join(folder_path, "final_combined.csv")
final_df.to_csv(output_file, index=False)

print(f"\n🎉 Done! File saved at:\n{output_file}")