from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from enum import Enum

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)


# TODO: Interactive radio button
# TODO: Weekly routine
# TODO: Location


class Routine(Enum):
    SLEEP = "Sleeping Time"
    CLASS = "Class Time"
    MEAL = "Meal Time"
    STUDY = "Study Time"
    EXERCISE = "Exercise Time"


# TODO: Styling components as option labels:
# https://dash.plotly.com/dash-core-components/radioitems#styling-components-as-option-labels
app.layout = html.Div(
    dcc.RadioItems(
        options=[
            {"label": Routine.SLEEP.value, "value": Routine.SLEEP.name},
            {"label": Routine.CLASS.value, "value": Routine.CLASS.name},
            {"label": Routine.MEAL.value, "value": Routine.MEAL.name},
            {"label": Routine.STUDY.value, "value": Routine.STUDY.name},
            {"label": Routine.EXERCISE.value, "value": Routine.EXERCISE.name},
        ],
        value=Routine.SLEEP.name,
        inline=True,
        clearable=False,
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
