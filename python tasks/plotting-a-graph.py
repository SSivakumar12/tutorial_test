import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
 

df = pd.read_csv("asylum_decisions_2001_2021.csv")
df = df.rename(columns={'Unnamed: 0': 'unnamed_0', 'Year': 'year', 'Quarter': 'quarter', 'Nationality': 'nationality', 'Region': 'region', 'Case type': 'case_type', 'Case outcome group': 'case_outcome_group', 'Case outcome': 'case_outcome', 'Age ': 'age', 'Sex': 'sex', 'Applicant type': 'applicant_type', 'UASC': 'uasc', 'Host Country': 'host_country', 'Decisions': 'decisions'})

df_4 = df[df["region"] == "Asia South"]

df_5 = df_4.groupby("nationality")[["case_outcome_group", "case_outcome"]].count()
df_5.reset_index(level = 0, inplace = True)
df_5



df_6 = df[df["region"] == "Africa North"]
df_7 = df_6.groupby("nationality")[["case_outcome_group", "case_outcome"]].count()
df_7.reset_index(level = 0, inplace = True)
df_7


fig = make_subplots(rows = 2, cols = 1)
fig.add_trace(go.Bar(x = df_5["nationality"], y = df_5["case_outcome_group"]), row = 1, col = 1)
fig.add_trace(go.Bar(x = df_7["nationality"], y = df_7["case_outcome_group"]), row = 2, col = 1)
fig.update_layout({"title": {"text": "bar charts comparing different regions", "x": 0.5, "y": 0.9}})
fig.show()







