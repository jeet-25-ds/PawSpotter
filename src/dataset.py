from preprocessing import get_generators

def load_dataset():

    train_datagen, validation_datagen = get_generators()

    train_data = train_datagen.flow_from_directory(
        'data/train',
        target_size=(96,96),
        batch_size=64,
        class_mode='binary',
        shuffle=True
    )

    validation_data = validation_datagen.flow_from_directory(
        'data/validation',
        target_size=(96,96),
        batch_size=64,
        class_mode='binary'
    )

    return train_data, validation_data