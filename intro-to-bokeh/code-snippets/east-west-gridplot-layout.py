# Bokeh libraries
from bokeh.io import output_file
from bokeh.layouts import gridplot

# Output to file
output_file(
    "east-west-top-2-gridplot.html", title="Conference Top 2 Teams Wins Race"
)

# Reduce the width of both figures
east_fig.plot_width = west_fig.plot_width = 300  # noqa

# Edit the titles
east_fig.title.text = "Eastern Conference"  # noqa
west_fig.title.text = "Western Conference"  # noqa

# Configure the gridplot
east_west_gridplot = gridplot(
    [[west_fig, east_fig]],  # noqa: F821
    toolbar_location="right",
)

# Plot the two visualizations in a horizontal configuration
show(east_west_gridplot)  # noqa
