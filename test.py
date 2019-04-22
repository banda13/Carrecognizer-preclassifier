import os
from shutil import copy

import numpy as np
from keras.engine.saving import load_model
from keras_preprocessing.image import load_img, img_to_array

CAR_TEST_DIR = "data/test/car/"
NOTCAR_TEST_DIR = "data/test/notcar/"
CAR_PREDICTION_DIR = "data/prediction/car"
NOTCAR_PREDICTION_DIR = "data/prediction/notcar"
FILE_NAME = "model/v1-mymodel.h5"
IMG_WIDTH, IMG_HEIGHT = 150, 150

car_files = os.listdir(CAR_TEST_DIR)
not_car_files = os.listdir(NOTCAR_TEST_DIR)

files_length = min(len(car_files), len(not_car_files))
boom_baby = 0
not_boom_baby = 0

model = load_model(FILE_NAME)

for f in car_files:
    image = load_img(CAR_TEST_DIR + f, target_size=(IMG_WIDTH, IMG_HEIGHT))
    image = img_to_array(image)
    image = image / 255
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    if prediction[0][0] <= 0.1:
        boom_baby += 1
        # copy(CAR_TEST_DIR + f, CAR_PREDICTION_DIR)
    else:
        copy(CAR_TEST_DIR + f, NOTCAR_PREDICTION_DIR)

print('-----')

for f in not_car_files:
    image = load_img(NOTCAR_TEST_DIR + f, target_size=(IMG_WIDTH, IMG_HEIGHT))
    image = img_to_array(image)
    image = image / 255
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    if prediction[0][0] >= 0.1:
        not_boom_baby += 1
        # copy(NOTCAR_TEST_DIR + f, NOTCAR_PREDICTION_DIR)
    else:
        copy(NOTCAR_TEST_DIR + f, CAR_PREDICTION_DIR)


print("%d car recognizer good from %d, %d missed. %f percent" % (boom_baby, files_length, (files_length - boom_baby),boom_baby / float(files_length)))
print("%d notcar recognizer good from %d, %d missed %f percent" % (not_boom_baby, files_length,(files_length - not_boom_baby), not_boom_baby / float(files_length)))