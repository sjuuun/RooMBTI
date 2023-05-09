from enum import Enum

import dash
from dash import callback, html, dcc
from dash.dependencies import Input, Output

from figures.weekly_routine_timeline import weekly_routine_timeline, weekly_routine_fake_data

dash.register_page(__name__)


class Routine(Enum):
    SLEEP = "Sleeping Time"
    CLASS = "Class Time"
    MEAL = "Meal Time"
    STUDY = "Study Time"
    EXERCISE = "Exercise Time"


layout = html.Div(children=[
    html.H1(children="This is our Comparison page"),

    html.Div(children="""
        This is our Comparison page content.
    """),

    html.Div(
        """
        This is for similarity, BFI, Indoor
        """
    ),

    html.Div(
        """
        This is for Daily Routine
        """
    ),

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

    html.Div(
        dcc.Graph(id="weekly_routine", figure=weekly_routine_timeline(weekly_routine_fake_data())),
        style=dict(float="left"),
    ),

    html.Div(
        """
        This is for Location
        """
    )
])


@callback(
    Output('weekly_routine', 'figure'),
    Input('routine_type', 'value'),
)
def update_weekly_routine(routine_type):
    weekly_df = weekly_routine_fake_data()
    updated_df = weekly_df[weekly_df["type"] == routine_type]
    return weekly_routine_timeline(updated_df)
