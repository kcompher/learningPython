# Databricks notebook source exported at Thu, 27 Aug 2015 17:03:31 UTC
# MAGIC %md #Table of Contents
# MAGIC * [Learning Objectives:](#Learning-Objectives:)
# MAGIC 	* [Some comments on pedagogical style](#Some-comments-on-pedagogical-style)
# MAGIC * [`matplotlib` — 2D and 3D plotting in Python](#matplotlib-—-2D-and-3D-plotting-in-Python)
# MAGIC 	* [Introduction](#Introduction)
# MAGIC 	* [The `matplotlib` MATLAB-like API](#The-matplotlib-MATLAB-like-API)
# MAGIC 		* [Example](#Example)
# MAGIC 	* [The `matplotlib` object-oriented API](#The-matplotlib-object-oriented-API)
# MAGIC 		* [Figure size, aspect ratio and DPI](#Figure-size,-aspect-ratio-and-DPI)
# MAGIC 		* [Saving figures](#Saving-figures)
# MAGIC 			* [What formats are available, and which ones should be used for best quality?](#What-formats-are-available,-and-which-ones-should-be-used-for-best-quality?)
# MAGIC 		* [Legends, labels and titles](#Legends,-labels-and-titles)
# MAGIC 		* [Formatting text: LaTeX, fontsize, font family](#Formatting-text:-LaTeX,-fontsize,-font-family)
# MAGIC 		* [Some LaTeX shown in Markdown cell](#Some-LaTeX-shown-in-Markdown-cell)
# MAGIC 		* [Setting colors, linewidths, linetypes](#Setting-colors,-linewidths,-linetypes)
# MAGIC 			* [Colors](#Colors)
# MAGIC 			* [Line and marker styles](#Line-and-marker-styles)
# MAGIC 		* [Control over axis appearance](#Control-over-axis-appearance)
# MAGIC 			* [Plot range](#Plot-range)
# MAGIC 			* [Logarithmic scale](#Logarithmic-scale)
# MAGIC 		* [Placement of ticks and custom tick labels](#Placement-of-ticks-and-custom-tick-labels)
# MAGIC 			* [Scientific notation](#Scientific-notation)
# MAGIC 		* [Axis number and axis label spacing](#Axis-number-and-axis-label-spacing)
# MAGIC 			* [Axis position adjustments](#Axis-position-adjustments)
# MAGIC 		* [Axis grid](#Axis-grid)
# MAGIC 		* [Axis spines](#Axis-spines)
# MAGIC 		* [Twin axes](#Twin-axes)
# MAGIC 		* [Axes where x and y are zero](#Axes-where-x-and-y-are-zero)
# MAGIC 		* [Other 2D plot styles](#Other-2D-plot-styles)
# MAGIC 		* [Text annotation](#Text-annotation)
# MAGIC 		* [Figures with multiple subplots and insets](#Figures-with-multiple-subplots-and-insets)
# MAGIC 			* [subplots](#subplots)
# MAGIC 			* [subplot2grid](#subplot2grid)
# MAGIC 			* [gridspec](#gridspec)
# MAGIC 			* [add_axes](#add_axes)
# MAGIC 		* [Colormap and contour figures](#Colormap-and-contour-figures)
# MAGIC 			* [pcolor](#pcolor)
# MAGIC 			* [imshow](#imshow)
# MAGIC 			* [contour](#contour)
# MAGIC 	* [3D figures](#3D-figures)
# MAGIC 		* &nbsp;
# MAGIC 			* [Surface plots](#Surface-plots)
# MAGIC 			* [Wire-frame plot](#Wire-frame-plot)
# MAGIC 			* [Coutour plots with projections](#Coutour-plots-with-projections)
# MAGIC 			* [Change the view angle](#Change-the-view-angle)
# MAGIC 		* [Animations](#Animations)
# MAGIC 		* [Backends](#Backends)
# MAGIC 			* [Generating SVG with the svg backend](#Generating-SVG-with-the-svg-backend)
# MAGIC 			* [The IPython notebook inline backend](#The-IPython-notebook-inline-backend)
# MAGIC 			* [Interactive backend (this makes more sense in a Python script file)](#Interactive-backend-%28this-makes-more-sense-in-a-Python-script-file%29)
# MAGIC 	* [Further reading](#Further-reading)
# MAGIC * [`seaborn` — statistical data visualization](#seaborn-—-statistical-data-visualization)
# MAGIC * [`bokeh` — web-based interactive visualization](#bokeh-—-web-based-interactive-visualization)

# COMMAND ----------

# MAGIC %md <hr/>
# MAGIC <img src="img/ContinuumLogoStacked.png">
# MAGIC 
# MAGIC **Developed by**
# MAGIC 
# MAGIC * J.R. Johansson, [robert@riken.jp](mailto:robert@riken.jp) 
# MAGIC * David Mertz &lt;[dmertz@continuum.io](mailto:dmertz@continuum.io)&gt;
# MAGIC * Dhavide Aruliah &lt;[daruliah@continuum.io](mailto:daruliah@continuum.io)&gt;
# MAGIC 
# MAGIC **Taught by**
# MAGIC 
# MAGIC * *&lt;Fill in instructor info at start of class&gt;*
# MAGIC 
# MAGIC This course was developed by Continuum Analytics, based on a tutorial created by J.R. Johansson (robert@riken.jp) http://dml.riken.jp/~rob/
# MAGIC 
# MAGIC The latest version of Johansson's version of this [IPython notebook](http://ipython.org/notebook.html) lecture is available at [http://github.com/jrjohansson/scientific-python-lectures](http://github.com/jrjohansson/scientific-python-lectures).
# MAGIC 
# MAGIC The other notebooks in his lecture series are indexed at [http://jrjohansson.github.io](http://jrjohansson.github.io).
# MAGIC 
# MAGIC (c) [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/), J.R. Johansson, Continuum Analytics

