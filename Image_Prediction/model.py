from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# data reading
imgs = np.load('image.npz')['arr_0']
labels = pd.read_csv('labels.csv')['labels']

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# splitting the data
Xtrain, Xtest, Ytrain, Ytest = train_test_split(
    imgs, labels, test_size=2000, train_size=5000)

# making a model
model = LogisticRegression(solver='saga', multi_class='multinomial')
model.fit(Xtrain, Ytrain)
