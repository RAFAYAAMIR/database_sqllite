import sqlite3
import numpy as np
import sys

IS_PYTHON3 = sys.version_info[0] >= 3

def array_to_blob(array):
    if IS_PYTHON3:
        return array.tostring()
    else:
        return np.getbuffer(array)
    
temp_db_path = "/home/rafay/Documents/rafay/projects/other/DrSohaibCVCourse_Lums/Practice/temp_dump/1688043067167_10936_YR63UZR_overspeeding_R30_C4_E2/database.db"

conn = sqlite3.connect(temp_db_path)

print("Opened database successfully")

cursor = conn.execute("SELECT image_id, rows, cols, data from keypoints")
data = {}
for row in cursor:
    if row[3] is not None:
        data[row[0]] = np.frombuffer(row[3], dtype=np.float32).reshape(row[1],row[2]).copy()


print("Operation done successfully for database of: ", temp_db_path.split('/')[-2])
# conn.close()

# database of 1688043067167_10936_YR63UZR_overspeeding_R30_C4_E2
# original value data[1][0]=[594.8164 286.0804]

data[1][0] = np.array([0.0,0.0], dtype=np.float32)
image_id_1_keypoints_blob = array_to_blob(data[1])
print("shape:    ", data[1].shape)
query = "INSERT INTO keypoints VALUES (?, ?, ?, ?)"
data_tuple = ((1,), data[1].shape, (image_id_1_keypoints_blob),)
conn.execute(query, (1,) + data[1].shape + (image_id_1_keypoints_blob,),)
# conn.execute("UPDATE keypoints set data = "+image_id_1_keypoints_blob+" where image_id = 1")
conn.commit()
conn.close()
