import plotly.express as px
import random

df = px.data.iris()

# Véletlenszerű, sokszínű színsorozat létrehozása
random_colors = [
    f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})"
    for _ in range(len(df))
]

# Sunburst diagram – hierarchia: faj -> petal_width kategória
fig = px.sunburst(
    df,
    path=["species", "petal_width"],
    color="petal_width",
    color_continuous_scale=random_colors
)

fig.update_layout(
    template="simple_white",
    font=dict(family="Arial", size=26, color="black"),  
    title=dict(
        text="Iris adathalmaz hierarchikus eloszlása ",
        font=dict(size=50, family="Arial", color="black"),
        x=0.5,
        xanchor='center'
    ),
    width=1400,
    height=1000,
    margin=dict(t=100, l=20, r=20, b=20)  
)

fig.show()
fig.write_image("Sunburst_sokszin_nagy.png", scale=6)
