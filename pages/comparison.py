

import dash
import dash_daq as daq
from dash import Dash, html, dcc, callback
from dash.dependencies import Input, Output

from pages import Routine
from figures.location_mapbox import location_mapbox, location_mapbox_fake_data
from figures.weekly_routine_timeline import weekly_routine_timeline, weekly_routine_fake_data
from figures import BFI, daily_routine, indoor
from figures.similarity import half_ring_plot
import fake_data


dash.register_page(__name__)

df_user, df_roommate = fake_data.user_and_roommate_data()
fig_bfi = BFI.bfi_fig(df_user[0], df_roommate[0]).fig_cmp
fig_indoor = indoor.indoor_fig(df_user[2], df_roommate[2]).fig_cmp
fig_daily_routine = daily_routine.daily_routine_fig(df_user[1], df_roommate[1]).fig_cmp


layout = html.Div(children=[
    html.H1(children="This is our Comparison page"),

    html.Div(children="""
        This is our Comparison page content.
    """),

    html.Div(children=[
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
        # html.Div(children=[
        #     dcc.Graph(id='similarity', figure=half_ring_plot(180))
        # ]),
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
            dcc.Graph(id="geographical_scatter", figure=location_mapbox(location_mapbox_fake_data())),
            style=dict(float="left"),
        )
    ],
    style={
        'padding': '0rem 0rem 0rem 16rem'
    }
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


@callback(
    Output('geographical_scatter', 'figure'),
    Input('routine_type', 'value'),
)
def update_geographical_scatter(routine_type):
    location_df = location_mapbox_fake_data()
    updated_df = location_df[location_df['type'] == routine_type]
    return location_mapbox(updated_df)
