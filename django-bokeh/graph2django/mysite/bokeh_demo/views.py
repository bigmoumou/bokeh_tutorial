from django.shortcuts import render

from bokeh.plotting import figure 
from bokeh.embed import components
# Create your views here.


def index(request):
    x = range(10)
    y = [2,3,5,6,2,4,2,6,5,7]
    title = 'demo'

    plot = figure(title=title, plot_width=400, plot_height=400)
    plot.line(x, y, line_width=2)
    script, div = components(plot)

    return render(request,
    			  'bokeh_demo/index.html',
    			  {'script': script, 'div': div})
