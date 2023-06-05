import dash_bootstrap_components as dbc
from dash import Dash, html, page_container

external_stylesheets = [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME]
app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)
server = app.server

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.I(className="fa-solid fa-people-roof", style=dict(color="#FFFFFF"))),
                        dbc.Col(dbc.NavbarBrand("RooMBTI", href="/")),
                        dbc.Col(
                            dbc.Nav(
                                [
                                    dbc.NavLink("Overview", href="/", active="exact", style=dict(color="#FFFFFF")),
                                    dbc.NavLink("Users", href="/users", active="exact", style=dict(color="#FFFFFF")),
                                    dbc.NavLink("Comparison", href="/comparison", active="exact",
                                                        style=dict(color="#FFFFFF")),
                                ],
                                pills=True
                            )
                        )
                    ],
                    align="center",
                ),
            )
        ]
    ),
    color="dark",
    dark=True,
)

app.layout = html.Div(
    [
        navbar,
        dbc.Container(
            dbc.Row(page_container)
        )
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
