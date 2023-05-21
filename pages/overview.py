import dash
import dash_bootstrap_components as dbc
from dash import callback, html, dcc
from dash.dependencies import Input, Output

import fake_data
from figures import daily_routine, indoor
from figures.bfi import bfi_single
from figures.location_mapbox import location_mapbox
from figures.weekly_routine import weekly_routine
from figures.widget import matched, top_3
from pages import Routine, SAMPLE_ME_ID

dash.register_page(__name__, path="/")

df_user, df_roommate = fake_data.user_and_roommate_data()

layout = html.Div(children=[
    html.H1(children="Overview"),

    html.Div(children="""
        Analyze your routines.
    """),

    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.Row(matched()),
                dbc.Row(top_3())
            ]),
            dbc.Col(
                dcc.Graph(id='bfi', figure=bfi_single(SAMPLE_ME_ID))
            ),
            dbc.Col(
                dcc.Graph(id='indoor', figure=indoor.indoor(SAMPLE_ME_ID))
            ),
        ]),
        dbc.Row(
            dcc.Graph(id='daily_routine', figure=daily_routine.daily_routine(SAMPLE_ME_ID))
        ),
        dbc.Row([
            html.Div(
                html.Div(
                    dbc.RadioItems(
                        id="my_routine_type",
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
                dcc.Graph(id="my_weekly_routine", figure=weekly_routine([SAMPLE_ME_ID]))
            ),
            dbc.Col(
                dcc.Graph(id="my_geographical_scatter", figure=location_mapbox([SAMPLE_ME_ID]))
            ),
        ]),
    ]),
])


@callback(
    Output('my_weekly_routine', 'figure'),
    Input('my_routine_type', 'value'),
)
def update_weekly_routine(routine_type):
    return weekly_routine([SAMPLE_ME_ID], routine_type)


@callback(
    Output('my_geographical_scatter', 'figure'),
    Input('my_routine_type', 'value'),
)
def update_geographical_scatter(routine_type):
    return location_mapbox([SAMPLE_ME_ID], routine_type)
