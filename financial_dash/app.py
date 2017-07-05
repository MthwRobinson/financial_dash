import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import pandas as pd
import quandl

from financial_dash.components.series_plot import SeriesPlot
from financial_dash.services.quandl import QuandlService

# Initialize the app
app = dash.Dash()

# Pull financial data down from quandl
qs = QuandlService()
data = qs.get_quandl(from_file = True)
series_plot = SeriesPlot(data)

app.layout = series_plot.div

app.css.append_css({
    "external_url" : "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
