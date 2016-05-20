import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import  dendrogram, linkage

#a = np.random.multivariate_normal([100, 100], [[3, 1], [1, 4]], size=[2,])
#b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[3,])
#X = np.concatenate((a, b),)

#plt.scatter(X[:,0], X[:,1])
#plt.show()

#print(X)


file = open('iris.txt', 'r')

cs = [0] * 150
ls = [0] * 150
cp = [0] * 150
lp = [0] * 150

print(cs)
count = 0
for line in file:
   # print(line+' ' + line.split(',',)[0])
    cs[count] = float(line.split(',')[0])
    ls[count] = float(line.split(',')[1])
    cp[count] = float(line.split(',')[2])
    lp[count] = float(line.split(',')[3])
    count += 1

#criar
tamanho = 50 *3
distancia = [0] * tamanho
for i in range(0, tamanho):
    distancia[i] = np.abs(cs[i] + ls[i])

X = np.column_stack((cs, ls,  distancia, [2] *  (tamanho))) # a coluna preenchida com "2" significa 2 samples
Z = linkage(X, 'ward')# ward, single, complete gerar a matrix linkada

print(X)

plt.plot(cs[:50], ls[:50], 'r.')#Iris-setosa
plt.plot(cs[51:100], ls[51:100], 'b.')#Iris-versicolor
plt.plot(cs[101:150], ls[101:150], 'g.')#Iris-virginica

#plt.scatter(X[:,0], X[:,1])
plt.show()

plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')

dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
    truncate_mode='lastp',
    p=12,
    show_leaf_counts=False,  # otherwise numbers in brackets are counts
    color_threshold=5,
    show_contracted=True,

)
plt.show()