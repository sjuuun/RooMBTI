import dash
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import html, dcc, callback
from dash.dependencies import Input, Output

import fake_data
from figures import daily_routine, indoor
from figures.bfi import bfi_compare
from figures.location_mapbox import location_mapbox, location_mapbox_fake_data
from figures.weekly_routine_timeline import weekly_routine_timeline, weekly_routine_fake_data
from pages import Routine, SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID

dash.register_page(__name__)

df_user, df_roommate = fake_data.user_and_roommate_data()
fig_indoor = indoor.indoor_fig(df_user[2], df_roommate[2]).fig_cmp

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
                ])
            ),
            dbc.Col(
                dcc.Graph(id='bfi', figure=bfi_compare(SAMPLE_ME_ID, SAMPLE_ROOMMATE_ID))
            ),
            dbc.Col(
                dcc.Graph(id='indoor', figure=fig_indoor)
            ),
        ]),
        dbc.Row(
            dcc.Graph(id='daily_routine', figure=daily_routine.daily_routine_compare("P3029", "P3030"))
        ),
        dbc.Row([
            html.Div(
                html.Div(
                    dcc.RadioItems(
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
                dcc.Graph(id="weekly_routine", figure=weekly_routine_timeline(weekly_routine_fake_data()))
            ),
            dbc.Col(
                dcc.Graph(id="geographical_scatter", figure=location_mapbox(location_mapbox_fake_data()))
            )
        ]),
    ]),
])


@callback(
    Output('weekly_routine', 'figure'),
    Input('routine_type', 'value'),
)
def update_weekly_routine(routine_type):
    weekly_df = weekly_routine_fake_data()
    updated_df = weekly_df[weekly_df["type"] == routine_type]
    return weekly_routine_timeline(updated_df)


@callback(
    Output('geographical_scatter', 'figure'),
    Input('routine_type', 'value'),
)
def update_geographical_scatter(routine_type):
    location_df = location_mapbox_fake_data()
    updated_df = location_df[location_df['type'] == routine_type]
    return location_mapbox(updated_df)
