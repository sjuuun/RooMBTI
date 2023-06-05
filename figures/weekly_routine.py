from typing import List

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def get_weekly_routine_data():
    df = pd.read_csv("./csv/weekly_routines.csv")
    df = df[df["routine"] != "INDOOR"]
    df["start_at"] = pd.to_datetime(df['start_at'], format='%H:%M:%S')
    df["end_at"] = df["start_at"] + pd.Timedelta(minutes=15)

    return df


weekly_df = get_weekly_routine_data()


def weekly_routine(user_ids: List[str], routine_type: str = None) -> go.Figure:
    df = weekly_df.loc[weekly_df["user_id"].isin(user_ids)]
    df = df.replace(user_ids[0], "You")
    if len(user_ids) == 2:
        df = df.replace(user_ids[1], "Roommate")
    if routine_type:
        df = df[df["routine"] == routine_type]
    df = df.sort_values(by='user_id', ascending=False)
    fig = make_subplots(rows=7, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    timeline_figs = []
    for i in range(7):
        w_df = df[df["weekday"] == i]
        if w_df.empty and len(user_ids) == 1:
            w_df = df.head(1)
            w_df['end_at'] = w_df['start_at']
        if w_df.empty and len(user_ids) == 2:
            filtered_user_ids = list(w_df['user_id'].unique())
            for u in ['You', 'Roommate']:
                if u not in filtered_user_ids:
                    w_df = pd.concat([w_df, pd.DataFrame({'user_id': [u], 'start_at': ['1900-01-01 00:00:00'], 'end_at': ['1900-01-01 00:00:00'], 'weekday': [i], 'routine': [routine_type]})], ignore_index=True)

        timeline_figs.append(
            px.timeline(w_df, x_start="start_at", x_end="end_at", y="user_id", color="user_id", category_orders={"user_id": ["You", "Roommate"]})
        )

    for i in range(7):
        f = timeline_figs[i]
        show_legend = True if i == 0 else False
        for j in range(len(f.data)):
            fig.add_trace(go.Bar(f.data[j], showlegend=show_legend), row=(i + 1), col=1)

    fig.update_yaxes(title="Mon", row=1, col=1, categoryorder='category ascending')
    fig.update_yaxes(title="Tue", row=2, col=1, categoryorder='category ascending')
    fig.update_yaxes(title="Wed", row=3, col=1, categoryorder='category ascending')
    fig.update_yaxes(title="Thr", row=4, col=1, categoryorder='category ascending')
    fig.update_yaxes(title="Fri", row=5, col=1, categoryorder='category ascending')
    fig.update_yaxes(title="Sat", row=6, col=1, categoryorder='category ascending')
    fig.update_yaxes(title="Sun", row=7, col=1, categoryorder='category ascending')

    fig.update_xaxes(tickformat="%H:%M", range=["1900-01-01 00:00:00", "1900-01-02 00:00:00"])
    fig.update_layout(title="Weekly Routine", template="simple_white")

    fig.update_xaxes(type="date")

    fig.update_layout(width=700, height=600)

    return fig
