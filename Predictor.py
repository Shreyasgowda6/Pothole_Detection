import numpy as np
import cv2
import glob
from keras.models import Sequential
from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

global size
size = 100
model = Sequential()
# Update the path link to the default path on your computer
model = load_model(r"Default\Path\To\Your\Model\sample.h5")


# X_test = np.load('./models/trainData/128x72x3x10000/X_test.npy')
# y_test = np.load('./models/trainData/128x72x3x10000/y_test.npy')

## load Testing data : non-pothole
nonPotholeTestImages = glob.glob(r"Default\Path\To\Your\Dataset\test\Plain/*.jpg")

# nonPotholeTrainImages.extend(glob.glob("C:/Users/anant/Desktop/pothole-and-plain-rode-images/My Dataset/train/Plain/*.jpeg"))
# nonPotholeTrainImages.extend(glob.glob("C:/Users/anant/Desktop/pothole-and-plain-rode-images/My Dataset/train/Plain/*.png"))

test2 = [cv2.imread(img, 0) for img in nonPotholeTestImages]
for i in range(0, len(test2)):
    test2[i] = cv2.resize(test2[i], (size, size))
temp4 = np.asarray(test2)

## load Testing data : potholes
potholeTestImages = glob.glob(r"Default\Path\To\Your\Dataset\test\Pothole/*.jpg")

# nonPotholeTrainImages.extend(glob.glob("C:/Users/anant/Desktop/pothole-and-plain-rode-images/My Dataset/train/Plain/*.jpeg"))
# nonPotholeTrainImages.extend(glob.glob("C:/Users/anant/Desktop/pothole-and-plain-rode-images/My Dataset/train/Plain/*.png"))


test1 = [cv2.imread(img, 0) for img in potholeTestImages]
for i in range(0, len(test1)):
    test1[i] = cv2.resize(test1[i], (size, size))
temp3 = np.asarray(test1)

X_test = []
X_test.extend(temp3)
X_test.extend(temp4)
X_test = np.asarray(X_test)

X_test = X_test.reshape(X_test.shape[0], size, size, 1)

y_test1 = np.ones([temp3.shape[0]], dtype=int)
y_test2 = np.zeros([temp4.shape[0]], dtype=int)

y_test = []
y_test.extend(y_test1)
y_test.extend(y_test2)
y_test = np.asarray(y_test)

y_test = to_categorical(y_test)

predicted_probabilities = model.predict(X_test)
for i in range(len(X_test)):
    print(">>> Predicted=%s" % (predicted_probabilities[i]))

# metrics = model.evaluate(X_test, y_test)
# for metric_i in range(len(model.metrics_names)):
#     metric_name = model.metrics_names[metric_i]
#     metric_value = metrics[metric_i]
#     print('{}: {}'.format(metric_name, metric_value))


