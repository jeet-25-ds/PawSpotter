import os
import shutil
from sklearn.model_selection import train_test_split

original_dataset_dir = r"H:\jeetprac\Cnn\train\train"
base_dir = r"H:\jeetprac\Cnn\dataset"   
train_dir = os.path.join(base_dir, "train")
validation_dir = os.path.join(base_dir, "validation")

os.makedirs(train_dir, exist_ok=True)
os.makedirs(validation_dir, exist_ok=True)

train_cats_dir = os.path.join(train_dir, "cats")
train_dogs_dir = os.path.join(train_dir, "dogs")

validation_cats_dir = os.path.join(validation_dir, "cats")
validation_dogs_dir = os.path.join(validation_dir, "dogs")

os.makedirs(train_cats_dir, exist_ok=True)
os.makedirs(train_dogs_dir, exist_ok=True)

os.makedirs(validation_cats_dir, exist_ok=True)
os.makedirs(validation_dogs_dir, exist_ok=True)

all_images = os.listdir(original_dataset_dir)

cat_images = [img for img in all_images if img.startswith("cat")]
dog_images = [img for img in all_images if img.startswith("dog")]

train_cats, val_cats = train_test_split(
    cat_images,
    test_size=0.2,
    random_state=42
)

train_dogs, val_dogs = train_test_split(
    dog_images,
    test_size=0.2,
    random_state=42
)


for img in train_cats:
    src = os.path.join(original_dataset_dir, img)
    dst = os.path.join(train_cats_dir, img)

    shutil.copyfile(src, dst)

for img in val_cats:
    src = os.path.join(original_dataset_dir, img)
    dst = os.path.join(validation_cats_dir, img)

    shutil.copyfile(src, dst)

for img in train_dogs:
    src = os.path.join(original_dataset_dir, img)
    dst = os.path.join(train_dogs_dir, img)

    shutil.copyfile(src, dst)

for img in val_dogs:
    src = os.path.join(original_dataset_dir, img)
    dst = os.path.join(validation_dogs_dir, img)

    shutil.copyfile(src, dst)