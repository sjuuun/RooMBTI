import pandas as pd
import plotly.express as px

similarity_df = pd.read_csv("./csv/similarity.csv")

def show_similarity():
    fig = px.bar(similarity_df, x='similarity', y='user_id', text_auto=True, orientation='h', height=1000)
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
    return fig