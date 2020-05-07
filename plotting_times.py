from motion_detector import df
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import HoverTool, ColumnDataSource
import pandas


df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type = 'datetime', height = 200, width = 1000, title = 'Motion Graph')
p.yaxis.minor_tick_line_color = None

hover = HoverTool(tooltips = [("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)
q = p.quad(left = "Start", right = "End", top=1, bottom=0, color = "green",source = cds)

output_file('Graph.html')
show(p)

