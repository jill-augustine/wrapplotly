Module wrapplotly.graphics
==========================

Functions
---------

    
`add_layer(data=None, x=None, y=None, layer=None, fig=None, row=None, col=None)`
:   Adds a layer to an existing figure

    
`autoplot(layers=None, data=None, x=None, y=None, fig=None, row=None, col=None, colorway=['rgb(102,194,165)', 'rgb(252,141,98)', 'rgb(141,160,203)', 'rgb(231,138,195)', 'rgb(166,216,84)', 'rgb(255,217,47)', 'rgb(229,196,148)', 'rgb(179,179,179)'], **kwargs)`
:   Creates one (sub)plot
    Parameters
    ----------
    layers: a list of lists (or array-like)
        - the inner lists hold details of the individual layers
        Each inner list must contain:
            0) the layer type either as a full word or one letter:
                - s(catter)
                - l(ine)
                - (bo)x
                - b(ar)
                - h(ist)
            1) the x axis column to be taken from data (if not specified as kwarg)
                OR a pandas.Series/numpy.ndarray/list of data
            2) the y axis column to be taken from data (if not specified as kwarg)
                OR a pandas.Series/numpy.ndarray/list of data
            3) a dict of keyword arguments to be passed to go.Functions() 
                e.g.  dict(connectgaps=True, opacity = 0.5)
               also accepts secondary_y parameter passed to add_trace()
    data: pandas.DataFrame
    x: (str) a column name from 'data' or an array-like to be used on all layers.
        x must then NOT be specified as part of the 'layers' argument
    y: (str) a column name from 'data' or an array-like to be used on all layers.
        y must then NOT be specified as part of the 'layers' argument
    fig: a predefined plotly.graph_objects.Figure on which to append the plot
    row: int (must also be specified if fig is specified)
    col: int (must also be specified if fig is specified)
    kwargs: keyword arguments passed onto fig.update_layout()

    
`multiplot(layers=None, nrows=None, ncols=None, fig=None, colorway=['rgb(102,194,165)', 'rgb(252,141,98)', 'rgb(141,160,203)', 'rgb(231,138,195)', 'rgb(166,216,84)', 'rgb(255,217,47)', 'rgb(229,196,148)', 'rgb(179,179,179)'], **kwargs)`
:   Creates a plot with multiple sub plots.
    Parameters
    ----------
    layers: This is an array-like of layeritems which are passed one-by-one to autoplot()
            positions can be skipped by setting that layer item to None
            e.g. [[layers_for_autoplot], None, [layers_for_autoplot]]
    **kwargs: keyword arguments passed onto fig.update_layout()
    
    Note
    ----
    In the case of axis kwargs, all subplots have two y-axes. 
    kwargs for multiplots are therefore for example: 
        xaxis3_title_text for the 3rd xaxis
        yaxis4_title_font for the 2nd yaxis of 2nd subplot (the fourth y axis in figure)

    
`multiplot_for_insights(layers=None, nrows=None, ncols=None, fig=None, colorway=['rgb(102,194,165)', 'rgb(252,141,98)', 'rgb(141,160,203)', 'rgb(231,138,195)', 'rgb(166,216,84)', 'rgb(255,217,47)', 'rgb(229,196,148)', 'rgb(179,179,179)'], subplot_titles=None, external_specs=None, shared_xaxes=False, shared_yaxes=False, vertical_spacing=0.02, horizontal_spacing=None, **kwargs)`
:   Creates a plot with multiple sub plots.
    layers: This is a list of layer-items which are passed one-by-one to autoplot()
            positions can be skipped by setting that layer item to None
            e.g. [[layers_for_autoplot()], None, [layers_for_autoplot()]]
    **kwargs are keyword arguments passed onto fig.update_layout()
    Note: in the case of kwargs. All subplots have two y-axes. kwargs for multiplots are therefore
    for example: xaxis3_title_text (for the 3rd xaxis) or 
                 yaxis4_title_font for the fourth y axis in figure (2nd yaxis of 2nd subplot)

    
`save_plot(plot, file, mode='static', **kwargs)`
:   Save a plot into external file, based on selected mode: option "static" exports plot as .png file,
    option "interactive" exports plot as html file.
    
    Parameters
    ----------
    plot: plotly.graph_objects.Figure
    file: str of filepath including file extension
    mode: str of 'interactive' or 'static'
    kwargs: kwargs passed on to write_image() for static plots and 
        to write_html() for interactive plots
    
    Returns
    -------
    None