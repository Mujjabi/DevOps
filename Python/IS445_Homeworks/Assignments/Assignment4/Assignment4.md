IS 445 - ACG/ACU: Data Visualization - Fall 2023
===============================================
Assignment 4
-----------------------
Student: Christopher Mujjabi

**Date: October 16, 2023**

## Instructions

## Compare Visualization Engines
Your assignment is to pick four of the following possibilities and write up a set of comparisons for constructing the same visualization.
You must evaluate matplotlib, vega-lite and bqplot, and you can choose one of the following in addition: D3, Bokeh, Plotly, R/RStudio.  Thes-e should total roughly half a page per engine.

1. ## **Matplotlib**
**What is the license for the software?**

Matplotlib license is based on the PSF (Python Software Foundation) license and it only used BSD (Berkeley Software Distribution) compatible code. The BSD License is a permissive open source software, which means that users can freely use, modify and redistribute the software in open-source and proprietary projects with minimal restrictions. 

**What is the focus of the software?**

Matplotlib focuses on creating static, animated and intereactive visualizations in python. Using matplotlib, one can generate publication quality plots, make customized visual styles and layouts, make interactive visualizations that can zoom, pan and update and can be exported in different file formats. 

**Does it have interactivity, and how easy is it?**

matplotlib is mostly used to generate static visualizations, however, since matplotlib can embed JupyterLab, it is possible to use Jupyter extension to adds widget and other functionality that can transform the static plots into a more interactive visualization. 

**What are the pros and cons of using it?**

Some of the pros for using matplotlib include the wide support community given that it is widely used by research scientists and data analytics communities. Therefore there is a lot of information that new users can access to simplify the learning journey. it is also easily accessible given the free-access licence. Matplotlib is also highly customizable which allows users to manipulate and customize charts in different styles. 

The cons of using this software include the steep-learning curve for new or novice users, especially users who are new or never used python before. Users need to learn python to better understand the matplotlib syntax. 

2. ## **Vega-lite**
**What is the license for the software?**

Vega-lite is licenced under the BSD 3-Clause "New" or "Revised" License, which is similar to the BSD 2-Clause License. Howevr, it has a 3rd clause that prohibits users from using the name of the copyright holder or its contributors to promote derived products without written consent. 

**What is the focus of the software?**

Vega-lite is a high-level visualization grammar for generating interactive visualization using JSON syntax. Vega-lite also serves as a declarative format for creating visualization. 

**Does it have interactivity, and how easy is it?**

Vega-lite excels in interactivity by offering a straightforward and concise way to specify interactive features using a JSON-based specification. It supports interactive features such a tooltips that display information when you hover over the data points, zooming to explore specific areas of the plot and panning to navigate large datasets. 

**What are the pros and cons of using it?**

The pros for vegalite is the ability to embed the vega-lite interactive visualization and deploy it in a JSON format on a github pages. I think this makes graphical sharing  and data presentation very easy. Also, vega-lite visualizations can me exported is various ways including PGN, HTML, SVG, PDF and JSON. The other vega-lite componet I personally liked was the vega-lite docs, that explicitly explain all the features that can be used to customize the visualization. 

However, I personally found the snytax very difficult to use since I wasnt familiar with Javascript. 


3. ### **Bqplot**

**What is the license for the software?**

Bqplot is licenced under the Apache License 2.0. This is a permissive license  which allows users to use, modify, distribute and create derivative work using the software without additional permissions. 

**What is the focus of the software?**

The Bqplot library was built on top of javascript and Python library ipywidgets and its mainly used to build fully interactive web applications in python envrionment using fewer line of code. 

**Does it have interactivity, and how easy is it?**

Bqplot specilizes in generating highly interactive web-based visualizations in python though jupyter notebooks using numerous tools such as  IPywidgets. Forexample, we can use bqplot to generate colored maps and add tooltips where we can hover over specific areas/regions on the map and obtain summarized information about that region. 

**What are the pros and cons of using it?**

Some of the pros include the rich set of widgets that can be used for interactivity, and how bqplot requires fewer line of code to generate interactive plots. Also, since it requires less coding, it is more user friendly, particularly to novice users. One of the cons would be the limitation to use bqplot outside of jupyter notebook. 


