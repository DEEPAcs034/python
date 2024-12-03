from bokeh.plotting import figure,output_file,show

fig=figure(min_width=800,min_height=200)
fig.hbar(y=[2,4,6],height=1,left=0,right=[1,2,3],color='Cyan')
output_file('bar.html')
show(fig)