# COMMAND ----------

# MAGIC %md # Learning Objectives:

# COMMAND ----------

# MAGIC %md After completion of this module, learners should be able to:
# MAGIC * construct reproducible scripts for generation of figures
# MAGIC * construct bare-bones two-dimensional plots
# MAGIC * customize plot objects (e.g., position, size, color, line thickness, axis ticks, etc.)
# MAGIC * annotate plots with custom text, legends, labels, etc.
# MAGIC * figure out how to construct more advanced figures (e.g., subplots, logartihmic plots, animations, etc.)
# MAGIC * explain and use backends to customize figure output (e.g., to files, animations, interactive windows, etc.)

# COMMAND ----------

# MAGIC %md ## Some comments on pedagogical style

# COMMAND ----------

# MAGIC %md * We will teach this course using Python 3, not Python 2.  The differences are small, but Python 3 is the way of future development.
# MAGIC * We will use this IPython Notebook (now called *Jupyter*) to write our shared code, and the version of this notebook enhanced during this class will be shared with all students.
# MAGIC * Students will also be provided with *Exercise Notebooks* in which to solve problems, make individual notes, and generally keep a personalized record of this class. 
# MAGIC * For both the shared instruction notebook and the excericse notebooks, the saved copies allow you to scroll back easily to everything you have done in one continuous interactive lesson, and save your work to review at breaks or overnight.

# COMMAND ----------

# MAGIC %md # `matplotlib` — 2D and 3D plotting in Python

# COMMAND ----------

# This line configures matplotlib to show figures embedded in the notebook, 
# instead of opening a new window for each figure. More about that later. 
# If you are using an old version of IPython, try using '%pylab inline' instead.
%matplotlib inline

# COMMAND ----------

# MAGIC %md ## Introduction

# COMMAND ----------

# MAGIC %md Matplotlib is an excellent 2D and 3D graphics library for generating scientific figures. Some of the many advantages of this library include:
# MAGIC 
# MAGIC * Easy to get started
# MAGIC * Support for LaTeX formatted labels and texts
# MAGIC * Great control of every element in a figure, including figure size and DPI. 
# MAGIC * High-quality output in many formats, including PNG, PDF, SVG, EPS, and PGF.
# MAGIC * GUI for interactively exploring figures *and* support for headless generation of figure files (useful for batch jobs).
# MAGIC 
# MAGIC Matplotlib is well suited for generating figures for scientific publications because all aspects of the figure can be controlled *programmatically*. This is important for reproducibility, and convenient when one needs to regenerate the figure with updated data or change its appearance. 
# MAGIC 
# MAGIC More information at the Matplotlib web page: http://matplotlib.org/

# COMMAND ----------

# MAGIC %md To get started using Matplotlib in a Python program, either include the symbols from the `pylab` module (the easy way):

# COMMAND ----------

from pylab import *

# COMMAND ----------

# MAGIC %md or import the `matplotlib.pyplot` module under the name `plt` (the tidy way):

# COMMAND ----------

import matplotlib.pyplot as plt
import numpy as np

# COMMAND ----------

# MAGIC %md ## The `matplotlib` MATLAB-like API

# COMMAND ----------

# MAGIC %md A great way to get started with plotting using matplotlib is to use the MATLAB-like API provided by matplotlib. 
# MAGIC 
# MAGIC It is designed to be compatible with MATLAB's plotting functions, so if you are familiar with MATLAB, start here.
# MAGIC 
# MAGIC To use this API from matplotlib, we need to include the symbols in the `pylab` module: 

# COMMAND ----------

# MAGIC %md ### Example

# COMMAND ----------

# MAGIC %md A simple figure with MATLAB-like plotting API:

# COMMAND ----------

x = np.linspace(0, 5, 10)
y = x ** 2

# COMMAND ----------

x, y

# COMMAND ----------

figure()
plot(x, y, 'g')
xlabel('x')
ylabel('y')
title('title')
show()

# COMMAND ----------

# MAGIC %md Most of the plotting-related functions in MATLAB are covered by the `pylab` module. For example, subplot and color/symbol selection:

# COMMAND ----------

subplot(1,2,1)
plot(x, y, 'r--')
subplot(1,2,2)
plot(y, x, 'g*-');

# COMMAND ----------

# MAGIC %md The pylab MATLAB-style API is easy to get started with if you are familiar with MATLAB, and it has a minimum of coding overhead for simple plots. 
# MAGIC 
# MAGIC However, I'd discourage you from using the MATLAB-compatible API for anything but the simplest figures.
# MAGIC 
# MAGIC For advanced figures with subplots, insets and other components, I recommend learning and using matplotlib's remarkably powerful, object-oriented plotting API. 

# COMMAND ----------

# MAGIC %md ## The `matplotlib` object-oriented API

# COMMAND ----------

# MAGIC %md The main idea with object-oriented programming is to have objects to which one can apply functions and actions, and no object or program states should be global (such as the MATLAB-like API). The real advantage of this approach becomes apparent when more than one figure is created, or when a figure contains more than one subplot. 
# MAGIC 
# MAGIC To use the object-oriented API, we start out very much like in the previous example, but instead of creating a new global figure instance, we store a reference to the newly created figure instance in the `fig` variable, and from it we create a new axis instance `axes` using the `add_axes` method in the `Figure` class instance `fig`:

# COMMAND ----------

fig = plt.figure()

