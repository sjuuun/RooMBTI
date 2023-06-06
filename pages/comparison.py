import dash
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import html, dcc, callback
from dash.dependencies import Input, Output

from figures import daily_routine, indoor
from figures.bfi import bfi_compare
from figures.location_mapbox import location_mapbox
from figures.weekly_routine import weekly_routine
from figures.similarity_barpolar import half_ring_plot
from pages import Routine, SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID

dash.register_page(__name__, title="RooMBTI")

layout = html.Div(children=[
    dcc.Location('path', refresh=False),
    html.H1(children="Comparison"),

    html.Div(children="""
        Compare routines between me and roommate.
    """),

    dbc.Container([
        dbc.Row([
            dbc.Col(
                dcc.Graph(id='similarity', figure=half_ring_plot(SAMPLE_ROOMMATE_ID)),
                width=3,
            ),
            dbc.Col(
                dcc.Graph(id='bfi', figure=bfi_compare(SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID)),
                width=4,
            ),
            dbc.Col(
                dcc.Graph(id='indoor', figure=indoor.indoor_compare(SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID)),
                width=5
            ),
        ]),
        dbc.Row(
            dcc.Graph(id='daily_routine', figure=daily_routine.daily_routine_compare(SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID))
        ),
        dbc.Row([
            html.Div(
                html.Div(
                    dbc.RadioItems(
                        id="routine_type",
                        options=[
                            {"label": Routine.SLEEP.value, "value": Routine.SLEEP.name},
                            {"label": Routine.CLASS.value, "value": Routine.CLASS.name},
                            {"label": Routine.MEAL.value, "value": Routine.MEAL.name},
                            {"label": Routine.STUDY.value, "value": Routine.STUDY.name},
                            {"label": Routine.EXERCISE.value, "value": Routine.EXERCISE.name},
                        ],
                        value=Routine.SLEEP.name,
                        inline=True,
                    )
                )
            ),
            dbc.Col(
                dcc.Graph(id="weekly_routine", figure=weekly_routine([SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID]))
            ),
            dbc.Col(
                dcc.Graph(id="geographical_scatter", figure=location_mapbox([SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID]))
            )
        ]),
    ]),
])


def parse_roommate_id(query_parameter: str) -> str:
    return query_parameter.split('=')[-1]


@callback(
    Output('similarity', 'figure'),
    Input('path', 'search'),
)
def update_similarity(path):
    roommate_id = parse_roommate_id(path)
    return half_ring_plot(roommate_id)


@callback(
    Output('bfi', 'figure'),
    Input('path', 'search'),
)
def update_bfi(path):
    roommate_id = parse_roommate_id(path)
    return bfi_compare(SAMPLE_ME_ID, roommate_id)


@callback(
    Output('indoor', 'figure'),
    Input('path', 'search'),
)
def update_indoor(path):
    roommate_id = parse_roommate_id(path)
    return indoor.indoor_compare(SAMPLE_ME_ID, roommate_id)


@callback(
    Output('daily_routine', 'figure'),
    Input('path', 'search'),
)
def update_daily_routine(path):
    roommate_id = parse_roommate_id(path)
    return daily_routine.daily_routine_compare(SAMPLE_ME_ID, roommate_id)


@callback(
    Output('weekly_routine', 'figure'),
    [Input('path', 'search'), Input('routine_type', 'value')],
)
def update_weekly_routine(path, routine_type):
    roommate_id = parse_roommate_id(path)
    return weekly_routine([SAMPLE_ME_ID, roommate_id], routine_type)


@callback(
    Output('geographical_scatter', 'figure'),
    [Input('path', 'search'), Input('routine_type', 'value')],
)
def update_geographical_scatter(path, routine_type):
    roommate_id = parse_roommate_id(path)
    return location_mapbox([SAMPLE_ME_ID, roommate_id], routine_type)
