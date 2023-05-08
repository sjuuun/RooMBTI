from dash import Dash, html, dcc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import fake_data
import BFI
import daily_routine
import indoor

app = Dash(__name__)

df_user, df_roommate = fake_data.user_and_roommate_data()
fig_bfi = BFI.bfi_fig(df_user[0], df_roommate[0]).fig
fig_indoor = indoor.indoor_fig(df_user[2], df_roommate[2]).fig
fig_daily_routine = daily_routine.daily_routine_fig(df_user[1], df_roommate[1]).fig


app.layout = html.Div(children=[
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
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)