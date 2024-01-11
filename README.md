## Pothole Detection System using Convolutional Neural Networks
# Overview
This repository contains the code for a Pothole Detection System utilizing Convolutional Neural Networks (CNNs). The system includes both model training using Logistic Regression and a custom Neural Network architecture.

# Features
Model Architecture: The neural network architecture consists of convolutional layers, pooling layers, and fully connected layers designed for effective pothole detection.

Data Processing: The system handles a diverse set of image data for training and testing, including pre-processing steps such as resizing and grayscale conversion.

Model Training: The code includes the implementation of a custom Logistic Regression model and a Neural Network model using TensorFlow and Keras.

# Dataset
The dataset used for training and testing is sourced from the 'My Dataset' directory, containing images of both potholes and non-pothole road surfaces.

# Dependencies
Make sure to install the necessary dependencies before running the code:

bash
Copy code
pip install pandas numpy matplotlib tensorflow opencv-python keras scikit-learn
Usage
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/pothole-detection-system.git
Navigate to the project directory:
bash
Copy code
cd pothole-detection-system
Run the code:
bash
Copy code
python pothole_detection.py
# Model Evaluation
The system provides model evaluation metrics, including accuracy, after training the models on the provided datasets.

# Model Saving
Trained models are saved in both '.h5' and '.json' formats for future use.
