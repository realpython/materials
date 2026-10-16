from nicegui import ui

traffic = [
    {"endpoint": "/login", "requests": 1280},
    {"endpoint": "/api/items", "requests": 2540},
    {"endpoint": "/api/search", "requests": 1875},
    {"endpoint": "/checkout", "requests": 940},
    {"endpoint": "/health", "requests": 4120},
    {"endpoint": "/admin", "requests": 210},
]

ui.echart(
    {
        "title": {"text": "Requests by Endpoint"},
        "xAxis": {
            "type": "category",
            "data": [row["endpoint"] for row in traffic],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"type": "bar", "data": [row["requests"] for row in traffic]}
        ],
    }
).classes("w-full")

ui.table(rows=traffic)

ui.run()
