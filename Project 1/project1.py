#%%
import pandas as pd
import plotly_express as px

#%%
df = pd.read_csv("names_year.csv")

#%%
luke = df.query("name == 'Ruth'")

#%%
fig = px.line(
    luke,
    x = "year",
    y = "Total"
)
#%%
fig.show()

#%%