graph = fig.add_axes([0, 0, 1, 0.3]) 
# left, bottom, width, height (range 0 to 1)

graph.plot(x, y, 'r')

graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_title('title');

# COMMAND ----------

# MAGIC %md Although a bit more code is involved, the advantage is that we now have full control of where the plot axes are placed, and we can easily add more than one axis to the figure:

# COMMAND ----------

fig = plt.figure()

graph1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
graph2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes

# main figure
graph1.plot(x, y, 'r')
graph1.set_xlabel('x')
graph1.set_ylabel('y')
graph1.set_title('Title\n')

# insert
graph2.plot(y, x, 'g')
graph2.set_xlabel('y')
graph2.set_ylabel('x')
graph2.set_title('Inset Title');

# COMMAND ----------

# MAGIC %md If we don't care about being explicit about where our plot axes are placed in the figure canvas, then we can use one of the many axis layout managers in matplotlib. My favorite is `subplots`, which can be used like this:

# COMMAND ----------

fig, axes = plt.subplots()

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');

# COMMAND ----------

fig, axes = plt.subplots(nrows=1, ncols=4)


styles = ['go-','r+', 'bx-', 'g--']
for style, ax in zip(styles, axes):
    ax.plot(x, y, style)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

# COMMAND ----------

# MAGIC %md That was easy, but it isn't so pretty with overlapping figure axes and labels, right?
# MAGIC 
# MAGIC We can deal with that by using the `fig.tight_layout` method, which automatically adjusts the positions of the axes on the figure canvas so that there is no overlapping content:

# COMMAND ----------

fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
    
fig.tight_layout()

# COMMAND ----------

# MAGIC %md ### Figure size, aspect ratio and DPI

# COMMAND ----------

# MAGIC %md Matplotlib allows the aspect ratio, DPI and figure size to be specified when the `Figure` object is created, using the `figsize` and `dpi` keyword arguments. `figsize` is a tuple of the width and height of the figure in inches, and `dpi` is the dots-per-inch (pixel per inch). To create an 800x400 pixel, 100 dots-per-inch figure, we can do: 

# COMMAND ----------

fig = plt.figure(figsize=(8,4), dpi=100)
plt.plot(x,y)
plt.show()

# COMMAND ----------

# MAGIC %md The same arguments can also be passed to layout managers, such as the `subplots` function:

# COMMAND ----------

fig, axes = plt.subplots(figsize=(12,3))

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');
plt.show()

# COMMAND ----------

# MAGIC %md ### Saving figures

# COMMAND ----------

# MAGIC %md To save a figure to a file, we can use the `savefig` method in the `Figure` class:

# COMMAND ----------

fig.savefig("filename.png")
!open filename.png

# COMMAND ----------

# MAGIC %md Here we can also optionally specify the DPI and choose between different output formats:

# COMMAND ----------

fig.savefig("filename.png", dpi=200)
!open filename.png

# COMMAND ----------

fig.savefig("filename.pdf")
!open filename.pdf

# COMMAND ----------

# MAGIC %md #### What formats are available, and which ones should be used for best quality?

# COMMAND ----------

# MAGIC %md Matplotlib can generate high-quality output in a number of formats, including PNG, JPG, EPS, SVG, PGF and PDF. For scientific papers, I recommend using PDF whenever possible. (LaTeX documents compiled with `pdflatex` can include PDFs using the `includegraphics` command). In some cases, PGF can also be a good alternative.

# COMMAND ----------

# MAGIC %md ### Legends, labels and titles

# COMMAND ----------

# MAGIC %md Now that we have covered the basics of how to create a figure canvas and add axes instances to the canvas, let's look at how to decorate a figure with titles, axis labels, and legends.

# COMMAND ----------

# MAGIC %md **Figure titles**
# MAGIC 
# MAGIC A title can be added to each axis instance in a figure. To set the title, use the `set_title` method in the axes instance:

# COMMAND ----------

ax.set_title("title");

# COMMAND ----------

# MAGIC %md **Axis labels**
# MAGIC 
# MAGIC Similarly, with the methods `set_xlabel` and `set_ylabel`, we can set the labels of the X and Y axes:

# COMMAND ----------

ax.set_xlabel("x")
ax.set_ylabel("y");

# COMMAND ----------

# MAGIC %md **Legends**
# MAGIC 
# MAGIC Legends for curves in a figure can be added in two ways. One method is to use the `legend` method of the axis object and pass a list/tuple of legend texts for the previously defined curves:

# COMMAND ----------

ax.legend(["curve1", "curve2", "curve3"]);

# COMMAND ----------

# MAGIC %md The method described above follows the MATLAB API. It is somewhat prone to errors and inflexible if curves are added to or removed from the figure (resulting in a wrongly labelled curve).
# MAGIC 
# MAGIC A better method is to use the `label="label text"` keyword argument when plots or other objects are added to the figure, and then using the `legend` method without arguments to add the legend to the figure: 

# COMMAND ----------

ax.plot(x, x**2, label="curve1")
ax.plot(x, x**3, label="curve2")
ax.legend();
plt.show()

# COMMAND ----------

# MAGIC %md The advantage with this method is that if curves are added or removed from the figure, the legend is automatically updated accordingly.
# MAGIC 
# MAGIC The `legend` function takes an optional keyword argument `loc` that can be used to specify where in the figure the legend is to be drawn. The allowed values of `loc` are numerical codes for the various places the legend can be drawn. See http://matplotlib.org/users/legend_guide.html#legend-location for details. Some of the most common `loc` values are:

# COMMAND ----------

