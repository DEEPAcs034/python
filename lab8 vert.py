from bokeh.plotting import figure,output_file,show


fig=figure(min_width=800,min_height=200)
fig.vbar(x=[2,4,6],width=1,bottom=0,top=[10,8,4],color='Cyan')
output_file('vbar.html')
show(fig)