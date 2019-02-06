# Bokeh libraries
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, CDSView, GroupFilter

# Create a ColumnDataSource
standings_cds = ColumnDataSource(standings)  # noqa

# Create the views for each team
celtics_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name="teamAbbr", group="BOS")],
)

raptors_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name="teamAbbr", group="TOR")],
)

rockets_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name="teamAbbr", group="HOU")],
)
warriors_view = CDSView(
    source=standings_cds,
    filters=[GroupFilter(column_name="teamAbbr", group="GS")],
)

# Create and configure the figure
east_fig = figure(
    x_axis_type="datetime",
    plot_height=300,
    x_axis_label="Date",
    y_axis_label="Wins",
    toolbar_location=None,
)

west_fig = figure(
    x_axis_type="datetime",
    plot_height=300,
    x_axis_label="Date",
    y_axis_label="Wins",
    toolbar_location=None,
)

# Configure the figures for each conference
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

west_fig.step(
    "stDate",
    "gameWon",
    color="#CE1141",
    legend="Rockets",
    source=standings_cds,
    view=rockets_view,
)
west_fig.step(
    "stDate",
    "gameWon",
    color="#006BB6",
    legend="Warriors",
    source=standings_cds,
    view=warriors_view,
)

# Move the legend to the upper left corner
east_fig.legend.location = "top_left"
west_fig.legend.location = "top_left"
