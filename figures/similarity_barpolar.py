import pandas as pd
import plotly.graph_objs as go

similarity_df = pd.read_csv(f'csv/similarity.csv')


def half_ring_plot(roommate_id):
    percentage = similarity_df[similarity_df['user_id'] == roommate_id]['similarity'].values[0]
    percentage *= 100

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=percentage,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100]}
        },
        title={'text': "Similarity"}
    ))
    return fig