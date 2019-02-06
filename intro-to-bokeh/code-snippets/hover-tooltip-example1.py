# Format the tooltip
tooltips = [
    ("Player", "@name"),
    ("Three-Pointers Made", "@play3PM"),
    ("Three-Pointers Attempted", "@play3PA"),
    ("Three-Point Percentage", "@pct3PM{00.0%}"),
]

# Configure a renderer to be used upon hover
hover_glyph = fig.circle(  # noqa
    x="play3PA",
    y="pct3PM",
    source=three_takers_cds,  # noqa
    size=15,
    alpha=0,
    hover_fill_color="black",
    hover_alpha=0.5,
)

# Add the HoverTool to the figure
fig.add_tools(HoverTool(tooltips=tooltips, renderers=[hover_glyph]))  # noqa

# Visualize
show(fig)  # noqa
