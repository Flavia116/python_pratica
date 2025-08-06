# ================================================
# Aula de Visualização de Dados com Seaborn e Matplotlib
# ================================================

# Importação das bibliotecas
import seaborn as sns
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# -----------------------------------------------
# Parte 1: Visualização com dataset "tips" do Seaborn
# -----------------------------------------------

dados = sns.load_dataset("tips")
print(dados.head())

# Regressão linear entre total da conta e gorjeta
sns.jointplot(data=dados, x="total_bill", y="tip", kind="reg")
plt.show()

# Regressão linear separada por fumantes e não fumantes
sns.lmplot(data=dados, x="total_bill", y="tip", col="smoker")
plt.show()

# -----------------------------------------------
# Parte 2: Criação de DataFrame com dados aleatórios
# -----------------------------------------------

df = pd.DataFrame()
df["idade"] = random.sample(range(20, 100), 30)
df["peso"] = random.sample(range(55, 150), 30)

print(df.shape)
print(df.head())

# Regressão linear entre idade e peso
sns.lmplot(data=df, x="idade", y="peso", fit_reg=True)

# Distribuição com KDE (Kernel Density Estimation)
sns.kdeplot(df.idade, label="Idade")
sns.kdeplot(df.peso, label="Peso")
plt.legend()
plt.show()

# Histograma bidimensional com displot
sns.displot(data=df, x="idade", y="peso")
plt.show()

# Histograma simples de peso
sns.displot(df.peso)
plt.show()

# Histograma + rugplot
plt.hist(df.idade, alpha=0.3)
sns.rugplot(df.idade)
plt.show()

# Boxenplot
sns.boxenplot(x=df.idade, color="m")
plt.show()

sns.boxenplot(x=df.peso, color="b")
plt.show()

# Violinplot
sns.violinplot(x=df.peso, color="y")
plt.show()

sns.violinplot(x=df.idade, color="k")
plt.show()

# -----------------------------------------------
# Parte 3: Dataset simulado com flag de fumante
# -----------------------------------------------

np.random.seed(42)
n = 1000
pct_smokers = 0.2

flag_fumante = np.random.rand(n) < pct_smokers
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

dados = pd.DataFrame({
    "altura": altura,
    "peso": peso,
    "flag_fumante": flag_fumante
})

dados["flag_fumante"] = dados["flag_fumante"].map({True: "Fumante", False: "Não fumante"})

print(dados.head())

# Gráfico de dispersão com regressão, separado por fumantes
sns.set(style="ticks")

sns.lmplot(
    x="altura",
    y="peso",
    data=dados,
    hue="flag_fumante",
    palette=["tab:blue", "tab:orange"],
    height=7
)

plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")
plt.title("Relação Entre Altura e Peso: Fumantes x Não Fumantes")
sns.despine()
plt.show()

# -----------------------------------------------
# Observação
# -----------------------------------------------
# Matplotlib é para gráficos genéricos.
# Seaborn é construído sobre o matplotlib e traz gráficos estatísticos com mais facilidade.# ================================================
# # Aula de Visualização de Dados com Seaborn e Matplotlib
# # ================================================
#