ax.legend(loc=0) # let matplotlib decide the optimal location
ax.legend(loc=1) # upper right corner
ax.legend(loc=2) # upper left corner
ax.legend(loc=3) # lower left corner
ax.legend(loc=4) # lower right corner
# .. many more options are available

# COMMAND ----------

# MAGIC %md The following figure shows how to use the figure title, axis labels and legends described above:

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(x, x**2, label="y = x**2")
ax.plot(x, x**3, "ro-", label="y = x**3")
ax.legend(loc=2); # upper left corner
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Title');

# COMMAND ----------

# MAGIC %md ### Formatting text: LaTeX, fontsize, font family

# COMMAND ----------

# MAGIC %md The figure above is functional, but it does not (yet) satisfy the criteria for a figure used in a publication. First and foremost, we need to have \LaTeX formatted text, and second, we need to be able to adjust the font size to appear legibly in a publication.
# MAGIC 
# MAGIC Matplotlib has great support for LaTeX. All we need to do is to use dollar signs to encapsulate LaTeX in any text (legend, title, label, etc.). For example, `"$y=x^3$"`.
# MAGIC 
# MAGIC But here we can run into a slightly subtle problem with LaTeX code and Python text strings. In LaTeX, we frequently use the backslash in commands, for example `\alpha` to produce the symbol $\alpha$. But the backslash already has a meaning in Python strings (the escape code character). To avoid Python messing up our LaTeX code, we need to use "raw" text strings. Raw text strings are prepended with an '`r`', like `r"\alpha"` or `r'\alpha'` instead of `"\alpha"` or `'\alpha'`:

# COMMAND ----------

# MAGIC %md ### Some LaTeX shown in Markdown cell

# COMMAND ----------

# MAGIC %md $x = \sum_0^{\infty} \frac{a}{b}$

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$', fontsize=18)
ax.set_ylabel(r'$y$', fontsize=18)
ax.set_title("Title");

# COMMAND ----------

# MAGIC %md We can also change the global font size and font family, which applies to all text elements in a figure (tick labels, axis labels and titles, legends, etc.):

# COMMAND ----------

# Update the matplotlib configuration parameters:
matplotlib.rcParams.update({'font.size': 18, 'font.family': 'serif'})

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$\Omega$')
ax.set_title(r'$\aleph_0$');

# COMMAND ----------

# MAGIC %md A good choice of global fonts are the STIX fonts: 

# COMMAND ----------

# Update the matplotlib configuration parameters:
matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title');

# COMMAND ----------

# MAGIC %md Or, alternatively, we can request that matplotlib use LaTeX to render the text elements in the figure:

# COMMAND ----------

# Not installed here!
# matplotlib.rcParams.update({'font.size': 18, 'text.usetex': True})

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title');

# COMMAND ----------

# restore
matplotlib.rcParams.update({'font.size': 12, 'font.family': 'sans', 'text.usetex': False})

# COMMAND ----------

# MAGIC %md ### Setting colors, linewidths, linetypes

# COMMAND ----------

# MAGIC %md #### Colors

# COMMAND ----------

# MAGIC %md With matplotlib, we can define the colors of lines and other graphical elements in a number of ways. First of all, we can use the MATLAB-like syntax where `'b'` means blue, `'g'` means green, etc. The MATLAB API for selecting line styles are also supported: where, for example, 'b.-' means a blue line with dots:

# COMMAND ----------

# MATLAB style line color and style 
ax.plot(x, x**2, 'b.-') # blue line with dots
ax.plot(x, x**3, 'g--') # green dashed line

# COMMAND ----------

# MAGIC %md We can also define colors by their names or RGB hex codes and optionally provide an alpha value using the `color` and `alpha` keyword arguments:

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(x, 1.5*x, color="#15cc55")        # RGB hex code for a greenish color
ax.plot(x, x+2, color="#1155dd", linewidth=3) # RGB hex code for a bluish color
ax.plot(x, x+1, color="red", alpha=0.5, linewidth=4) 
# half-transparant red


# COMMAND ----------

# MAGIC %md #### Line and marker styles

# COMMAND ----------

# MAGIC %md To change the line width, we can use the `linewidth` or `lw` keyword argument. The line style can be selected using the `linestyle` or `ls` keyword arguments:

# COMMAND ----------

fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color="blue", linewidth=0.25, label="A")
ax.plot(x, x+2, color="blue", linewidth=0.50, label="B")
ax.plot(x, x+3, color="blue", linewidth=1.00, label="C")
ax.plot(x, x+4, color="blue", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="red", lw=2, linestyle='-')
ax.plot(x, x+6, color="red", lw=2, ls='-.')
ax.plot(x, x+7, color="red", lw=2, ls=':')

# custom dash
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="green", lw=2, ls='*', marker='+')
ax.plot(x, x+10, color="green", lw=2, ls='*', marker='o')
ax.plot(x, x+11, color="green", lw=2, ls='*', marker='s')
ax.plot(x, x+12, color="green", lw=2, ls='*', marker='1')

# marker size and color
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2, label="D")
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue");
ax.legend(loc=0, fancybox=True, title="Legend")

# COMMAND ----------

# MAGIC %md ### Control over axis appearance

# COMMAND ----------

# MAGIC %md The appearance of the axes is an important aspect of a figure that we often need to modify to make publication quality graphics. We need to be able to control where the ticks and labels are placed, modify the font size and possibly the labels used on the axes. In this section we will look at controling those properties in a matplotlib figure.

# COMMAND ----------

# MAGIC %md #### Plot range

# COMMAND ----------

# MAGIC %md First, let's configure the ranges of the axes. We can use the `set_ylim` and `set_xlim` methods in the axis object, or `axis('tight')` for automatically getting "tightly fitted" axes ranges:

