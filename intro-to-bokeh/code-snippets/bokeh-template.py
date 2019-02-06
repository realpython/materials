"""Bokeh Visualization Template

This template is a general outline for turning your data into a
visualization using Bokeh.
"""
# Data handling
import pandas as pd  # noqa
import numpy as np  # noqa

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource  # noqa
from bokeh.layouts import row, column, gridplot  # noqa
from bokeh.models.widgets import Tabs, Panel  # noqa

# Prepare the data

# Determine where the visualization will be rendered
output_file("filename.html")  # Render to static HTML, or
output_notebook()  # Render inline in a Jupyter Notebook

# Set up the figure(s)
fig = figure()  # Instantiate a figure() object

# Connect to and draw the data

# Organize the layout

# Preview and save
show(fig)  # See what I made, and save if I like it
