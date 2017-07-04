import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

import pandas as pd

from financial_dash.style.colors

class SeriesPlot():
    """
    Creates a plot component using economic time series
        from Quandl
    """

    def __init__(self, df):
        """
        data is a list of dataframes returned from
            a service call to quandl
        """

        self.series_plot = html.Div(children=[

            # html.H1(children='Look at my awesome plot!'),
            dcc.Graph(
                id='gdp',
                figure={
                    'data' : [go.Scatter(
                        x=df.index,
                        y=df['Value'],
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
