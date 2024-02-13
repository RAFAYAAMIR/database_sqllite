import sqlite3
from PIL import Image
import numpy as np

db_path = "/home/rafay/Downloads/colmap-3.8/temp_dump/1688043067167_10936_YR63UZR_overspeeding_R30_C4_E2/database.db"
temp_db_path = "/home/rafay/Documents/rafay/projects/other/DrSohaibCVCourse_Lums/Practice/database.db"


def convert_data(data, file_name):
    # Convert binary format to 
    # images or files data
    with open(file_name, 'wb') as file:
        file.write(data)
    img = Image.open(file_name)
    print(img)

conn = sqlite3.connect(temp_db_path)

print("Opened database successfully")

cursor = conn.execute("SELECT image_id, rows, cols, data from keypoints")
for row in cursor:
    print("image_id = ", row[0])
    print("rows = ", row[1])
    print("cols = ", row[2])
    data = np.frombuffer(row[3], dtype=np.float32).reshape(row[1],row[2])
    
    print(type(data))
    print("data:    ",data)
    print("data shape:    ", data.shape)
    print("\n")

print("Operation done successfully")
conn.close()
