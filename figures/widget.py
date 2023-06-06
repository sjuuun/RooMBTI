import dash_bootstrap_components as dbc
from dash import html


def matched() -> dbc.Card:
    return dbc.Card(
        dbc.CardBody([
            html.H3("Matched"),
            dbc.CardLink("4 / 10", href="/users"),
        ]),
        style={"text-align": "center"}
    )


def top_3() -> dbc.Card:
    return dbc.Card(
        dbc.CardBody([
            html.H3("Top 3 Users"),
            dbc.Row(
                dbc.Col([
                    dbc.CardLink("P3023", href="/comparison?roommate_id=P3023"),
                    dbc.CardLink("P3021", href="/comparison?roommate_id=P3021"),
                    dbc.CardLink("P3027", href="/comparison?roommate_id=P3027")
                ])
            )
        ]),
        style={"text-align": "center"}
    )
