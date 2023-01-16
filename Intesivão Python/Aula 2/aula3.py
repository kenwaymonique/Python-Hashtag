#Passo 1: Importar a base de dados
import pandas as pd
tabela = pd.read_csv("telecom_users.csv")

#Passo 2: Visualizar a base de dados
print(tabela)
tabela = tabela.drop("Unnamed: 0", axis=1)
#axis = 0 (linha); axis = 1 (coluna)

#Passo 3: Tratamento de dados
#Resolver valores que estão sendo reconhecidos de forma errada
#TotalGasto deveria ser número e é reconhecida como texto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
print(tabela.info())
#Resolver valores vazios
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

#Passo 4: Análise Inicial
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True))

#Passo 5: Análise e conclusão do problema
import plotly.express as px
grafico = px.histogram(tabela, x="TipoContrato", color="Churn", text_auto=True)

grafico.show()