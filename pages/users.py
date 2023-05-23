import random

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import html, dcc
from figures.similarity_barchart import show_similarity

fig = show_similarity()

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children="Users"),

    html.Div(children="""
        Choose roommate.
    """),
    dbc.Container(
        dcc.Graph(id="similarity_barchart", figure=fig)
    ),
])
