import pandas as pd
import plotly.express as px

# Adatok
data = {
    "Év": [2010, 2011, 2012, 2013, 2014, 2015, 2016,
           2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "Teljes adattömeg (zettabájt)": [2, 5, 6.5, 9, 12.5, 15.5, 18, 26,
                                     33, 41, 64.2, 79, 97, 120, 147, 181],
    "Növekedés (zettabájt)": [None, 3, 1.5, 2.5, 3.5, 3, 2.5, 8, 7, 8,
                              23.2, 14.8, 18, 23, 27, 34],
    "Növekedés az előző évhez képest (%)": [None, 150, 30, 38.46, 38.89, 24, 16.13, 44.44,
                      26.92, 24.24, 56.59, 23.05, 22.78, 23.71, 22.5, 23.13]
}

df = pd.DataFrame(data)

# Oszlopdiagram
fig = px.bar(
    df,
    x="Év",
    y="Teljes adattömeg (zettabájt)",
    title="Globális adattömeg növekedése (2010–2025)",
    text="Teljes adattömeg (zettabájt)",
    color="Növekedés az előző évhez képest (%)",
    color_continuous_scale="Viridis"
)

# Szövegek és tengelyek
fig.update_traces(
    texttemplate="%{text}",
    textposition="outside"
)

# Elrendezés – szakdolgozati stílus
fig.update_layout(
    xaxis_title="Év",
    yaxis_title="Adattömeg (zettabájt)",
    coloraxis_colorbar=dict(
        title="Növekedés<br>az előző évhez<br>képest (%)",
        x=1.1,  # távolabb a diagramtól
        xanchor="left"
    ),
    template="simple_white",
    font=dict(family="Arial", size=14, color="black"),
    title=dict(
        font=dict(size=20, family="Arial"),
        x=0.5,
        xanchor="center",
        yanchor="top",
        pad=dict(t=50)
    ),
    width=900,
    height=600,
    margin=dict(t=90, l=80, r=100, b=60)
)

# Csak az Y-tengely becsíkozva
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=True, gridcolor="lightgrey", gridwidth=0.5)

# Mentés magas felbontásban
fig.write_image("Globalis_adattomeg.png", scale=3)
print("Mentve: Globalis_adattomeg.png")

# Megjelenítés (opcionális)
fig.show()
