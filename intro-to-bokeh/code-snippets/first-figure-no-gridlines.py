# Bokeh Libraries
from bokeh.io import output_notebook
from bokeh.plotting import figure, show

# The figure will be rendered inline in my Jupyter Notebook
output_notebook()

# Example figure
fig = figure(
    background_fill_color="gray",
    background_fill_alpha=0.5,
    border_fill_color="blue",
    border_fill_alpha=0.25,
    plot_height=300,
    plot_width=500,
    h_symmetry=True,
    x_axis_label="X Label",
    x_axis_type="datetime",
    x_axis_location="above",
    x_range=("2018-01-01", "2018-06-30"),
    y_axis_label="Y Label",
    y_axis_type="linear",
    y_axis_location="left",
    y_range=(0, 100),
    title="Example Figure",
    title_location="right",
    toolbar_location="below",
    tools="save",
)

# Remove the gridlines from the figure() object
fig.grid.grid_line_color = None

# See what it looks like
show(fig)
