import sklearn
from numpy.ma.extras import column_stack
#from numpy.ma.extras import column_stack
from sklearn.tree import plot_tree

sklearn.__version__

print(sklearn.__version__)

#vamos começar importando o dataset iris do skicit-learn
from sklearn.datasets import load_iris
data = load_iris()

import pandas as pd
df = pd.DataFrame(data["data"], columns = data["feature_names"])
df["species"] = data["target"]
print(df.head(2))

import matplotlib.pyplot as plt

# Gráfico de dispersão entre sepal length e petal width
df.plot.scatter(x="sepal length (cm)", y="petal width (cm)")
plt.title("Dispersão: Comprimento da Sépala vs Largura da Pétala")
plt.grid(True)
plt.show()

print(df)

columns = ["sepal length (cm)", "sepal width (cm)", "petal width (cm)"]
df[columns].plot.area()

plt.title("Gráfico de Área das Medidas da Íris")
plt.xlabel("Índice")
plt.ylabel("Medidas")
plt.grid(True)
plt.show()

df.groupby("species").mean().plot.bar()
plt.show()

df.groupby("species").count().plot.pie (y = "sepal length (cm)")
plt.show()

df.groupby("species").plot.hist (y = "sepal length (cm)")
plt.show()