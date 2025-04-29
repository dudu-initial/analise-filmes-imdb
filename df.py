
# %%
# 1. Importando Dados

import pandas as pd
import matplotlib.pyplot as plt

# %%

# 2. Carregamento dos Dados
df = pd.read_csv("imdb_top_1000.csv", sep=",")

df.head()
# %%

# 3. Exploração inicial dos Dados

df.head()
df.info()
df.describe()


# %%

# 4. Tratamento dos Dados
df["Released_Year"] = df["Released_Year"].replace("PG", " ")


# %%

# 5. Convertendo para datetime (após filtrar inválidos)

df["Released_Year"] = pd.to_datetime(df["Released_Year"], format="%Y", errors="coerce")
# 5.1 Extraindo apenas o ano
df["Released_Year"] = df["Released_Year"].dt.year

# 5.2 Converter para inteiro (permitindo NaN)

df["Released_Year"] = df["Released_Year"].astype("Int64")

# %%

# 6. Análises

# 6.1 Quais os gêneros mais bem avaliados?
df_genero = df.groupby("Genre", as_index=False).agg({
    "Series_Title": "count",
    "IMDB_Rating": ["sum", "mean"]
})

# %%
df_genero = df_genero.reset_index(drop=True)

# %%
df_genero.head()
