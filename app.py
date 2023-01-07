import numpy as np
from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from helpers import get_prepared_data, isolation_forest

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = get_prepared_data()
df['avg'] = df.mean(axis=1)
coll = '176.59.128.0-176.59.159.255'

def check_anomaly(ip_network: str):
    result = isolation_forest(data=df, coll=ip_network, cont=0.02)
    df['anomaly'] = result
    df['to_show'] = df.apply(lambda x: x[ip_network] if x['anomaly'] == -1 else None, axis=1)


check_anomaly(coll)
fig = px.line(
    df,
    x=df.index,
    y=coll,
    # range_x=['2021-12-01', '2022-02-15']
)
fig.add_trace(go.Scatter(mode="markers", x=df.index, y=df['to_show'], name="Anomaly"))

app.layout = html.Div(children=[
    html.H1(children='Аномалии'),

    html.Div(children='''
        Поиск аномалий во временных рядах.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
