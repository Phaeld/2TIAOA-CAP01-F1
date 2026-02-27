import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

csv = 'heart_disease.csv'
df = pd.read_csv(csv)

# Análise exploratória básica
print("Linhas, Colunas: ", df.shape)
print('Colunas: ', list(df.columns))
print(df.info())

# Verifica se o dataset possui linhas com algum valor nulo
print(df.isnull().any(axis=1).sum())
print((df == '?').sum())

# Verifica se alguma linha possui valor zero para colesterol e frequência cardiaca, pressão arterial ou idade (possivel omissão de valores)
print(df.min())


'''
    Verificado que o dataset está limpo vamos definir as variáveis alvo
    Este processo é importante pois irá verificar o grau de balanceamento do 
    dataset. Por exemplo se tem um número muito grande de saudaveis comparado com doentes e vice versa.
'''

#Tem doença ou não
target_binary = df['target_binary'].value_counts()

# Gravidade da doença
num = df['num'].value_counts()

print(f"Doenças: {target_binary} \n Gravidade: {num}\n")
print(df["target_binary"].value_counts(normalize=True) * 100)
print(df["num"].value_counts(normalize=True) * 100)

'''
    O resultado mostra balanceamento entre doentes e saudáveis e coerência nos valores, pois a soma de 
    num (gravidade da doença) é proporcional a target_binary com valor 1 (doente).
    No entanto é importante observar que há um desbalanceamento nas gravidades das doenças, o que pode enviesar o modelo.
    Por exemplo, um modelo de previsão iria tender para classe de gravidade 2, dado a quantidade de gravidades 
    nesta classe.
    
    Doenças: target_binary
    0    554
    1    470
    Name: count, dtype: int64 
    
    Gravidade: num
    0    554
    2    367
    1     55
    3     35
    4     13
    Name: count, dtype: int64
    
    target_binary
    0    54.101562
    1    45.898438
    Name: proportion, dtype: float64
    num
    0    54.101562
    2    35.839844
    1     5.371094
    3     3.417969
    4     1.269531
    Name: proportion, dtype: float64
'''

# Distribuição target_binary
plt.figure()
df["target_binary"].value_counts().plot(kind="bar")
plt.title("Distribuição - Doença Cardíaca (Binário)")
plt.xlabel("Classe")
plt.ylabel("Quantidade")
plt.savefig("grafico_target.png")
plt.close()

# Distribuição de gravidade
plt.figure()
df["num"].value_counts().sort_index().plot(kind="bar")
plt.title("Distribuição - Gravidade da Doença")
plt.xlabel("Classe de Gravidade")
plt.ylabel("Quantidade")
plt.savefig("grafico_gravidade.png")
plt.close()

# Distribuição de idade
plt.figure()
df["age"].plot(kind="hist", bins=20)
plt.title("Distribuição de Idade dos Pacientes")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.savefig("grafico_idade.png")
plt.close()