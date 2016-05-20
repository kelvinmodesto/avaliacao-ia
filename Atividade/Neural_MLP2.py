import numpy as np
import matplotlib.pyplot as plt

class Perceptron(object):

    def __init__(self, eta=0.01, epochs=50):
        self.eta = eta
        self.epochs = epochs

    def train(self, X, y):

        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.epochs):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] +=  update * xi
                self.w_[0] +=  update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


import pandas as pd
"""
file = open('iris.txt', 'r')

cs = [None] * 150
ls = [None] * 150
cp = [None] * 150
lp = [None] * 150

count = 0
for line in file:
   # print(line+' ' + line.split(',',)[0])
    cs[count] = line.split(',')[0]
    ls[count] = line.split(',')[1]
    cp[count] = line.split(',')[2]
    lp[count] = line.split(',')[3]
    count += 1
"""

import pandas as pd
import random
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

"""
# setosa and versicolor
y = df.iloc[0:150, 4].values
print()

y = np.where(y == 'Iris-setosa', -1, 1)


# sepal length and petal length
X = df.iloc[0:100, [0,2]].values


#matplotlib inline
import matplotlib.pyplot as plt
from mlxtend.evaluate import plot_decision_regions

ppn = Perceptron(epochs=10, eta=0.1)

ppn.train(X, y)
print('Weights: %s' % ppn.w_)
plot_decision_regions(X, y,  clf=ppn)
plt.title('Perceptron')
plt.xlabel('sepal length ')
plt.ylabel('petal length')
plt.show()

plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
plt.xlabel('Iterations')
plt.ylabel('Missclassifications')
plt.show()"""

import matplotlib.pyplot as plt
from mlxtend.evaluate import plot_decision_regions
# versicolor, virginica, setosa
y2 = df.iloc[45:80, 4].values
y2 = np.where(y2 == 'Iris-virginica', -1, 1)

# sepal width and petal width
X2 = df.iloc[45:80,  [1,3]].values

ppn = Perceptron(epochs=10, eta=0.01)
ppn.train(X2, y2)

y2 = df.iloc[0:150, 4].values
y2 = np.where(y2 == 'Iris-virginica', -1, 1)
X2 = df.iloc[0:150, [1,3]].values
plot_decision_regions(X2, y2, clf=ppn)
plt.show()

plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
plt.xlabel('Iterations')
plt.ylabel('Missclassifications')
plt.show()