import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

import pandas as pd
import numpy as np

import financial_dash.style.colors as colors

class SeriesPlot():
    """
    Creates a plot component using economic time series
        from Quandl
    """

    def __init__(self, data):
        """
        data is a list of dataframes returned from
            a service call to quandl
        """
        self.data = data
        all_values = [x['name'] for x in data]
        self.div = html.Div(children=[
            dcc.Graph(
                id='ts-plot',
                figure = self.build_figure(all_values)
            ),
            self.build_dropdown(),

        ])


    def build_figure(self, selected_series):
        """
        Plots the series returned by quandl
        """
        # Build the data for the plot
        plots = []
        for result in self.data:
            if result['name'] in selected_series:
                if result['name'] == 'Consumer Confidence':
                    values = [x/10 for x in result['values']]
                else:
                    values = result['values']
                plots.append(go.Scatter(
                    x = result['dates'],
                    y = values,
                    mode = 'line',
                    opacity = 0.7,
                    name = result['name']
                ))

        # Build the graph component
        figure={
            'data' : plots,
            'layout' : go.Layout(
                title = 'Economic Series Over Time',
                xaxis = {'title' : 'Year'},
                yaxis = {'title' : 'Value'},
                margin = {
                    'l' : 40,
                    'b' : 40,
                    't' : 10,
                    'r' : 10
                },
                legend = {'x':1, 'y':1},
                hovermode = 'closest',
                plot_bgcolor = colors.series_plot['background'],
                paper_bgcolor = colors.series_plot['background']
            )
        }
        return figure

    def build_dropdown(self):
        """
        Builds the obtions for the drop down menu
        """
        options = []
        values = []
        for result in self.data:
            options.append({
                'label' : result['name'],
                'value' : result['name']
            })
            values.append(result['name'])
        dropdown = dcc.Dropdown(
            id='ts-dropdown',
            options = options,
            value = values,
            multi = True
        )
        return dropdown












