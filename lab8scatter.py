from bokeh.plotting import figure,output_file,show
p=figure(min_width=400,min_height=400)
p.scatter([1,4,3,2,5],[6,5,2,4,7],marker='circle',size=20,fill_color='Green')
output_file('scatter.html')
show(p)
