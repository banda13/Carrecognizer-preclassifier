from keras import Sequential
from keras.layers import Conv2D, Flatten, Dense, Activation, MaxPooling2D, Dropout
from keras_preprocessing.image import ImageDataGenerator

TRAIN_DIR = "data/train/"
VALIDATE_DIR = "data/validate/"
IMG_WIDTH, IMG_HEIGHT = 150, 150

BATCH_SIZE = 32
EPOCHS = 20
TRAIN_STEP = 100
VALIDATION_STEP = 20

FILE_NAME = "model/mymodel.h5"

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

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

model.fit_generator(
        train_generator,
        steps_per_epoch=TRAIN_STEP,
        epochs=EPOCHS,
        validation_data=validation_generator,
        validation_steps=VALIDATION_STEP)

model.save(FILE_NAME)

