from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from helpers import get_prepared_data

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = get_prepared_data()
df['avg'] = df.mean(axis=1)
df['dash_date'] = df.index



fig = px.line(df, x=df.index, y='avg')

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