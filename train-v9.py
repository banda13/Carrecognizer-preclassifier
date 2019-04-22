from keras import Sequential
from keras.callbacks import TensorBoard
from keras.layers import Conv2D, Flatten, Dense, Activation, MaxPooling2D, Dropout
from keras.optimizers import SGD, RMSprop
from keras.regularizers import Regularizer, l2, l1_l2
from keras_preprocessing.image import ImageDataGenerator

NAME = "v9"
TRAIN_DIR = "data/train/"
VALIDATE_DIR = "data/validate/"
IMG_WIDTH, IMG_HEIGHT = 150, 150

BATCH_SIZE = 64
EPOCHS = 10
TRAIN_STEP = 200
VALIDATION_STEP = 50

FILE_NAME = "model/%s-mymodel.h5" % NAME

try:
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid', kernel_regularizer=l1_l2(0.01)))

    model.compile(loss='binary_crossentropy',
                  optimizer=RMSprop(lr=0.001, rho=0.9, epsilon=None, decay=0.0),
                  metrics=['accuracy'])

    train_datagen = ImageDataGenerator(
            rescale=1./255,
            shear_range=0.3,
            zoom_range=0.3,
            horizontal_flip=False)

    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
            TRAIN_DIR,
            target_size=(IMG_WIDTH, IMG_HEIGHT),
            batch_size=BATCH_SIZE,
            class_mode='binary')

    validation_generator = test_datagen.flow_from_directory(
            VALIDATE_DIR,
            target_size=(IMG_WIDTH, IMG_HEIGHT),
            batch_size=BATCH_SIZE,
            class_mode='binary')

    callbacks = [TensorBoard(log_dir="logs/{}".format(NAME))]

    model.fit_generator(
            train_generator,
            callbacks=callbacks,
            steps_per_epoch=TRAIN_STEP,
            epochs=EPOCHS,
            validation_data=validation_generator,
            validation_steps=VALIDATION_STEP)

    score = model.evaluate_generator(validation_generator, VALIDATION_STEP/BATCH_SIZE, workers=12)
    scores = model.predict_generator(validation_generator, VALIDATION_STEP/BATCH_SIZE, workers=12)
    model.save(FILE_NAME)

    with open("logs/mylog.txt", "a") as f:
        f.write("\n\n--------" + NAME + "----------\n")
        f.write(str(score) + "\n")
except Exception as e:
    with open("logs/mylog.txt", "a") as f:
        f.write("\n\n--------" + NAME + "----------\n")
        f.write("Failed")