# COMMAND ----------

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range");

# COMMAND ----------

# MAGIC %md #### Logarithmic scale

# COMMAND ----------

# MAGIC %md It is also possible to set a logarithmic scale for one or both axes. This functionality is in fact only one application of a more general transformation system in Matplotlib. Each of the axes' scales are set separately using `set_xscale` and `set_yscale` methods, which accept one parameter (with the value "log" in this case):

# COMMAND ----------

fig, axes = plt.subplots(1, 2, figsize=(10,4))
      
axes[0].plot(x, x**2)
axes[0].plot(x, np.exp(x))
axes[0].set_title("Normal scale")

axes[1].plot(x, x**2, x, np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)");

# COMMAND ----------

# MAGIC %md ### Placement of ticks and custom tick labels

# COMMAND ----------

# MAGIC %md We can explicitly determine where we want the axis ticks with `set_xticks` and `set_yticks`, which both take a list of values for where on the axis the ticks are to be placed. We can also use the `set_xticklabels` and `set_yticklabels` methods to provide a list of custom text labels for each tick location:

# COMMAND ----------

fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(x, x**2, x, x**3, lw=2)

ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'], fontsize=18)

yticks = [0, 50, 100, 150]
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18); # use LaTeX formatted labels
plt.show()

# COMMAND ----------

# MAGIC %md There are a number of more advanced methods for controlling major and minor tick placement in matplotlib figures, such as automatic placement according to different policies. See http://matplotlib.org/api/ticker_api.html for details.

# COMMAND ----------

# MAGIC %md #### Scientific notation

# COMMAND ----------

# MAGIC %md With large numbers on axes, it is often better to use scientific notation:

# COMMAND ----------

fig, ax = plt.subplots(1, 1)
      
ax.plot(x, x**2, x, exp(x))
ax.set_title("scientific notation")

ax.set_yticks([0, 50, 100, 150])

from matplotlib import ticker
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
ax.yaxis.set_major_formatter(formatter)
plt.show()

# COMMAND ----------

# MAGIC %md ### Axis number and axis label spacing

# COMMAND ----------

# distance between x and y axis and the numbers on the axes
rcParams['xtick.major.pad'] = 5
rcParams['ytick.major.pad'] = 5

fig, ax = plt.subplots(1, 1)
      
ax.plot(x, x**2, x, exp(x))
ax.set_yticks([0, 50, 100, 150])

ax.set_title("label and axis spacing")

# padding between axis label and axis numbers
ax.xaxis.labelpad = 5
ax.yaxis.labelpad = 5

ax.set_xlabel("x")
ax.set_ylabel("y");

# COMMAND ----------

# restore defaults
rcParams['xtick.major.pad'] = 3
rcParams['ytick.major.pad'] = 3

# COMMAND ----------

# MAGIC %md #### Axis position adjustments

# COMMAND ----------

# MAGIC %md Unfortunately when saving figures, the labels are sometimes clipped. When necessary, adjust the positions of axes a little using `subplots_adjust`:

# COMMAND ----------

fig, ax = plt.subplots(1, 1)
      
ax.plot(x, x**2, x, exp(x))
ax.set_yticks([0, 50, 100, 150])

ax.set_title("title")
ax.set_xlabel("x")
ax.set_ylabel("y")

fig.subplots_adjust(left=0.15, right=.9, bottom=0.1, top=0.9);

# COMMAND ----------

# MAGIC %md ### Axis grid

# COMMAND ----------

# MAGIC %md With the `grid` method in the axis object, we can turn on and off grid lines. We can also customize the appearance of the grid lines using the same keyword arguments as the `plot` function:

# COMMAND ----------

fig, axes = plt.subplots(1, 2, figsize=(10,3))

# default grid appearance
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)

# custom grid appearance
axes[1].plot(x, x**2, x, x**3, lw=2)
axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)

# COMMAND ----------

# MAGIC %md ### Axis spines

# COMMAND ----------

# MAGIC %md We can also change the properties of axis spines:

# COMMAND ----------

fig, ax = plt.subplots(figsize=(6,2))

ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('green')

ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)

# turn off axis spine to the right
ax.spines['right'].set_color("none")
ax.yaxis.tick_left() # only ticks on the left side

# COMMAND ----------

# MAGIC %md ### Twin axes

# COMMAND ----------

# MAGIC %md Sometimes it is useful to have dual x or y axes in a figure; for example, when plotting curves with different units together. Matplotlib supports this with the `twinx` and `twiny` functions:

# COMMAND ----------

fig, ax1 = plt.subplots()

ax1.plot(x, x**2, lw=2, color="blue")
ax1.set_ylabel(r"area $(m^2)$", fontsize=18, color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")
    
ax2 = ax1.twinx()
ax2.plot(x, x**3, lw=2, color="red")
ax2.set_ylabel(r"volume $(m^3)$", fontsize=18, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")

# COMMAND ----------

# MAGIC %md ### Axes where x and y are zero

# COMMAND ----------

fig, ax = plt.subplots()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0)) # set position of x spine to x=0

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))   # set position of y spine to y=0

xx = np.linspace(-0.75, 1., 100)
ax.plot(xx, xx**3);

# COMMAND ----------

# MAGIC %md ### Other 2D plot styles

# COMMAND ----------

# MAGIC %md In addition to the regular `plot` method, there are a number of other functions for generating different kind of plots. Some of the more useful ones are shown below. 
# MAGIC 
# MAGIC TIP: See the [matplotlib plot gallery](http://matplotlib.org/gallery.html) for a complete list of available plot types. 

# COMMAND ----------

n = array([0,1,2,3,4,5])

# COMMAND ----------

