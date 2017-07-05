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
        self.div = html.Div(children=[
            dcc.Graph(
                id='gdp',
                figure={
                    'data' : self.build_data(),
                    'layout' : go.Layout(
                        title = 'Economic Series Over Time'
                        xaxis = {'title' : 'Year'},
                        yaxis = {'title' : 'Value'},
                        margin = {
                            'l' : 40,
                            'b' : 40,
                            't' : 10,
                            'r' : 10
                        },
                        legend = {'x':.8, 'y':0},
                        hovermode = 'closest',
                        plot_bgcolor = colors.series_plot['background'],
                        paper_bgcolor = colors.series_plot['background']
                    )
                }
            ),
            self.build_dropdown()
        ])

    def build_data(self):
        """
        Plots the series returned by quandl
        """
        plots = []
        for result in self.data:
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
        return plots

    def build_dropdown(self):
        """
        Builds the obtions for the drop down menu
        """
        options = []
        for result in self.data:
            options.append({
                'label' : result['name'],
                'value' : result['name']
            })
        dropdown = dcc.Dropdown(
            options = options,
            value = self.data[0]['name'],
            multi = True
        )
        return dropdown












