import os
from shutil import copy
from random import choice

# set your own
# will be scanned recursively
BASE_CAR_SOURCE_DIRECTORY = "D:\\Projects\\CarRecognizer\\data2\\autoscout-data"
BASE_NOTCAR_SOURCE_DIRECTORY = "D:\\Projects\\CarRecognizer\\data2\\autoscout-data\\deleted"
DESTINATION_CAR_DIRECTORY = "data\\car\\"
DESTINATION_NOTCAR_DIRECTORY = "data\\notcar"

print("Loading data started")

LIMIT = 2000
for i in range(LIMIT):
    folder_path = BASE_CAR_SOURCE_DIRECTORY
    while os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        if len(files) == 0:
            # check if directory is empty, if yes, step up
            folder_path = BASE_CAR_SOURCE_DIRECTORY
            continue
        folder_path = folder_path + "/" + choice(files)
        if not os.path.isdir(folder_path) and len(files) < 1000:
            # we reached the bottom of the directory-system, and check if it has a minimum amount of data,
            #  if not step up, this category is irrelevant
            folder_path = BASE_CAR_SOURCE_DIRECTORY
            continue
    copy(folder_path, DESTINATION_CAR_DIRECTORY)

for i in range(LIMIT):
    folder_path = BASE_NOTCAR_SOURCE_DIRECTORY
    while os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        if len(files) == 0:
            folder_path = BASE_CAR_SOURCE_DIRECTORY
            continue
        folder_path = folder_path + "/" + choice(files)
        if not os.path.isdir(folder_path) and len(files) < 1000:
            folder_path = BASE_CAR_SOURCE_DIRECTORY
            continue
    copy(folder_path, DESTINATION_NOTCAR_DIRECTORY)


