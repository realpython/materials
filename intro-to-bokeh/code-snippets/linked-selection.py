# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import (
    ColumnDataSource,
    CategoricalColorMapper,
    NumeralTickFormatter,
)
from bokeh.layouts import gridplot

# Output inline in the notebook
output_file(
    "phi-gm-linked-selections.html", title="76ers Percentages vs. Win-Loss"
)

# Store the data in a ColumnDataSource
gm_stats_cds = ColumnDataSource(phi_gm_stats_2)  # noqa

# Create a CategoricalColorMapper that assigns specific
# colors to wins and losses
win_loss_mapper = CategoricalColorMapper(
    factors=["W", "L"], palette=["Green", "Red"]
)

# Specify the tools
toolList = ["lasso_select", "tap", "reset", "save"]

# Create a figure relating the percentages
pctFig = figure(
    title="2PT FG % vs 3PT FG %, 2017-18 Regular Season",
    plot_height=400,
    plot_width=400,
    tools=toolList,
    x_axis_label="2PT FG%",
    y_axis_label="3PT FG%",
)

# Draw with circle markers
pctFig.circle(
    x="team2P%", y="team3P%", source=gm_stats_cds, size=12, color="black"
)

# Format the y-axis tick labels as percenages
pctFig.xaxis[0].formatter = NumeralTickFormatter(format="00.0%")
pctFig.yaxis[0].formatter = NumeralTickFormatter(format="00.0%")

# Create a figure relating the totals
totFig = figure(
    title="Team Points vs Opponent Points, 2017-18 Regular Season",
    plot_height=400,
    plot_width=400,
    tools=toolList,
    x_axis_label="Team Points",
    y_axis_label="Opponent Points",
)

# Draw with square markers
totFig.square(
    x="teamPTS",
    y="opptPTS",
    source=gm_stats_cds,
    size=10,
    color=dict(field="winLoss", transform=win_loss_mapper),
)

# Create layout
grid = gridplot([[pctFig, totFig]])

# Visualize
show(grid)
