
import matplotlib.pyplot as plt
import numpy as np

#grafico de dispersão
idades = [10,20,30,40,50,60,70,80]

ids = [ x for x in range (len(idades))]
print(ids)

x = [1,2,3,4,5,6,7,8]
y = [5,2,4,5,6,8,4,8]

plt.scatter (x,y, label = "comparação", color = "black", marker = "+")
plt.legend()
plt.show()

#grafico de área empilhado
dias = [1,2,3,4,5]
dormir = [7,8,6,77,7]
comer = [2,3,4,5,3]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,13]

plt.stackplot ( dias, dormir,comer,trabalhar,passear , colors = ["m", "c", "r", "k", "b"])
plt.show()

#grafico de pizza I
fatias = [7,2,2,13]
atividade = ["estudar", "treinar", "fazer", "conquistar"]
cor = ["olive", "lime", "violet", "royalblue"]

plt.pie(fatias, labels =  atividade, colors  = cor, startangle = 90, shadow = True, explode = (0,0.2,0,0))
plt.show()

#grafico de pizza II
fatias_1 = [2,3,5,8]
atividade_1 = ["Comer", "trabalhar", "sonhar", "repetir"]
cores = ["olive", "lime", "violet", "royalblue"]

plt.pie(fatias_1, labels = atividade_1, colors = cores , startangle = 90, shadow = True, explode = (0,0.1,0,0))
plt.show()

#grafico de pizza III
fatias_2 = [1,3,5,8]
atividade_2 = ["teste1", "teste2", "teste3","teste4"]
cores_2 = ["violet", "blue", "orange", "lime" ]

plt.pie(fatias_2, labels = atividade_2, colors = cores_2, shadow = True, startangle= 70, explode = (0,0.3,0,0))
plt.show()

from pylab import *

#grafico de representação visual
x = linspace(0,5,10)
y =  x ** 2

#labels e título
fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # margens aumentadas
axes.plot(x, y, 'r')
axes.set_xlabel("Eixo X")
axes.set_ylabel("Eixo Y")
axes.set_title("Figura Principal")
axes = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # margens aumentadas
axes.plot(y, x, 'k')
axes.set_xlabel("Eixo y")
axes.set_ylabel("Eixo x")
axes.set_title("Figura secundária")
plt.show()

x = linspace(0,5,10)
y = x ** 2

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x,y, "r")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Título")

fig.tight_layout()
plt.show()

x = np.linspace(0,4,5)
print(x)

###



























