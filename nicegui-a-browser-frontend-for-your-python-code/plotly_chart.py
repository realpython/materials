import pandas as pd
import plotly.express as px
from nicegui import ui

traffic = pd.DataFrame(
    {
        "Endpoint": [
            "/login",
            "/api/items",
            "/api/search",
            "/checkout",
            "/health",
            "/admin",
        ],
        "Requests": [1280, 2540, 1875, 940, 4120, 210],
    }
)
fig = px.bar(
    traffic,
    x="Endpoint",
    y="Requests",
    title="Requests by Endpoint",
)
ui.plotly(fig).classes("w-full")

ui.run()
