from bokeh.plotting import figure,output_file,show
from math import pi
p=figure(min_width=400,min_height=400)
p.rect(x=[1,2,3],y=[1,2,3],width=0.2,height=40,color='Green',angle=pi/3,height_units='screen')
output_file('Rectangle.html')
show(p)