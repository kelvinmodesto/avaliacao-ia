from numpy import array
import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import  dendrogram, linkage


matrix = []
matrix.append(5)
matrix.append(51)

#plt.show()

def make_fake_data():
    amp = 1000.
    x = []
    y = []

    file = open('iris.txt', 'r')
    cs = []
    ls = []

    for line in file:
        # print(line+' ' + line.split(',',)[0])
        cs.append(float(line.split(',')[0]))
        ls.append(float(line.split(',')[1]))
    print(cs)

    for i in range(0, 1550):
        s = 20
        x.append(np.random.normal(30))
        y.append(np.random.normal(30))
    print(x)
    for i in range(0, 150):
        s = 2
        x.append(np.random.normal(150))
        y.append(np.random.normal(150))
    for i in range(0, 150):
        s = 5
        x.append(np.random.normal(-20))
        y.append(np.random.normal(50))

    x.append(cs)
    x.append(ls)


    plt.figure(1)
    plt.title('fake data')
#   plt.plot(x,y, 'r*')
    plt.show()

    d = []
    for i in range(len(cs) - 1):
       # for j in range(i+1, len(x) - 1):
        d.append(np.fabs(cs[i] + ls[i]))

    print(len(d))

    return d

matr = make_fake_data()
print (matr)
matr.sort()
print(matr)

dendrogram(matr,
           color_threshold=1,
           truncate_mode='lastp',
           labels=array(['a', 'b', 'c', 'd', 'e', 'f']),
           distance_sort='descending')

plt.plot(matr, 'b.')

plt.show()
