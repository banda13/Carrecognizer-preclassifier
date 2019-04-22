import os
from shutil import copy
from random import shuffle

# ugh so ugly, please refactor the duplications

CAR_SOURCE_FOLDER = "data/car/"
NOTCAR_SOURCE_FOLDER = "data/notcar/"
TRAIN_DIR = "data/train"
CAR_TRAIN_DIR = TRAIN_DIR + "/car"
NOTCAR_TRAIN_DIR = TRAIN_DIR + "/notcar"
TEST_DIR = "data/test"
CAR_TEST_DIR = TEST_DIR + "/car"
NOTCAR_TEST_DIR = TEST_DIR + "/notcar"
VALIDATE_DIR = "data/validate"
CAR_VALIDATE_DIR = VALIDATE_DIR + "/car"
NOTCAR_VALIDATE_DIR = VALIDATE_DIR + "/notcar"

data_distribution = {'train': 0.6, 'test': 0.2, 'validate': 0.2}

print("checking if all necessary directory exists, if not create it")
if not os.path.isdir(CAR_TRAIN_DIR):
    os.makedirs(CAR_TRAIN_DIR)
if not os.path.isdir(NOTCAR_TRAIN_DIR):
    os.makedirs(NOTCAR_TRAIN_DIR)

if not os.path.isdir(CAR_TEST_DIR):
    os.makedirs(CAR_TEST_DIR)
if not os.path.isdir(NOTCAR_TEST_DIR):
    os.makedirs(NOTCAR_TEST_DIR)

if not os.path.isdir(CAR_VALIDATE_DIR):
    os.makedirs(CAR_VALIDATE_DIR)
if not os.path.isdir(NOTCAR_VALIDATE_DIR):
    os.makedirs(NOTCAR_VALIDATE_DIR)

print("read file names to memory, its ok, it wont be so many.. (few 1000)")
car_files = os.listdir(CAR_SOURCE_FOLDER)
not_car_files = os.listdir(NOTCAR_SOURCE_FOLDER)

print("shuffle them to make it more interesting")
shuffle(car_files)
shuffle(not_car_files)

print("separate data")
files_length = min(len(car_files), len(not_car_files))
train_end_idx = round(files_length * data_distribution['train'])
car_train_files = car_files[0: train_end_idx]
not_car_train_files = not_car_files[0: train_end_idx]

test_end_idx = train_end_idx + round(files_length * data_distribution['test'])
car_test_files = car_files[train_end_idx: test_end_idx]
not_car_test_files = not_car_files[train_end_idx: test_end_idx]

validate_end_idx = test_end_idx + round(files_length * data_distribution['validate'])
car_validate_files = car_files[test_end_idx:validate_end_idx]
not_car_validate_files = not_car_files[test_end_idx:validate_end_idx]

print("do copy")
for f in car_train_files:
    copy(CAR_SOURCE_FOLDER + f, CAR_TRAIN_DIR)

for f in car_test_files:
    copy(CAR_SOURCE_FOLDER + f, CAR_TEST_DIR)

for f in car_validate_files:
    copy(CAR_SOURCE_FOLDER + f, CAR_VALIDATE_DIR)

for f in not_car_train_files:
    copy(NOTCAR_SOURCE_FOLDER + f, NOTCAR_TRAIN_DIR)

for f in not_car_test_files:
    copy(NOTCAR_SOURCE_FOLDER + f, NOTCAR_TEST_DIR)

for f in not_car_validate_files:
    copy(NOTCAR_SOURCE_FOLDER + f, NOTCAR_VALIDATE_DIR)
