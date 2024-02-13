import sqlite3
from PIL import Image
import numpy as np

db_path_1688043067167_10936_YR63UZR_overspeeding_R30_C4_E2 = "/home/rafay/Documents/rafay/projects/other/DrSohaibCVCourse_Lums/Practice/temp_dump/1688043067167_10936_YR63UZR_overspeeding_R30_C4_E2/database.db"
db_path_1688043067167_10936_YR63UZR_overspeeding_keypointsR30_C4_E97 = "/home/rafay/Documents/rafay/projects/other/DrSohaibCVCourse_Lums/Practice/temp_dump/1688043067167_10936_YR63UZR_overspeeding_keypointsR30_C4_E97/database.db"
db_path_1688043067167_10936_YR63UZR_overspeeding_keypointsR30_C4_E18 = "/home/rafay/Documents/rafay/projects/other/DrSohaibCVCourse_Lums/Practice/temp_dump/1688043067167_10936_YR63UZR_overspeeding_keypointsR30_C4_E18/database.db"
db_path_1688043067167_10936_YR63UZR_overspeeding_keypointsR30_C4 = "/home/rafay/Documents/rafay/projects/other/DrSohaibCVCourse_Lums/Practice/temp_dump/1688043067167_10936_YR63UZR_overspeeding_keypointsR30_C4/database.db"

temp_db_paths = [db_path_1688043067167_10936_YR63UZR_overspeeding_R30_C4_E2,
                db_path_1688043067167_10936_YR63UZR_overspeeding_keypointsR30_C4_E97,
                db_path_1688043067167_10936_YR63UZR_overspeeding_keypointsR30_C4_E18,
                db_path_1688043067167_10936_YR63UZR_overspeeding_keypointsR30_C4]

def convert_data(data, file_name):
    # Convert binary format to 
    # images or files data
    with open(file_name, 'wb') as file:
        file.write(data)
    img = Image.open(file_name)
    print(img)

all_keypoits = {}
for temp_db_path in temp_db_paths:
    # print(temp_db_path.split('/')[-2])
    conn = sqlite3.connect(temp_db_path)
    # print("Opened database successfully")
    cursor = conn.execute("SELECT image_id, rows, cols, data from keypoints")
    data = {}
    for row in cursor:
        if row[3] is not None:
            data[row[0]] = np.frombuffer(row[3], dtype=np.uint32).reshape(row[1],row[2])
    all_keypoits[temp_db_path.split('/')[-2]] = data
    print("Operation done successfully for database of: ", temp_db_path.split('/')[-2])
    conn.close()

for db_kp in all_keypoits.keys():
    for compare_with in all_keypoits.keys():
        if db_kp is not compare_with:
            print("comparing keypoints of:   ", db_kp, " with ", compare_with)
            for image_id in all_keypoits[db_kp].keys():
                if (all_keypoits[db_kp][image_id] != all_keypoits[compare_with][image_id]).any():
                    print("\n\n\nimage_id:    ", image_id)
                    print("\nall_keypoits[db_kp][image_id]")
                    print(all_keypoits[db_kp][image_id])
                    print("\nall_keypoits[compare_with][image_id]")
                    print(all_keypoits[compare_with][image_id])