fig, axes = plt.subplots(1, 4, figsize=(12,3))

axes[0].scatter(xx, xx + 0.25*randn(len(xx)))
axes[0].set_title("scatter")

axes[1].step(n, n**2, lw=2)
axes[1].set_title("step")

axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
axes[2].set_title("bar")

axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5);
axes[3].set_title("fill_between");

# COMMAND ----------

# polar plot using add_axes and polar projection
fig = plt.figure()
ax = fig.add_axes([0.0, 0.0, .6, .6], polar=True)
t = linspace(0, 2 * pi, 100)
ax.plot(t, t, color='blue', lw=3);

# COMMAND ----------

# A histogram
n = np.random.randn(100000)
fig, axes = plt.subplots(1, 2, figsize=(12,4))

axes[0].hist(n)
axes[0].set_title("Default histogram")
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title("Cumulative detailed histogram")
axes[1].set_xlim((min(n), max(n)));

# COMMAND ----------

# MAGIC %md ### Text annotation

# COMMAND ----------

# MAGIC %md We can annotate text in matplotlib figures using the `text` function. It supports LaTeX formatting just like axis label texts and titles:

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(xx, xx**2, xx, xx**3)

ax.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
ax.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green");

# COMMAND ----------

# MAGIC %md ### Figures with multiple subplots and insets

# COMMAND ----------

# MAGIC %md We can add axes to a matplotlib Figure canvas manually using `fig.add_axes` or with a sub-figure layout manager such as `subplots`, `subplot2grid`, or `gridspec`:

# COMMAND ----------

# MAGIC %md #### subplots

# COMMAND ----------

fig, ax = plt.subplots(2, 3)
fig.tight_layout()

# COMMAND ----------

# MAGIC %md #### subplot2grid

# COMMAND ----------

fig = plt.figure()
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
fig.tight_layout()

# COMMAND ----------

# MAGIC %md #### gridspec

# COMMAND ----------

import matplotlib.gridspec as gridspec

# COMMAND ----------

fig = plt.figure()

gs = gridspec.GridSpec(2, 3, height_ratios=[2,1], width_ratios=[1,2,1])
for g in gs:
    ax = fig.add_subplot(g)
    
fig.tight_layout()

# COMMAND ----------

# MAGIC %md #### add_axes

# COMMAND ----------

# MAGIC %md Manually adding axes with `add_axes` is useful for adding insets to figures:

# COMMAND ----------

fig, ax = plt.subplots()

ax.plot(xx, xx**2, xx, xx**3)
fig.tight_layout()

# inset
inset_ax = fig.add_axes([0.2, 0.55, 0.35, 0.35]) # X, Y, width, height

inset_ax.plot(xx, xx**2, xx, xx**3)
inset_ax.set_title('zoom near origin')

# set axis range
inset_ax.set_xlim(-.2, .2)
inset_ax.set_ylim(-.005, .01)

# set axis tick locations
inset_ax.set_yticks([0, 0.005, 0.01])
inset_ax.set_xticks([-0.1,0,.1]);

# COMMAND ----------

# MAGIC %md ### Colormap and contour figures

# COMMAND ----------

# MAGIC %md Colormaps and contour figures are useful for plotting functions of two variables. In most of these functions we will use a colormap to encode one dimension of the data. There are a number of predefined colormaps. It is relatively straightforward to define custom colormaps. For a list of pre-defined colormaps, see: http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps

# COMMAND ----------

alpha = 0.7
phi_ext = 2 * pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * cos(phi_p)*cos(phi_m) - alpha * cos(phi_ext - 2*phi_p)

# COMMAND ----------

phi_m = linspace(0, 2*pi, 200)
phi_p = linspace(0, 2*pi, 200)
X,Y = meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

# COMMAND ----------

# MAGIC %md #### pcolor

# COMMAND ----------

fig, ax = plt.subplots()

#p = ax.pcolor(X/(2*pi), Y/(2*pi), Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
p = ax.pcolor(X/(2*pi), Y/(2*pi), Z, cmap=cm.autumn, vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p, ax=ax)

# COMMAND ----------

dir(cm)

# COMMAND ----------

# MAGIC %md #### imshow

# COMMAND ----------

fig, ax = plt.subplots()

im = ax.imshow(Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
im.set_interpolation('bilinear')

cb = fig.colorbar(im, ax=ax)

# COMMAND ----------

# MAGIC %md #### contour

# COMMAND ----------

fig, ax = plt.subplots()

cnt = ax.contour(Z, cmap=cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])

# COMMAND ----------

# MAGIC %md ## 3D figures

# COMMAND ----------

# MAGIC %md To use 3D graphics in matplotlib, we first need to create an instance of the `Axes3D` class. 3D axes can be added to a matplotlib figure canvas in exactly the same way as 2D axes; or, more conveniently, by passing a `projection='3d'` keyword argument to the `add_axes` or `add_subplot` methods.

# COMMAND ----------

from mpl_toolkits.mplot3d.axes3d import Axes3D

# COMMAND ----------

# MAGIC %md #### Surface plots

# COMMAND ----------

fig = plt.figure(figsize=(14,6))

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)

# COMMAND ----------

# MAGIC %md #### Wire-frame plot

# COMMAND ----------

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1, 1, 1, projection='3d')

p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)

# COMMAND ----------

# MAGIC %md #### Coutour plots with projections

# COMMAND ----------

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax.contour(X, Y, Z, zdir='z', offset=-pi, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-pi, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=3*pi, cmap=cm.coolwarm)

ax.set_xlim3d(-pi, 2*pi);
ax.set_ylim3d(0, 3*pi);
ax.set_zlim3d(-pi, 2*pi);

