
# PawSpotter – Dog vs Cat Image Classification using CNN

## Overview

PawSpotter is a Deep Learning-based image classification project that identifies whether an uploaded image contains a **Dog** or a **Cat**. The project uses a **Convolutional Neural Network (CNN)** built with TensorFlow/Keras and provides an interactive web interface using Streamlit.

The model is trained on labeled dog and cat images and learns visual features such as edges, textures, shapes, and patterns to accurately classify new images.

This project demonstrates the complete machine learning workflow including data preparation, image preprocessing, CNN model development, training, evaluation, prediction, and deployment through a web application.

---

## Features

* Binary image classification (Dog vs Cat)
* Deep Learning model built using CNN
* Image preprocessing and normalization
* Model training and evaluation pipeline
* Interactive Streamlit web application
* Upload and classify custom images
* Prediction confidence display
* Modular project structure for maintainability

---

## Project Architecture

```text
User Uploads Image
         │
         ▼
 Image Preprocessing
 (Resize & Normalize)
         │
         ▼
  CNN Model (.h5)
         │
         ▼
 Probability Score
         │
         ▼
 Dog or Cat Prediction
         │
         ▼
 Streamlit Web Interface
```

---

## Technologies Used

### Programming Language

* Python

### Deep Learning Framework

* TensorFlow
* Keras

### Web Framework

* Streamlit

### Data Processing

* NumPy
* OpenCV
* Pillow

### Visualization

* Matplotlib

---

## Dataset

The model is trained using a Dog vs Cat image dataset containing labeled images of:

* Dogs
* Cats

The dataset is divided into:

* Training Set
* Validation Set

Images are preprocessed before training to ensure consistency and improve model performance.

### Preprocessing Steps

* Image resizing
* Pixel normalization
* Label encoding
* Dataset organization into train and validation folders

---

## CNN Architecture

The Convolutional Neural Network consists of multiple layers:

### Convolution Layers

Used to extract image features such as:

* Edges
* Textures
* Shapes
* Patterns

### Activation Function

ReLU (Rectified Linear Unit)

### Pooling Layers

MaxPooling layers reduce dimensionality and computational complexity.

### Flatten Layer

Converts feature maps into a one-dimensional vector.

### Dense Layers

Fully connected layers learn higher-level image representations.

### Output Layer

Binary Classification:

* Dog
* Cat

Activation Function:

```python
Sigmoid
```

Loss Function:

```python
Binary Crossentropy
```

Optimizer:

```python
Adam
```

---

## Project Structure

```text
PawSpotter/
│
├── data/
│   ├── train/
│   └── validation/
│
├── models/
│   └── dog_cat_model.h5
│
├── src/
│   ├── dataset.py
│   ├── evaluation.py
│   ├── model.py
│   ├── predict.py
│   ├── prepare_dataset.py
│   ├── preprocessing.py
│   └── train.py
│
├── test_images/
│   └── dog1.jpg
│
├── web/
│   └── app.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/jeet-25-ds/PawSpotter.git
```

### Navigate to Project Folder

```bash
cd PawSpotter
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

To train the CNN model:

```bash
python src/train.py
```

The trained model will be saved inside:

```text
models/dog_cat_model.h5
```

---

## Running Predictions

To predict a single image:

```bash
python src/predict.py
```

The model loads the trained weights and predicts whether the image contains a dog or a cat.

---

## Running the Streamlit Application

Launch the web application:

```bash
streamlit run web/app.py
```

After execution, open:

```text
http://localhost:8501
```

---

## Application Workflow

1. User uploads an image.
2. Image is resized and normalized.
3. CNN model processes the image.
4. Prediction probability is generated.
5. Final classification is displayed.
6. Confidence score is shown to the user.

---

## Sample Output

### Input

Uploaded image of a dog or cat.

### Output

```text
Prediction: Dog
Confidence: 97.4%
```

or

```text
Prediction: Cat
Confidence: 95.8%
```

---

### Future Enhancements

The current version of PawSpotter focuses on binary image classification, identifying whether an uploaded image contains a dog or a cat. Future versions of the project aim to extend its capabilities and improve overall functionality.

1. Dog Breed Classification

Develop a dedicated CNN model trained on dog breed datasets to identify specific breeds such as:

Labrador Retriever
Golden Retriever
German Shepherd
Husky
Beagle
Pug
Rottweiler
Shih Tzu

This enhancement will enable the system to move beyond simple dog detection and provide fine-grained breed identification.

2. Cat Breed Classification

Train a separate CNN model for cat breed recognition, allowing classification of breeds such as:

Persian
Siamese
Bengal
Maine Coon
Ragdoll
British Shorthair

This will provide more detailed and informative predictions for cat images.

3. Hierarchical Prediction Pipeline

Implement a two-stage classification system:

Stage 1: Identify whether the uploaded image contains a Dog or a Cat.

Stage 2: Route the image to the corresponding breed classification model to predict the exact breed.

This architecture will improve scalability and allow specialized models to achieve better performance.

4. Improved CNN Architecture

Experiment with deeper custom CNN architectures and advanced regularization techniques to improve classification accuracy and model generalization.

Potential improvements include:

Additional convolutional layers
Batch Normalization
Dropout optimization
Data augmentation techniques
Hyperparameter tuning

5. Confidence-Based Predictions

Provide confidence scores and prediction probabilities to help users better understand model certainty and reliability.

6. Multi-Animal Classification

Expand the project beyond dogs and cats by supporting additional animal categories and breed-level classification in future versions.
---

## Learning Outcomes

Through this project, the following concepts were implemented and explored:

* Deep Learning Fundamentals
* Convolutional Neural Networks
* Image Preprocessing
* Binary Image Classification
* Model Evaluation
* TensorFlow/Keras
* Streamlit Deployment
* End-to-End Machine Learning Pipeline

---

## Author

**Jeet**

Data Science & Machine Learning Enthusiast

GitHub: https://github.com/jeet-25-ds

---

## License

This project is intended for educational and learning purposes.
