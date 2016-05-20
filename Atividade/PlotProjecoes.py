from matplotlib import *
from pylab import *
import matplotlib.pyplot as plt
#(comprimento da sépala – cs,
# largura da sépala – ls,
# comprimento da pétala – cp,
# e largura da pétala – lp, tudo em centímetros)
# o último elemento (texto) diz o tipo da planta (os primeiros 50 são Setosa, os 50 seguintes Versicolor e os 50 últimos Virginica).

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

#comprimento da sépala – cs X largura da sépala – ls#

"""a. Faça um gráfico de cada uma das 6 projeções bi-dimensionais possíveis:"""
#i. cs x ls;
plt.plot(cs, ls, 'ro')

#plt.title('cs x ls')
#plt.show()
#plt.plot(cs[:50], ls[:50], 'r.')#Iris-setosa
#plt.plot(cs[51:100], ls[51:100], 'b.')#Iris-versicolor
#plt.plot(cs[101:150], ls[101:150], 'g.')#Iris-virginica


#ii. cs x cp;
plt.plot(cs, cp, 'bo')
#plt.title('cs x cp')
#plt.show()

#iii. cs x lp;
plt.plot(cs, lp, 'g^')
#plt.title('cs x lp')
#plt.show()


#iv. ls x cp;
plt.plot(ls, cp, 'r^')

#plt.title('ls x cp')
#plt.show()

#v. ls x lp;
plt.plot(ls, lp, 'r*')

#plt.title('ls x lp')
#plt.show()

#vi. cp x lp.
plt.plot(cp, lp, 'y.')

#plt.title('cp x lp')
#plt.show()

#plt.savefig('grafico.png')
plt.title('Todas analises')
plt.show()

