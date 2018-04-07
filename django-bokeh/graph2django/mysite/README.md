# How to embed bokeh plot in Django: Quick Start
This short tutorial is meant for people who want to embed Bokeh plot in Django.     
It does not include comparison with others tools.

## It's just two steps :
- Step1. 畫出 bokeh 的圖 (figure)
- Step2. Decompose 成 script 和 div 後傳到前端 (透過 jinja)
- Done !

## Quick Start Example:
### Step1. Bokeh figure:    
A simple lineplot example in bokeh tutorial.

```python
from bokeh.plotting import figure

x = range(10)
y = [2,3,5,6,2,4,2,6,5,7]
title = 'demo'

plot = figure(title=title, plot_width=400, plot_height=400)
plot.line(x, y, line_width=2)
show(plot)
```    

Which may look like:    

![](./github_imgs/example_lineplot01.png)


### Step2-1. Decompose to script and div:
Decompose the bokeh figure by just two lines.
```python
from bokeh.embed import components

script, div = components(plot)
```

### Step2-1. Sent it to the frontend:
The full example looks like this (file: views.py).
```python
from django.shortcuts import render
from bokeh.plotting import figure 
from bokeh.embed import components

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
```
