# Bokeh library
from bokeh.plotting import show
from bokeh.io import output_file
from bokeh.layouts import column

# Output to file
output_file(
    "east-west-top-2-standings-race.html",
    title="Conference Top 2 Teams Wins Race",
)

# Plot the two visualizations in a vertical configuration
show(column(west_fig, east_fig))  # noqa
