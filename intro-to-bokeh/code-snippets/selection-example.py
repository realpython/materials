# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter

# Output to file
output_file(
    "three-point-att-vs-pct.html", title="Three-Point Attempts vs. Percentage"
)

# Store the data in a ColumnDataSource
three_takers_cds = ColumnDataSource(three_takers)  # noqa

# Specify the selection tools to be made available
select_tools = ["box_select", "lasso_select", "poly_select", "tap", "reset"]

# Create the figure
fig = figure(
    plot_height=400,
    plot_width=600,
    x_axis_label="Three-Point Shots Attempted",
    y_axis_label="Percentage Made",
    title="3PT Shots Attempted vs. Percentage Made (min. 100 3PA), 2017-18",
    toolbar_location="below",
    tools=select_tools,
)

# Format the y-axis tick labels as percentages
fig.yaxis[0].formatter = NumeralTickFormatter(format="00.0%")

# Add square representing each player
fig.square(
    x="play3PA",
    y="pct3PM",
    source=three_takers_cds,
    color="royalblue",
    selection_color="deepskyblue",
    nonselection_color="lightgray",
    nonselection_alpha=0.3,
)

# Visualize
show(fig)
