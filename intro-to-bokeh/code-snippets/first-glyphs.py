# Bokeh Libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show

# My x-y coordinate data
x = [1, 2, 1]
y = [1, 1, 2]

# Output the visualization directly in the notebook
output_file("first_glyphs.html", title="First Glyphs")

# Create a figure with no toolbar and axis ranges of [0,3]
fig = figure(
    title="My Coordinates",
    plot_height=300,
    plot_width=300,
    x_range=(0, 3),
    y_range=(0, 3),
    toolbar_location=None,
)

# Draw the coordinates as circles
fig.circle(x=x, y=y, color="green", size=10, alpha=0.5)

# Show plot
show(fig)
