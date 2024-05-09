#%%
import pandas as pd
import plotly_express as px

#%%
df = pd.read_csv("names_year.csv")
df
#%%
luke = df.query("name == 'Felisha'")

# luke = luke["UT"]

print(luke["UT"].sum())
luke

#%%
fig = px.line(
    luke,
    x = "year",
    y = "Total"
)
#%%
fig.show()

#%%

