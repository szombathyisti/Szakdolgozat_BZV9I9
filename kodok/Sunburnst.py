import plotly.express as px


df = px.data.iris()

# Sunburst diagram – hierarchia: faj -> petal_width kategória
fig = px.sunburst(
    df,
    path=["species", "petal_width"],  
    title="Iris adathalmaz hierarchikus eloszlása ",
    color="species",
    color_discrete_sequence=["#B0C4DE", "#6495ED", "#1E3A8A"]
)


fig.update_layout(
    template="simple_white",
    font=dict(family="Arial", size=14, color="black"),
    title_font=dict(size=20, family="Arial", color="black"),
    width=800,
    height=600,
    margin=dict(t=60, l=60, r=30, b=60)
)

fig.show()  # A kódot lefuttatva az alapértelmezett böngészőben megkapjuk az interaktív diagrammot
fig.write_image("Sunburst.png", scale=3)
