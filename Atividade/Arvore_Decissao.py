import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from random import randint

n_classes = 3
plot_colors = "bry" #cor blue red e yellow
plot_step = 0.02

#  Carrga os dados da biblioteca
iris = load_iris()
print ("feature names: " + str(iris.feature_names))
print ("target names: " + str(iris.target_names))
print ("first data measurements: " + str(iris.data[0]))
print ("first data label: " + str(iris.target[0]))

#teste com grupos randomicos
for pairidx, pair in enumerate([[randint(0,3), randint(0,3)], [randint(0,3), randint(0,3)], [randint(0,3), randint(0,3)],
                                [randint(0,3), randint(0,3)], [randint(0,3), randint(0,3)], [randint(0,3), randint(0,3)]]):

#grupos divididos corretamente
#for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3],
                                #[1, 2], [1, 3], [2, 3]]):
    # ira ser com um par de caracteristicas
    X = iris.data[:, pair]
    y = iris.target

    # Embaralha os dados para analise
    idx = np.arange(X.shape[0])
    np.random.seed(13)
    np.random.shuffle(idx)
    X = X[idx]
    y = y[idx]

    # Uniformiza os dados
    mean = X.mean(axis=0)
    std = X.std(axis=0)
    X = (X - mean) / std

    # treina a arvore de decisão usando a biblioteca
    clf = DecisionTreeClassifier().fit(X, y)

    # Plota os limite do graficos
    plt.subplot(2, 3, pairidx + 1)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

    plt.xlabel(iris.feature_names[pair[0]])
    plt.ylabel(iris.feature_names[pair[1]])
    plt.axis("tight")

    # Plota os pontos de treinamento
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i],
                    cmap=plt.cm.Paired)

    plt.axis("tight")

plt.suptitle("Superfície da Árvore de decisão")
plt.legend()
plt.show()

## Treinar classificador

import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()

test_idx = [0, 50, 100] # index of measurements to remove (one of each type)

print ("Teste idx: " + str(test_idx))


train_target = np.delete(iris.target, test_idx) # grupo alvo(treinar a label)
train_data = np.delete(iris.data, test_idx, axis=0) # grupo de data de teste

print ("train_data: " + str(train_data))
print ("train_target: " + str(train_target))

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

#Classificar em N arvores
""""
test_idx = [50, 80, 100]
train_data = np.delete(iris.data, test_idx, axis=0) # training data (w/o testing)
clf.fit(train_data, train_target)"""
#***********

print ("test_data" + str(clf.predict(test_data)))

# visualize tree
import matplotlib.pyplot as plt
from sklearn.externals.six import StringIO
import pydotplus
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

graph.write_png("iris.png")#criar imagem com a Arvore de decisão
