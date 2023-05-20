import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, page_registry, page_container

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
                        dbc.Col(dbc.NavbarBrand("RooMBTI")),
                    ],
                    align="center",
                ),
            )
        ]
    ),
    color="dark",
    dark=True,
)

SIDEBAR_STYLE = {
    # "position": "fixed",
    # "top": 0,
    # "left": 0,
    # "bottom": 0,
    "float": "left",
    "width": "16rem",
    "height": "100%",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        # html.H2("", className="display-4"),
        html.P("Compare routines between me and roommate", className="lead"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Overview", href="/", active="exact"),
                dbc.NavLink("Users", href="/users", active="exact"),
                dbc.NavLink("Comparison", href="/comparison", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

app.layout = html.Div(
    [
        html.Header(navbar),
        sidebar,
        page_container,
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
