import dash
from dash import html

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children="This is our Users page"),

    html.Div(children="""
        This is our Users page content.
    """),

])
