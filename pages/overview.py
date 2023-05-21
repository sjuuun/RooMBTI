import dash
import dash_bootstrap_components as dbc
from dash import callback, html, dcc
from dash.dependencies import Input, Output

import fake_data
from figures import daily_routine, indoor
from figures.bfi import bfi_single
from figures.location_mapbox import location_mapbox
from figures.weekly_routine import weekly_routine
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
                dbc.Row(
                    html.Div(
                        id='matched',
                        children=[html.H3("Matched"), html.H4("9/40")],
                        style={
                            'float': 'left',
                            'margin': '20px',
                            'width': '200px',
                            'height': '90px',
                            'text-align': 'center',
                            'border-style': 'solid',
                            'border-color': '#eeeee4'
                        }
                    )
                ),
                dbc.Row(
                    html.Div(id='top3', children=[
                        html.H3("Top 3 Users"),
                        html.Div(id='user figures', children=[
                            html.Img(
                                src="https://e7.pngegg.com/pngimages/84/165/png-clipart-united-states-avatar-organization-information-user-avatar-service-computer-wallpaper.png",
                                style={
                                    'width': '25%',
                                    'heigh': '25%',
                                }
                            ),
                            html.Img(
                                src="https://e7.pngegg.com/pngimages/84/165/png-clipart-united-states-avatar-organization-information-user-avatar-service-computer-wallpaper.png",
                                style={
                                    'width': '25%',
                                    'heigh': '25%',
                                }
                            ),
                            html.Img(
                                src="https://e7.pngegg.com/pngimages/84/165/png-clipart-united-states-avatar-organization-information-user-avatar-service-computer-wallpaper.png",
                                style={
                                    'width': '25%',
                                    'heigh': '25%',
                                }
                            )
                        ],
                        style={'float': 'left'}),
                    ],
                    style={
                        'float': 'left',
                        'margin': '20px',
                        'width': '200px',
                        'height': '90px',
                        'text-align': 'center',
                        'border-style': 'solid',
                        'border-color': '#eeeee4'
                    })
                )
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
