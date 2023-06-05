import dash
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import html, dcc, callback
from dash.dependencies import Input, Output

from figures import daily_routine, indoor
from figures.bfi import bfi_compare
from figures.location_mapbox import location_mapbox
from figures.weekly_routine import weekly_routine
from pages import Routine, SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID

dash.register_page(__name__, title="RooMBTI")

layout = html.Div(children=[
    html.H1(children="Comparison"),

    html.Div(children="""
        Compare routines between me and roommate.
    """),

    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div(id='similarity', children=[
                    daq.Gauge(
                        label='Similarity',
                        showCurrentValue=True,
                        value=76,
                        max=100,
                        min=0,
                        color="#346beb"
                    )
                ]),
                width=2,
                align='center'
            ),
            dbc.Col(
                dcc.Graph(id='bfi', figure=bfi_compare(SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID)),
                width=5,
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


@callback(
    Output('weekly_routine', 'figure'),
    Input('routine_type', 'value'),
)
def update_weekly_routine(routine_type):
    return weekly_routine([SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID], routine_type)


@callback(
    Output('geographical_scatter', 'figure'),
    Input('routine_type', 'value'),
)
def update_geographical_scatter(routine_type):
    return location_mapbox([SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID], routine_type)
