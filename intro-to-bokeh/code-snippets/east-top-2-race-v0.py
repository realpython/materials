# Bokeh libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Output to file
output_file(
    "east-top-2-standings-race.html",
    title="Eastern Conference Top 2 Teams Wins Race",
)

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)  # noqa

# Create views for each team
celtics_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name="teamAbbr", group="BOS")],
)
raptors_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name="teamAbbr", group="TOR")],
)

# Create and configure the figure
east_fig = figure(
    x_axis_type="datetime",
    plot_height=300,
    plot_width=600,
    title="Eastern Conference Top 2 Teams Wins Race, 2017-18",
    x_axis_label="Date",
    y_axis_label="Wins",
    toolbar_location=None,
)

# Render the race as step lines
east_fig.step(
    "stDate",
    "gameWon",
    color="#007A33",
    legend="Celtics",
    source=standings_cds,
    view=celtics_view,
)
east_fig.step(
    "stDate",
    "gameWon",
    color="#CE1141",
    legend="Raptors",
    source=standings_cds,
    view=raptors_view,
)

# Move the legend to the upper left corner
east_fig.legend.location = "top_left"

# Show the plot
show(east_fig)
