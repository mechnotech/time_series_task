from dash import html, dcc


def make_layout(layout_context):
    return html.Div(
        children=[
            html.Div(
                children=[
                    html.P(children="\U0001F4E1", className="header-emoji"),
                    html.H1(
                        children="Аномалии", className="header-title"
                    ),
                    html.P(
                        children="Поиск аномалий во временных рядах",
                        className="header-description",
                    ),
                ],
                className="header",
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(children="IP подсеть", className="menu-title"),
                            dcc.Dropdown(
                                id="ip_network",
                                options=layout_context['visible_columns'],
                                value='85.249.0.0-85.249.255.255',
                                clearable=False,
                                searchable=True,
                                className='dropdown'
                            ),
                        ]
                    ),
                    html.Div(
                        children=[
                            html.Div(children="Модель", className="menu-title"),
                            dcc.Dropdown(
                                id="model",
                                options=['HBOS', 'Isolation Forest'],
                                value='HBOS',
                                clearable=False,
                                className="dropdown",
                            ),
                        ],
                    ),
                    html.Div(
                        children=[
                            html.Div(
                                children="Фактор контаминации",
                                className="Select-control2"
                            ),
                            dcc.Slider(
                                id="cont_factor",
                                min=0.01,
                                max=0.09,
                                step=0.01,
                                value=0.02,
                                className="slider"
                            ),
                        ]
                    ),

                ],
                className="menu",

            ),
            html.Div(
                children=[
                    html.Div(
                        children=dcc.Graph(
                            id="time-series-chart", config={"displayModeBar": False},
                        ),
                        className="card",
                    ),
                ],
                className="wrapper",
            ),
        ]
    )