# COMMAND ----------

# MAGIC %md #### Change the view angle

# COMMAND ----------

# MAGIC %md We can change the perspective of a 3D plot using the `view_init` method, which takes two arguments: `elevation` and `azimuth` angle (in degrees):

# COMMAND ----------

fig = plt.figure(figsize=(12,6))

ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
ax.view_init(30, 45)

ax = fig.add_subplot(1,2,2, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
ax.view_init(70, 30)

fig.tight_layout()

# COMMAND ----------

# MAGIC %md ### Animations

# COMMAND ----------

# MAGIC %md Matplotlib also includes a simple API for generating animations for sequences of figures. With the `FuncAnimation` function, we can generate a movie file from sequences of figures. The function takes the following arguments: 
# MAGIC 
# MAGIC * `fig`, a figure canvas, 
# MAGIC * `func`, a function that we provide which updates the figure, 
# MAGIC * `init_func`, a function we provide to setup the figure, 
# MAGIC * `frame`, the number of frames to generate, and 
# MAGIC * `blit`, which tells the animation function to only update parts of the frame which have changed (for smoother animations):
# MAGIC 
# MAGIC     def init():
# MAGIC         # setup figure
# MAGIC 
# MAGIC     def update(frame_counter):
# MAGIC         # update figure for new frame
# MAGIC 
# MAGIC     anim = animation.FuncAnimation(fig, update, init_func=init, frames=200, blit=True)
# MAGIC 
# MAGIC     anim.save('animation.mp4', fps=30) # fps = frames per second
# MAGIC 
# MAGIC To use the animation features in matplotlib we first need to import the module `matplotlib.animation`:

# COMMAND ----------

from matplotlib import animation

# COMMAND ----------

# solve the ode problem of the double compound pendulum again

from scipy.integrate import odeint

g = 9.82; L = 0.5; m = 0.1

def dx(x, t):
    x1, x2, x3, x4 = x[0], x[1], x[2], x[3]
    
    dx1 = 6.0/(m*L**2) * (2 * x3 - 3 * cos(x1-x2) * x4)/(16 - 9 * cos(x1-x2)**2)
    dx2 = 6.0/(m*L**2) * (8 * x4 - 3 * cos(x1-x2) * x3)/(16 - 9 * cos(x1-x2)**2)
    dx3 = -0.5 * m * L**2 * ( dx1 * dx2 * sin(x1-x2) + 3 * (g/L) * sin(x1))
    dx4 = -0.5 * m * L**2 * (-dx1 * dx2 * sin(x1-x2) + (g/L) * sin(x2))
    return [dx1, dx2, dx3, dx4]

x0 = [pi/2, pi/2, 0, 0]  # initial state
t = linspace(0, 10, 250) # time coordinates
x = odeint(dx, x0, t)    # solve the ODE problem

# COMMAND ----------

# MAGIC %md Generate an animation that shows the positions of the pendulums as a function of time:

# COMMAND ----------

# MAGIC %md NOTE: To generate the movie file, we need to have either `ffmpeg` or `avconv` installed. Install it on Ubuntu using:
# MAGIC 
# MAGIC     $ sudo apt-get install ffmpeg
# MAGIC 
# MAGIC or (newer versions):
# MAGIC 
# MAGIC     $ sudo apt-get install libav-tools
# MAGIC 
# MAGIC On OS X, try: 
# MAGIC 
# MAGIC     $ sudo port install ffmpeg

# COMMAND ----------

!ffmpeg

# COMMAND ----------

fig, ax = plt.subplots(figsize=(5,5))

ax.set_ylim([-1.5, 0.5])
ax.set_xlim([1, -1])

pendulum1, = ax.plot([], [], color="red", lw=2)
pendulum2, = ax.plot([], [], color="blue", lw=2)

def init():
    pendulum1.set_data([], [])
    pendulum2.set_data([], [])

def update(n): 
    # n = frame counter
    # calculate the positions of the pendulums
    x1 = + L * sin(x[n, 0])
    y1 = - L * cos(x[n, 0])
    x2 = x1 + L * sin(x[n, 1])
    y2 = y1 - L * cos(x[n, 1])
    
    # update the line data
    pendulum1.set_data([0 ,x1], [0 ,y1])
    pendulum2.set_data([x1,x2], [y1,y2])

anim = animation.FuncAnimation(fig, update, init_func=init, frames=len(t), blit=True)

# anim.save can be called in a few different ways, some which might or might not work
# on different platforms and with different versions of matplotlib and video encoders
#anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'], writer=animation.FFMpegWriter())
#anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'])
anim.save('animation.mp4', fps=20, writer="ffmpeg", codec="libx264")
#anim.save('animation.mp4', fps=20, writer="avconvert", codec="libx264")

plt.close(fig)

# COMMAND ----------

from IPython.display import HTML
VIDEO_TAG = """<video controls>
 <source src="{0}" type="video/mp4">
 Your browser does not support the video tag.
</video>"""
video_tag = VIDEO_TAG.format('animation.mp4')
HTML(video_tag)

# COMMAND ----------

# If that doesn't work, try calling to shell
!open animation.mp4

# COMMAND ----------

# MAGIC %md ### Backends

# COMMAND ----------

# MAGIC %md Matplotlib has a number of "backends" which are responsible for rendering graphs. The different backends are able to generate graphics with different formats and display/event loops. There is a distinction between noninteractive backends (such as 'agg', 'svg', 'pdf', etc.) that are only used to generate image files (e.g., with the `savefig` function), and interactive backends (such as Qt4Agg, GTK, MaxOSX) that can display a GUI window for interactively exploring figures. 
# MAGIC 
# MAGIC A list of available backends are:

# COMMAND ----------

print(matplotlib.rcsetup.all_backends)

# COMMAND ----------

# MAGIC %md The default backend, called `agg`, is based on a library for raster graphics, which is great for generating raster formats like PNG.
# MAGIC 
# MAGIC Normally we don't need to bother with changing the default backend; but sometimes it can be useful to switch to, for example, PDF or GTKCairo (if you are using Linux) to produce high-quality vector graphics instead of raster-based graphics. 

# COMMAND ----------

# MAGIC %md #### Generating SVG with the svg backend

# COMMAND ----------

#
# RESTART THE NOTEBOOK: the matplotlib backend can only be 
# selected before pylab is imported! (e.g. Kernel > Restart)
# 
import matplotlib
matplotlib.use('svg')
import matplotlib.pylab as plt
import numpy
from IPython.display import Image, SVG

# COMMAND ----------

#
# Now we are using the svg backend to produce SVG vector graphics
#
fig, ax = plt.subplots()
t = numpy.linspace(0, 10, 100)
ax.plot(t, numpy.cos(t)*numpy.sin(t))
plt.savefig("test.svg")

# COMMAND ----------

#
# Show the produced SVG file. 
#
SVG(filename="test.svg")

# COMMAND ----------

# MAGIC %md #### The IPython notebook inline backend

# COMMAND ----------

# MAGIC %md When we use IPython notebook, it is convenient to use a matplotlib backend that outputs the graphics embedded in the notebook file. To activate this backend, somewhere in the beginning on the notebook, we add:
# MAGIC 
# MAGIC     %matplotlib inline
# MAGIC 
# MAGIC It is also possible to activate inline matplotlib plotting with:
# MAGIC 
# MAGIC     %pylab inline
# MAGIC 
# MAGIC The difference is that `%pylab inline` imports a number of packages into the global address space (scipy, numpy), while `%matplotlib inline` only sets up inline plotting. In new notebooks created for IPython 1.0+, I recommend using `%matplotlib inline`, since it is tidier and you have more control over which packages are imported and how. Commonly, scipy and numpy are imported separately with:
# MAGIC 
# MAGIC     import numpy as np
# MAGIC     import scipy as sp
# MAGIC     import matplotlib.pyplot as plt

# COMMAND ----------

# MAGIC %md The inline backend has a number of configuration options that can be set by using the IPython magic command `%config` to update settings in `InlineBackend`. For example, we can switch to SVG figures or higher-resolution figures with either:
# MAGIC 
# MAGIC     %config InlineBackend.figure_format='svg'
# MAGIC      
# MAGIC or:
# MAGIC 
# MAGIC     %config InlineBackend.figure_format='retina'
# MAGIC     
# MAGIC For more information, type:
# MAGIC 
# MAGIC     %config InlineBackend

# COMMAND ----------

# MAGIC %matplotlib inline
# MAGIC %config InlineBackend.figure_format='svg'
# MAGIC 
# MAGIC import matplotlib.pylab as plt
# MAGIC import numpy

# COMMAND ----------

#
# Now we are using the SVG vector graphics displaced inline in the notebook
#
fig, ax = plt.subplots()
t = numpy.linspace(0, 10, 100)
ax.plot(t, numpy.cos(t)*numpy.sin(t))
plt.savefig("test.svg")

# COMMAND ----------

# MAGIC %md #### Interactive backend (this makes more sense in a Python script file)

# COMMAND ----------

#
# RESTART THE NOTEBOOK: the matplotlib backend can only be selected before pylab is imported!
# (e.g. Kernel > Restart)
# 
import matplotlib
matplotlib.use('Qt4Agg') # or for example OS X
import matplotlib.pylab as plt
import numpy

# COMMAND ----------

# Now, open an interactive plot window with the Qt4Agg backend
fig, ax = plt.subplots()
t = numpy.linspace(0, 10, 100)
ax.plot(t, numpy.cos(t)*numpy.sin(t))
plt.show()

# COMMAND ----------

# MAGIC %md Note that when we use an interactive backend, we must call `plt.show()` to make the figure appear on the screen.

# COMMAND ----------

# MAGIC %md ## Further reading

# COMMAND ----------

# MAGIC %md * http://www.matplotlib.org - The project web page for matplotlib.
# MAGIC * https://github.com/matplotlib/matplotlib - The source code for matplotlib.
# MAGIC * http://matplotlib.org/gallery.html - A large gallery showcasing various types of plots matplotlib can create. Highly recommended! 
# MAGIC * http://www.loria.fr/~rougier/teaching/matplotlib - A good matplotlib tutorial.
# MAGIC * http://scipy-lectures.github.io/matplotlib/matplotlib.html - Another good matplotlib reference.

# COMMAND ----------

# MAGIC %md # `seaborn` — statistical data visualization

# COMMAND ----------

# MAGIC %md Seaborn is a Python visualization library based on `matplotlib`. It provides a high-level interface for drawing attractive statistical graphics.
# MAGIC 
# MAGIC Homepage for the Seaborn project: http://stanford.edu/~mwaskom/software/seaborn/

# COMMAND ----------

# MAGIC %md # `bokeh` — web-based interactive visualization

# COMMAND ----------

# MAGIC %md Bokeh is a Python interactive visualization library that targets modern web browsers for presentation. Its goal is to provide elegant, concise construction of novel graphics in the style of D3.js, but also deliver this capability with high-performance interactivity over very large or streaming datasets. Bokeh can help anyone who would like to quickly and easily create interactive plots, dashboards, and data applications.
# MAGIC 
# MAGIC Homepage for Bokeh: http://bokeh.pydata.org/