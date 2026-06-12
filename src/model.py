from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Dense,
    Dropout,
    BatchNormalization,
    GlobalAveragePooling2D
)

def build_model():

    model = Sequential()

    model.add(
        Conv2D(
            32,
            (3,3),
            activation='relu',
            input_shape=(96,96,3)
        )
    )

    model.add(BatchNormalization())
    model.add(MaxPooling2D(2,2))

    model.add(
        Conv2D(
            64,
            (3,3),
            activation='relu'
        )
    )

    model.add(BatchNormalization())
    model.add(MaxPooling2D(2,2))

    model.add(
        Conv2D(
            128,
            (3,3),
            activation='relu'
        )
    )

    model.add(BatchNormalization())
    model.add(MaxPooling2D(2,2))

    model.add(GlobalAveragePooling2D())

    model.add(Dense(128, activation='relu'))

    model.add(Dropout(0.5))

    model.add(Dense(1, activation='sigmoid'))

    return model