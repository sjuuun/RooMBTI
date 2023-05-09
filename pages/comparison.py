import dash
from dash import html

dash.register_page(__name__)

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
