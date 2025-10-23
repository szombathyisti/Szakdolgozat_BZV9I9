import plotly.express as px

df = px.data.iris()

fig = px.pie(
    df,
    names="species",
    title="Iris fajok eloszlása",
    hole=0.0,
    color_discrete_sequence=["#679EE6", "#4D76C1", "#1E3A8A"]
)


fig.update_traces(
    textinfo="percent+label",
    hoverinfo="none",
    marker=dict(line=dict(color="#FFFFFF", width=0.0))
)

fig.update_layout(
    template="simple_white",
    showlegend=False,  
    font=dict(family="Arial", size=14, color="black"),
    title=dict(
        text="Iris fajok eloszlása<br><sup>Ronald Fisher adathalmaza alapján</sup>",
        font=dict(size=20, family="Arial", color="black"),
        x=0.5,  
        xanchor="center",
        yanchor="top",
        pad=dict(t=50)  
    ),
    width=800,
    height=600,
    margin=dict(t=100, l=60, r=30, b=60)  
)


fig.write_image("Piechart.png", scale=3)
print("Mentve: Piechart.png")
