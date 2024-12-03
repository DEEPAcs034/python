import json

import pandas as pd
import plotly.express as px
india_states=json.load(open("states_india.geojson","r"))
df=pd.read_csv("india_census - india_census.csv")
state_id_map={}
for feature in india_states["features"]:
    feature["id"]=feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]]=feature["id"]
df=pd.read_csv("india_census - india_census.csv")
df["Density"]=df["Density[a]"].apply(lambda X: int(X.split("/")[0].replace(",","")))
df["id"]=df["State or union territory"].apply(lambda X: state_id_map[X])
print(df.head())
fig=px.choropleth(
df,
locations="id",
geojson=india_states,
color="Population",
hover_name="State or union territory",
hover_data=["Density","Sex ratio","Population"],
title="India Population Statewise",)
#fig.update_geos(fitbounds="locations",visible=False)
fig.show()