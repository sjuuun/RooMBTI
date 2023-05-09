import dash
from dash import html, dcc
import plotly.express as px
import dash_daq as daq
import pandas as pd
import random

# make a nickname for a user
def make_nickname():
    letters = ['a', 'b', 'c', 'd', 'e', 'f',
              'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x',
              'y', 'z', '0', '1', '2', '3',
              '4', '5', '6', '7', '8', '9']
    nickname = ''
    nickname_limit_length = random.randint(5, 10)
    for _ in range(nickname_limit_length):
        nickname += letters[random.randint(0, 35)]
    # print(f'nickname is {nickname}')
    return nickname

id_list = [i for i in range(50)]
user_list = [make_nickname() for _ in range(50)]
similarity_list = [round(random.random(), 4)*100 for _ in range(50)]

user_df = pd.DataFrame({'id': id_list, 'user': user_list, 'similarity': similarity_list})
# print(user_df.head())

fig = px.bar(user_df, x='similarity', y='user', text_auto=True, orientation='h', height=1000)
fig.update_layout(yaxis={'categoryorder': 'total ascending'})
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["type", "bar"],
                    label="Ascending order",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Descending order",
                    method="restyle"
                )
            ]),
            direction="down",
            pad={"r": 10, "t":10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)
fig.update_layout(
    annotations=[
        dict(
            text="Order",
            showarrow=False,
            x=0,
            y=1.085,
            yref="paper",
            align="left"
        )
    ]
)

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1(children="This is our Users page"),

    html.Div(children="""
        This is our Users page content.
    """),
    html.Div(
        dcc.Graph(id="similarity_barchart", figure=fig),
        style=dict(float="left"),
    ),
])
