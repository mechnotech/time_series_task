from dash import html, dcc


def make_layout(layout_context):
    return html.Div(children=[
        html.H1(children='Аномалии'),
        html.Div(children='Поиск аномалий во временных рядах.'),
        dcc.Graph(id="time-series-chart"),
        html.P("Выбор IP-сети:"),
        dcc.Dropdown(
            id="ip_network",
            options=layout_context['visible_columns'],
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
