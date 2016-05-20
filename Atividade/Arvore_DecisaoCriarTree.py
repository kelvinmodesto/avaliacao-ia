import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier


iris = load_iris()

#print ("feature names: " + str(iris.feature_names))
#print ("target names: " + str(iris.target_names))
#print ("first data measurements: " + str(iris.data[0]))
#print ("first data label: " + str(iris.target[0]))

test_idx = [0, 50, 100] # index of measurements to remove (one of each type)

train_target = np.delete(iris.target, test_idx) # training labels (w/o testing)
train_data = np.delete(iris.data, test_idx, axis=0) # training data (w/o testing)

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print (clf.predict(test_data))

# visualize tree
from sklearn.externals.six import StringIO
import pydotplus
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")