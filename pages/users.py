import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

from figures.similarity_barchart import show_similarity

dash.register_page(__name__, title="RooMBTI")

layout = html.Div(children=[
    html.H1(children="Users"),

    html.Div(children="""
        Choose roommate.
    """),
    dbc.Container(
        dcc.Graph(id="similarity_barchart", figure=show_similarity())
    ),
])
