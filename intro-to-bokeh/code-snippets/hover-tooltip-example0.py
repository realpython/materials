# Bokeh Library
from bokeh.models import HoverTool

# Format the tooltip
tooltips = [
    ("Player", "@name"),
    ("Three-Pointers Made", "@play3PM"),
    ("Three-Pointers Attempted", "@play3PA"),
    ("Three-Point Percentage", "@pct3PM{00.0%}"),
]

# Add the HoverTool to the figure
fig.add_tools(HoverTool(tooltips=tooltips))  # noqa

# Visualize
show(fig)  # noqa
