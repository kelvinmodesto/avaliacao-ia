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

#plt.plot(cs[:50], ls[:50], 'r.')#Iris-setosa
#plt.plot(cs[51:100], ls[51:100], 'b.')#Iris-versicolor
#plt.plot(cs[101:150], ls[101:150], 'g.')#Iris-virginica


#ii. cs x cp;
plt.plot(cs, cp, 'bo')

#iii. cs x lp;
plt.plot(cs, lp, 'g^')

#iv. ls x cp;
plt.plot(ls, cp, 'r^')

#v. ls x lp;
plt.plot(ls, lp, 'r*')

#vi. cp x lp.
plt.plot(cp, lp, 'y.')


#plt.savefig('grafico.png')
plt.show()


"""b. Responda:"""
#i. Você percebe algum padrão nos dados?

"""Alguns dados parecem esta agrupados """

#ii. Existe algum grupo que é mais fácil de separar?

"""Alguns grupos possuem uma parte que pode ser reparada mais facilmente, porém a outra parte está misturada com outros grupos"""

#iii. Qual dimensão parece ser mais informativa? (útil para classificação)

"""4 dimensão, uma vez que """

#[<matplotlib.lines.Line2D instance at 0x01878990>]

#show( )
