import plotly.express as px

df = px.data.iris()

fig = px.pie(
    df,
    names="species",
    hole=0.0,
    color_discrete_sequence=["#679EE6", "#4D76C1", "#1E3A8A"]
)

fig.update_traces(
    textinfo="percent+label",
    hoverinfo="none",
    textfont=dict(size=24, family="Arial", color="black"),  
    marker=dict(line=dict(color="#FFFFFF", width=0.0))
)

fig.update_layout(
    template="simple_white",
    showlegend=False,
    font=dict(family="Arial", size=16, color="black"),
    width=800,
    height=600,
    margin=dict(t=10, l=10, r=10, b=10) 
)

fig.write_image("Piechart.png", scale=3)
print("Mentve: Piechart.png")
