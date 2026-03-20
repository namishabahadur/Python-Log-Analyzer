import os
import shutil

# Folder to organize
folder_path = "test_folder"

# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}

# Create folders if not exist
for category in file_types:
    os.makedirs(os.path.join(folder_path, category), exist_ok=True)

# Move files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        moved = False
        for category, extensions in file_types.items():
            for ext in extensions:
                if file.endswith(ext):
                    shutil.move(file_path, os.path.join(folder_path, category))
                    moved = True
                    break
            if moved:
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others"))

print("Files organized successfully!")
