import pandas as pd
import plotly.express as px

similarity_df = pd.read_csv("./csv/similarity.csv")


def show_similarity():
    fig = px.bar(similarity_df,
                x='similarity',
                y='user_id',
                text_auto=True,
                orientation='h',
                height=800,
                labels={
                    'user_id': 'user'
                },
                title="Routine similarity among users")
    fig.update_xaxes(range=[0, 1])
    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    for _, r in similarity_df.iterrows():
        fig.add_annotation(
            {
                'x': r['similarity'],
                'y': r['user_id'],
                'text': f"<a href='/comparison?roommate_id={r['user_id']}' target='_self'>{r['user_id']}</a>",
                'showarrow': False,
                'xshift': 30
            }
        )
    return fig