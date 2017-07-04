import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

import pandas as pd

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

        self.div = html.Div(children=[

            # html.H1(children='Look at my awesome plot!'),
            dcc.Graph(
                id='gdp',
                figure={
                    'data' : [go.Scatter(
                        x=data['dates'],
                        y=data['values'],
                        mode='line',
                        opacity=0.7
                    )],
                    'layout' : {
                        'title' : 'GDP Over Time',
                        'font' : {
                            'color' : colors.series_plot['text']
                        },
                        'plot_bgcolor' : colors.series_plot['background'],
                        'paper_bgcolor' : colors.series_plot['background']
                    }
                }
            ),
            dcc.Dropdown(
                options = [
                    {'label' : 'GDP', 'value' : 'GDP'}
                ],
                value = 'GDP'
            )
        ])
