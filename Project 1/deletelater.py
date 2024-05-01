#%%
import pandas as pd
import plotly_express as px

 #%%

df = pd.read_csv("names_year.csv")

#%%

df
# %%

fig = px.line(
    df,
    x="year",
    y="Total"
)
fig.show()
# %%
