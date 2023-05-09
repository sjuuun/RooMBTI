from enum import Enum

import dash
from dash import callback, html, dcc
from dash.dependencies import Input, Output

from figures.location_mapbox import location_mapbox, location_mapbox_fake_my_data
from figures.weekly_routine_timeline import weekly_routine_timeline, weekly_routine_fake_my_data

dash.register_page(__name__, path="/")


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
