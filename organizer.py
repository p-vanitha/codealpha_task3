import os
import shutil
source_folder = "source_files"
destination_folder = "jpg_files"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
moved_files = 0
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print("Moved:", filename)
        moved_files += 1

print("\n================================")
print("       TASK COMPLETED")
print("================================")
print("Total JPG files moved:", moved_files)