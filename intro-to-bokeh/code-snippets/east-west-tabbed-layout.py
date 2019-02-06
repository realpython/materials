# Bokeh Library
from bokeh.io import output_file
from bokeh.models.widgets import Tabs, Panel

# Output to file
output_file(
    "east-west-top-2-tabbed_layout.html",
    title="Conference Top 2 Teams Wins Race",
)

# Increase the plot widths
east_fig.plot_width = west_fig.plot_width = 800  # noqa

# Create two panels, one for each conference
east_panel = Panel(child=east_fig, title="Eastern Conference")  # noqa
west_panel = Panel(child=west_fig, title="Western Conference")  # noqa

# Assign the panels to Tabs
tabs = Tabs(tabs=[west_panel, east_panel])

# Show the tabbed layout
show(tabs)  # noqa
