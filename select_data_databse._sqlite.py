import sqlite3

db_path = "/home/rafay/Downloads/colmap-3.8/temp_dump/1688043067167_10936_YR63UZR_overspeeding_R30_C4_E2/database.db"
temp_db_path = "/home/rafay/Documents/rafay/projects/other/DrSohaibCVCourse_Lums/Practice/database.db"

conn = sqlite3.connect(temp_db_path)

print("Opened database successfully")

cursor = conn.execute("SELECT image_id, rows, cols, data from keypoints")
for row in cursor:
    print("image_id = ", row[0])
    print("rows = ", row[1])
    print("cols = ", row[2])
    print("data = ", row[3], "\n")
    # print("\n")

print("Operation done successfully")
conn.close()
