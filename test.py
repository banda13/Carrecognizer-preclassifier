import os
import numpy as np
from keras.engine.saving import load_model
from keras_preprocessing.image import load_img, img_to_array

CAR_TEST_DIR = "data/test/car/"
NOTCAR_TEST_DIR = "data/train/car/"
FILE_NAME = "model/mymodel.h5"
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
    print(prediction)
