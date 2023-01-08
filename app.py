from dash import Dash, dcc, html, Input, Output
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from helpers import get_prepared_data, isolation_forest
from settings import config

app = Dash(__name__)
server = app.server
np.random.seed(config.random_state)
df = get_prepared_data()
visible_columns = df.columns.copy()


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
        # range_x=['2021-12-01', '2022-02-15']
    )
    fig.add_trace(go.Scatter(mode="markers", x=a.index, y=a[ip_network], name="Аномалия"))
    return fig


app.layout = html.Div(children=[
    html.H1(children='Аномалии'),
    html.Div(children='Поиск аномалий во временных рядах.'),
    dcc.Graph(id="time-series-chart"),
    html.P("Выбор IP-сети:"),
    dcc.Dropdown(
        id="ip_network",
        options=visible_columns,
        value='85.249.0.0-85.249.255.255',
        clearable=True,
        searchable=True,
    ),
    html.P("Фактор контаминации (0.01 - 0.08)"),
    dcc.Slider(
        id="cont_factor",
        min=0.01,
        max=0.09,
        step=0.01,
        value=0.02
    )

])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=config.app_port)
