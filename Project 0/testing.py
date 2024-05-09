#%%
import pandas as pd
import plotly_express as px

#%%
df = pd.read_csv("covid.csv")

#%%
df.info()
# %%

df["trans"].value_counts()

#%%
df2 = df[["model", "manufacturer", "year"]]
df2.info()
df2.describe()

#%%
jeep = df2.query("manufacturer == 'jeep'")

jeep.describe

#%%

fig
