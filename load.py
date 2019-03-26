import os
from shutil import copy
from random import choice

# set your own
# will be scanned recursively
BASE_CAR_SOURCE_DIRECTORY = "D:\\Projects\\CarRecognizer\\data\\autoscout2"
BASE_NOTCAR_SOURCE_DIRECTORY = "D:\\Projects\\CarRecognizer\\data\\deleted"
DESTINATION_CAR_DIRECTORY = "data\\car\\"
DESTINATION_NOTCAR_DIRECTORY = "data\\notcar"

LIMIT = 1000
for i in range(LIMIT):
    folder_path = BASE_CAR_SOURCE_DIRECTORY
    while os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        if len(files) == 0:
            folder_path = BASE_CAR_SOURCE_DIRECTORY
            continue
        folder_path = folder_path + "/" + choice(files)
    copy(folder_path, DESTINATION_CAR_DIRECTORY)

for i in range(LIMIT):
    folder_path = BASE_NOTCAR_SOURCE_DIRECTORY
    while os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        if len(files) == 0:
            folder_path = BASE_NOTCAR_SOURCE_DIRECTORY
            continue
        folder_path = folder_path + "/" + choice(files)
    copy(folder_path, DESTINATION_NOTCAR_DIRECTORY)


