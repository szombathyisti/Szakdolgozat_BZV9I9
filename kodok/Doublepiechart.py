import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go


feladat_színek = ["#012D58", "#0056ad", "#2fccf4", "#4f5df6", "#89b5f8"]
backend_frontend_színek = ["#003366", "#3385ff"]


data = {
    "Feladat": [
        "Elfelejtett jelszó funkció",
        '"A" widget',
        '"B" widget',
        '"C" widget',
        "Új térkép nézet"
    ],
    "Backend": [8, 5, 5, 4, 2],
    "Frontend": [2, 5, 6, 15, 8]
}
df = pd.DataFrame(data)
df["Összes"] = df["Backend"] + df["Frontend"]


összes_backend = df["Backend"].sum()
összes_frontend = df["Frontend"].sum()
df2 = pd.DataFrame({
    "Típus": ["Backend", "Frontend"],
    "Összesített órák": [összes_backend, összes_frontend]
})


fig = make_subplots(
    rows=1, cols=2,
    specs=[[{'type':'domain'}, {'type':'domain'}]],
    subplot_titles=[
        "Feladatok összes erőforrásigénye",
        "Backend vs Frontend arány"
    ]
)


fig.add_trace(
    go.Pie(
        labels=df["Feladat"],
        values=df["Összes"],
        textinfo='percent+label',
        textfont_size=22,
        insidetextorientation='horizontal',
        marker=dict(colors=feladat_színek),
        showlegend=False
    ),
    row=1, col=1
)


fig.add_trace(
    go.Pie(
        labels=df2["Típus"],
        values=df2["Összesített órák"],
        textinfo='percent+label',
        textfont_size=22,
        insidetextorientation='horizontal',
        marker=dict(colors=backend_frontend_színek),
        showlegend=False
    ),
    row=1, col=2
)


fig.update_layout(
    title_text="Projekt erőforrás-megoszlás",
    title_x=0.5,
    title_font_size=40,
    margin=dict(l=20, r=20, t=150, b=20),
    annotations=[dict(font_size=34)]  
)


fig.write_image("diagramok_egyben.png", width=1600, height=900, scale=1.5)


