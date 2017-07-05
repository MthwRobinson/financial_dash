import dash
from dash.dependencies import Input, Output

from financial_dash.components.series_plot import SeriesPlot
from financial_dash.services.quandl import QuandlService

# Initialize the app
app = dash.Dash()

# Pull financial data down from quandl
qs = QuandlService()
data = qs.get_quandl(from_file = True)
series_plot = SeriesPlot(data)

# Main app layout
app.layout = series_plot.div

# Functions to update graphs
@app.callback(
    Output('ts-plot', 'figure'),
    [Input('ts-dropdown', 'value')]
)
def update_ts_plot(selected_series):
    return series_plot.build_figure(selected_series)

app.css.append_css({
    "external_url" : "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
