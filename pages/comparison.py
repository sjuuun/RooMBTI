import dash
from dash import Dash, html, dcc
from figures import BFI, daily_routine, indoor
import fake_data


dash.register_page(__name__)

df_user, df_roommate = fake_data.user_and_roommate_data()
fig_bfi = BFI.bfi_fig(df_user[0], df_roommate[0]).fig
fig_indoor = indoor.indoor_fig(df_user[2], df_roommate[2]).fig
fig_daily_routine = daily_routine.daily_routine_fig(df_user[1], df_roommate[1]).fig

layout = html.Div(children=[
    html.H1(children="This is our Comparison page"),

    html.Div(children="""
        This is our Comparison page content.
    """),

    html.Div(
        children=[
            dcc.Graph(
                id='example-graph1',
                figure=fig_bfi
            ),
            dcc.Graph(
                id='example-graph2',
                figure=fig_indoor
            ),
            dcc.Graph(
                id='example-graph3',
                figure=fig_daily_routine
        )]
    ),

    html.Div(
        """
        This is for Daily Routine
        """
    ),

    html.Div(
        """
        This is for radio Item
        """
    ),

    html.Div(
        """
        This is for Weekly Routine
        """
    ),

    html.Div(
        """
        This is for Location
        """
    )
])
