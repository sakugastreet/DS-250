#%%
import pandas as pd
import plotly_express as px

#%%
df = pd.read_csv("mpg.csv")

#%%


#%%
fig = px.scatter(
    df,
    x = "displ",
    y = "hwy",
    
)
#%%
fig.show()

#%%
(df
  .head(5)
  .filter(["manufacturer", "model","year", "hwy"])
)


# %%
