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
    if routine_type:
        df = df[df["routine"] == routine_type]

    fig = make_subplots(rows=7, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    timeline_figs = []
    for i in range(7):
        timeline_figs.append(
            px.timeline(df[df["weekday"] == i], x_start="start_at", x_end="end_at", y="user_id", color="user_id")
        )

    for i in range(7):
        f = timeline_figs[i]
        show_legend = True if i == 0 else False
        for j in range(len(f.data)):
            fig.add_trace(go.Bar(f.data[j], showlegend=show_legend), row=(i + 1), col=1)

    fig.update_yaxes(title="Mon", row=1, col=1)
    fig.update_yaxes(title="Tue", row=2, col=1)
    fig.update_yaxes(title="Wed", row=3, col=1)
    fig.update_yaxes(title="Thr", row=4, col=1)
    fig.update_yaxes(title="Fri", row=5, col=1)
    fig.update_yaxes(title="Sat", row=6, col=1)
    fig.update_yaxes(title="Sun", row=7, col=1)

    fig.update_xaxes(tickformat="%H:%M", range=["1900-01-01 00:00:00", "1900-01-02 00:00:00"])
    fig.update_layout(title="Weekly Routine")

    fig.update_xaxes(type="date")

    fig.update_layout(width=700, height=600)

    return fig
