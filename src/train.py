from dataset import load_dataset
from model import build_model

train_data, validation_data = load_dataset()

model = build_model()

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    train_data,
    epochs=10,
    validation_data=validation_data
)

model.save("../models/dog_cat_model.h5")