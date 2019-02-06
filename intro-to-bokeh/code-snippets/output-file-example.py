# Bokeh Libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show

# The figure will be rendered in a static HTML file
# called output_file_test.html
output_file("output_file_test.html", title="Empty Bokeh Figure")

# Set up a generic figure() object
fig = figure()

# See what it looks like
show(fig)
