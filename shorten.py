import os, random

# can use to remove a few image, if you accidently added to many images..

CAR_DIR = "data/car/"
NOT_CAR = "data/notcar/"

cars = os.listdir(CAR_DIR)
notcars = os.listdir(NOT_CAR)
while len(cars) > 10000:
    try:
        os.remove(CAR_DIR + random.choice(cars))
        cars = os.listdir(CAR_DIR)
    except Exception as e:
        pass

while len(notcars) > 10000:
    try:
        os.remove(NOT_CAR + random.choice(notcars))
        notcars = os.listdir(NOT_CAR)
    except Exception as e:
        pass
