import matplotlib.pyplot as plt
import numpy as np

# Gráfico 1: Seno de x no intervalo de 2 a 3
x = np.arange(2, 3, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.title("Gráfico de Seno")
plt.xlabel("Variável 1")
plt.ylabel("Variável 2")
plt.show()

# Gráfico 1: Log de x no intervalo de 2 a 4
x3 = np.arange(2,7,4)
y3 = np.log(x3)
plt.plot(y3,  label = "Grafico log", color = "yellow")
plt.xlabel("Variável 1")
plt.ylabel("Variável 2")
plt.legend()
plt.show()

# Gráfico 2: Linha simples com legenda
x2 = [1, 2, 3]
y2 = [11, 12, 15]
plt.plot(x2, y2, label="Teste de sobrevivência", color="red")
plt.legend()
plt.title("Gráfico Linha Simples")
plt.xlabel("Variável 1")
plt.ylabel("Variável 2")
plt.show()

# Gráfico 3: Barras azuis
x1 = [2, 4, 6, 8, 10]
y1 = [6, 7, 8, 2, 4]
plt.bar(x1, y1, label="Barras", color="blue")
plt.legend()
plt.title("Gráfico de Barras Azuis")
plt.xlabel("Variável 1")
plt.ylabel("Variável 2")
plt.show()

# Gráfico 4: Barras laranja com dados invertidos
var_1 = [10, 9, 8, 7, 6, 4]
var_2 = [4, 6, 7, 8, 9, 10]
plt.bar(var_1, var_2, label="Grafico barra", color="black")
plt.legend()
plt.title("Gráfico de Barras ")
plt.xlabel("Variável 1")
plt.ylabel("Variável 2")
plt.show()






























