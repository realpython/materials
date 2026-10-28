# Bokeh Library
from bokeh.io import output_file
from bokeh.models import TabPanel, Tabs

# Output to file
output_file(
    "east-west-top-2-tabbed_layout.html",
    title="Conference Top 2 Teams Wins Race",
)

# Increase the plot widths
east_fig.width = west_fig.width = 800  # noqa

# Create two panels, one for each conference
east_panel = TabPanel(child=east_fig, title="Eastern Conference")  # noqa
west_panel = TabPanel(child=west_fig, title="Western Conference")  # noqa

# Assign the panels to Tabs
tabs = Tabs(tabs=[west_panel, east_panel])

# Show the tabbed layout
show(tabs)  # noqa
