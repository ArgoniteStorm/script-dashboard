import pandas as pd

tabela = pd.read_excel("funcionarios_vendas.xlsx")

tabela["Vendas (R$)"] = (
    tabela["Vendas (R$)"]
    .astype(str)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)
tabela["Promoção"] = tabela["Vendas (R$)"] >= 30000

print(tabela)