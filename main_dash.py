from settings import config

import dash
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output

from app_layouts.layouts import make_layout
from helpers import isolation_forest, get_prepared_data

app = dash.Dash(__name__)
server = app.server

df = get_prepared_data()
layout_context = {'visible_columns': df.columns.copy()}
app.layout = make_layout(layout_context)


def check_anomaly(ip_network: str, cont_factor: float):
    result = isolation_forest(data=df, coll=ip_network, cont=cont_factor)
    df['anomaly'] = result


@app.callback(
    Output("time-series-chart", "figure"),
    Input("ip_network", "value"),
    Input('cont_factor', 'value'))
def display_time_series(ip_network, cont_factor: float):
    check_anomaly(ip_network, cont_factor)
    a = df.loc[df.anomaly == -1, [ip_network]]
    fig = px.line(
        df[ip_network],
        x=df.index,
        y=ip_network,
    )
    fig.add_trace(go.Scatter(mode="markers", x=a.index, y=a[ip_network], name="Аномалия"))
    return fig


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=config.app_port)
