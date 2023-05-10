from enum import Enum

import dash
from dash import callback, html, dcc
from dash.dependencies import Input, Output

from figures.location_mapbox import location_mapbox, location_mapbox_fake_my_data
from figures.weekly_routine_timeline import weekly_routine_timeline, weekly_routine_fake_my_data

from figures import BFI, daily_routine, indoor
import fake_data

dash.register_page(__name__, path="/")


df_user, df_roommate = fake_data.user_and_roommate_data()
fig_bfi = BFI.bfi_fig(df_user[0]).fig
fig_indoor = indoor.indoor_fig(df_user[2]).fig
fig_daily_routine = daily_routine.daily_routine_fig(df_user[1]).fig


class Routine(Enum):
    SLEEP = "Sleeping Time"
    CLASS = "Class Time"
    MEAL = "Meal Time"
    STUDY = "Study Time"
    EXERCISE = "Exercise Time"


layout = html.Div(children=[
    html.H1(children="This is our Overview page"),

    html.Div(children="""
        This is our Overview page content.
    """),
    html.Div(children=[
        html.Div(id='matched', children=[
            html.H3("Matched"),
            html.H4("9/40"),
        ],
        style={
            'float': 'left',
            'margin': '20px',
            'height': '90px',
            'text-align': 'center',
            'border-style': 'solid',
            'border-color': '#eeeee4'
        }),
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
                ),
            ],
            style={
                'float': 'left'
            }
            ),
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
        ]
    ),
    html.Div(children=[
        html.Div(children=[
            html.Div(dcc.Graph(id='bfi',figure=fig_bfi))
            ],
        ),
        html.Div(children=[
            dcc.Graph(id='indoor',figure=fig_indoor),
            ],
        ),

        ],
        style={
            'float': 'initial',
            'display': 'flex'
        }
    ),

    html.Div(children=[
        dcc.Graph(id='daily_routine',figure=fig_daily_routine),
        ],
        style={
            'padding': '0rem 0rem 0rem 16rem'
        }
    ),


    html.Div(children=[
        html.Div(
            html.Div(
                dcc.RadioItems(
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

        html.Div(
            dcc.Graph(id="my_weekly_routine", figure=weekly_routine_timeline(weekly_routine_fake_my_data())),
            style=dict(float="left"),
        ),

        html.Div(
            dcc.Graph(id="my_geographical_scatter", figure=location_mapbox(location_mapbox_fake_my_data())),
            style=dict(float="left"),
        )],
        style={
            'padding': '0rem 0rem 0rem 16rem'
        }
    )
])


@callback(
    Output('my_weekly_routine', 'figure'),
    Input('my_routine_type', 'value'),
)
def update_weekly_routine(routine_type):
    weekly_df = weekly_routine_fake_my_data()
    updated_df = weekly_df[weekly_df["type"] == routine_type]
    return weekly_routine_timeline(updated_df)


@callback(
    Output('my_geographical_scatter', 'figure'),
    Input('my_routine_type', 'value'),
)
def update_geographical_scatter(routine_type):
    location_df = location_mapbox_fake_my_data()
    updated_df = location_df[location_df['type'] == routine_type]
    return location_mapbox(updated_df)
