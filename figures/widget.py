import pandas as pd

import dash_bootstrap_components as dbc
from dash import html


def matched() -> dbc.Card:
    return dbc.Card(
        dbc.CardBody([
            html.H3("Matched"),
            dbc.CardLink("9 / 40", href="/users"),
        ]),
        style={"text-align": "center"}
    )
# style = {
#         'float': 'left',
#         'margin': '20px',
#         'width': '200px',
#         'height': '90px',
#         'text-align': 'center',
#         'border-style': 'solid',
#         'border-color': '#eeeee4'
#     }


def top_3() -> dbc.Card:
    return dbc.Card(
        dbc.CardBody([
            html.H3("Top 3 Users"),
            dbc.Row(
                dbc.Col([
                    dbc.NavLink(className="fa-solid fa-person fa-2xl", href="/comparison", active="exact"),
                    dbc.NavLink(className="fa-solid fa-person fa-2xl", href="/comparison", active="exact"),
                    dbc.NavLink(className="fa-solid fa-person fa-2xl", href="/comparison", active="exact")
                ])
            )
        ]),
        style={"text-align": "center"}
    )
# html.Div(id='top3', children=[
#     html.H3("Top 3 Users"),
#     html.Div(id='user figures', children=[
#         html.Img(
#             src="https://e7.pngegg.com/pngimages/84/165/png-clipart-united-states-avatar-organization-information-user-avatar-service-computer-wallpaper.png",
#             style={
#                 'width': '25%',
#                 'heigh': '25%',
#             }
#         ),
#         html.Img(
#             src="https://e7.pngegg.com/pngimages/84/165/png-clipart-united-states-avatar-organization-information-user-avatar-service-computer-wallpaper.png",
#             style={
#                 'width': '25%',
#                 'heigh': '25%',
#             }
#         ),
#         html.Img(
#             src="https://e7.pngegg.com/pngimages/84/165/png-clipart-united-states-avatar-organization-information-user-avatar-service-computer-wallpaper.png",
#             style={
#                 'width': '25%',
#                 'heigh': '25%',
#             }
#         )
#     ],
#     style={'float': 'left'}),
# ],
# style={
#     'float': 'left',
#     'margin': '20px',
#     'width': '200px',
#     'height': '90px',
#     'text-align': 'center',
#     'border-style': 'solid',
#     'border-color': '#eeeee4'
# })
