#basically this piece of code generates a graph of the timeline of object

from Motiondetector import df
from bokeh.plotting import output_file,show,figure
from bokeh.models import HoverTool,ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")#the format in which we want to display the time on the graph
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds=ColumnDataSource(df)

p=figure(x_axis_type="datetime",width=500,height=100,sizing_mode="scale_both",title="Motion Graph")

p.yaxis.minor_tick_line_color=None #to remove tick lines
p.yaxis[0].ticker.desired_num_ticks=1  #for removing grids in thr grsph

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])#it gives the details about that particulat timeline when v move the cursor on it
p.add_tools(hover)

q=p.quad(left="Start",right="End",top=1,bottom=0,color="green",source=cds)

output_file("Motiograph.html")

show(p)
