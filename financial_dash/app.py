import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

import pandas as pd

import quandl

# Initialize the app
app = dash.Dash()

# Pull financial data down from quandl
df = quandl.get('FRED/GDP')

colors = {
    'background' : '#111111',
    'text' : '#7FDBFF'
}

app.layout = html.Div(children=[

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
                    'color' : colors['text']
                },
                'plot_bgcolor' : colors['background'],
                'paper_bgcolor' : colors['background']
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

app.css.append_css({
    "external_url" : "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
