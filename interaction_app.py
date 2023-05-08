from enum import Enum

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets)


class Routine(Enum):
    SLEEP = "Sleeping Time"
    CLASS = "Class Time"
    MEAL = "Meal Time"
    STUDY = "Study Time"
    EXERCISE = "Exercise Time"


location_df = pd.read_csv("csv/sample_location.csv")
px.set_mapbox_access_token(open(".mapbox_token").read())

location_fig = px.scatter_mapbox(
    location_df,
    lat="latitude",
    lon="longitude",
    hover_name="type",
    hover_data=["latitude", "longitude"],
    zoom=3,
    width=500,
    height=500
)
location_fig.update_layout(mapbox_style="streets")
location_fig.update_layout(mapbox_bounds={"west": 127.35, "east": 127.37, "south": 36.36, "north": 36.38})

# TODO: Styling components as option labels:
# https://dash.plotly.com/dash-core-components/radioitems#styling-components-as-option-labels
app.layout = html.Div(
    [
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
        ),
        html.Div(
            dcc.Graph(id="geographical_scatter", figure=location_fig)
        ),
    ]
)

@app.callback(
    Output('geographical_scatter', 'figure'),
    Input('routine_type', 'value'),
)
def update_geographical_scatter(routine_type):
    updated_df = location_df[location_df['type'] == routine_type]
    updated_location_fig = px.scatter_mapbox(
        updated_df,
        lat="latitude",
        lon="longitude",
        hover_name="type",
        hover_data=["latitude", "longitude"],
        zoom=3,
        width=500,
        height=500
    )
    updated_location_fig.update_layout(mapbox_style="streets")
    updated_location_fig.update_layout(mapbox_bounds={"west": 127.35, "east": 127.37, "south": 36.36, "north": 36.38})
    return updated_location_fig


if __name__ == '__main__':
    app.run_server(debug=True)
