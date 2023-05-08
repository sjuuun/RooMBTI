from enum import Enum

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
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


def weekly_routine_timeline(df: pd.DataFrame) -> go.Figure:
    fig = make_subplots(rows=7, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    fig_mon = px.timeline(df[df["weekday"] == 0], x_start="start", x_end="end", y="user_id")
    fig_tue = px.timeline(df[df["weekday"] == 1], x_start="start", x_end="end", y="user_id")
    fig_wed = px.timeline(df[df["weekday"] == 2], x_start="start", x_end="end", y="user_id")
    fig_thr = px.timeline(df[df["weekday"] == 3], x_start="start", x_end="end", y="user_id")
    fig_fri = px.timeline(df[df["weekday"] == 4], x_start="start", x_end="end", y="user_id")
    fig_sat = px.timeline(df[df["weekday"] == 5], x_start="start", x_end="end", y="user_id")
    fig_sun = px.timeline(df[df["weekday"] == 6], x_start="start", x_end="end", y="user_id")

    fig.add_trace(go.Bar(fig_mon.data[0]), row=1, col=1)
    fig.add_trace(go.Bar(fig_tue.data[0]), row=2, col=1)
    fig.add_trace(go.Bar(fig_wed.data[0]), row=3, col=1)
    fig.add_trace(go.Bar(fig_thr.data[0]), row=4, col=1)
    fig.add_trace(go.Bar(fig_fri.data[0]), row=5, col=1)
    fig.add_trace(go.Bar(fig_sat.data[0]), row=6, col=1)
    fig.add_trace(go.Bar(fig_sun.data[0]), row=7, col=1)

    fig.update_xaxes(type='date')

    return fig


def location_scatter_mapbox(df: pd.DataFrame) -> go.Figure:
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        hover_name="type",
        hover_data=["latitude", "longitude"],
        zoom=3,
        width=500,
        height=500
    )
    fig.update_layout(mapbox_style="streets")
    fig.update_layout(mapbox_bounds={"west": 127.35, "east": 127.37, "south": 36.36, "north": 36.38})

    return fig


location_df = pd.read_csv("csv/sample_location.csv")
px.set_mapbox_access_token(open(".mapbox_token").read())

location_fig = location_scatter_mapbox(location_df)

weekly_df = pd.DataFrame()
for i in range(7):
    _df = pd.DataFrame([
        dict(type="SLEEP", user_id="Me", weekday=i, start="1970-01-01 00:00:00", end="1970-01-01 09:42:00"),
        dict(type="SLEEP", user_id="Me", weekday=i, start="1970-01-01 23:10:00", end="1970-01-01 23:59:59"),
        dict(type="CLASS", user_id="Me", weekday=i, start="1970-01-01 10:07:00", end="1970-01-01 11:42:00"),
        dict(type="MEAL", user_id="Me", weekday=i, start="1970-01-01 12:20:00", end="1970-01-01 13:07:00"),
        dict(type="SLEEP", user_id="Roommate", weekday=i, start="1970-01-01 02:00:00", end="1970-01-01 11:42:00"),
        dict(type="CLASS", user_id="Roommate", weekday=i, start="1970-01-01 12:55:00", end="1970-01-01 15:02:00"),
    ])
    weekly_df = pd.concat([weekly_df, _df])

weekly_fig = weekly_routine_timeline(weekly_df)

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
        html.Div(
            dcc.Graph(id="weekly_routine", figure=weekly_fig)
        )
    ]
)


@app.callback(
    Output('geographical_scatter', 'figure'),
    Input('routine_type', 'value'),
)
def update_geographical_scatter(routine_type):
    updated_df = location_df[location_df['type'] == routine_type]
    return location_scatter_mapbox(updated_df)


@app.callback(
    Output('weekly_routine', 'figure'),
    Input('routine_type', 'value'),
)
def update_weekly_routine(routine_type):
    updated_df = weekly_df[weekly_df["type"] == routine_type]
    return weekly_routine_timeline(updated_df)


if __name__ == '__main__':
    app.run_server(debug=True)
