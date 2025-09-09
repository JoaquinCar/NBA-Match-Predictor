import shutil

cache_path = r"C:\Users\joaqu\.cache\kagglehub\datasets\eoinamoore\historical-nba-data-and-player-box-scores\versions\239"
project_path = r"C:\Users\joaqu\Documents\NBA\data"

shutil.copytree(cache_path, project_path, dirs_exist_ok=True)