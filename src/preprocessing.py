from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_generators():

    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=25,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    validation_datagen = ImageDataGenerator(
        rescale=1./255
    )

    return train_datagen, validation_datagen