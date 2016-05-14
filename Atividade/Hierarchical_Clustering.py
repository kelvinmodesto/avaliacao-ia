import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import  dendrogram, linkage
from numpy import array
import numpy as np

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

def criarDados_cs_X_ls():

    plt.figure(1)
    plt.title('CS X LS')
    plt.scatter(cs, ls)

    d = []
    for i in range(len(cs) - 1):
        for j in range(i+1, len(cs) - 1):
            d.append(np.sqrt(((cs[i]-cs[j])**2 + (ls[i]-ls[j])**2)))
    return d

mat = criarDados_cs_X_ls()


plt.figure(102)
plt.title("Three Clusters")

linkage_matrix = linkage(mat, 'single')
print ("three clusters")
print (linkage_matrix)

dendrogram(linkage_matrix,
           truncate_mode='lastp',
           color_threshold=1,
           show_leaf_counts=True)

plt.show()