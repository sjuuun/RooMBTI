import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def weekly_routine_fake_data() -> pd.DataFrame:
    weekly_df = pd.DataFrame()
    for i in range(7):
        _df = pd.DataFrame([
            dict(type="SLEEP", user_id="Me", weekday=i, start="1970-01-01 00:00:00", end="1970-01-01 09:42:00"),
            dict(type="SLEEP", user_id="Me", weekday=i, start="1970-01-01 23:10:00", end="1970-01-01 23:59:59"),
            dict(type="CLASS", user_id="Me", weekday=i, start="1970-01-01 10:07:00", end="1970-01-01 11:42:00"),
            dict(type="MEAL", user_id="Me", weekday=i, start="1970-01-01 12:20:00", end="1970-01-01 13:07:00"),
            dict(type="STUDY", user_id="Me", weekday=i, start="1970-01-01 19:20:00", end="1970-01-01 21:07:00"),
            dict(type="EXERCISE", user_id="Me", weekday=i, start="1970-01-01 21:30:00", end="1970-01-01 22:47:00"),
            dict(type="SLEEP", user_id="Roommate", weekday=i, start="1970-01-01 02:00:00", end="1970-01-01 11:42:00"),
            dict(type="CLASS", user_id="Roommate", weekday=i, start="1970-01-01 12:55:00", end="1970-01-01 15:02:00"),
            dict(type="MEAL", user_id="Roommate", weekday=i, start="1970-01-01 17:20:00", end="1970-01-01 18:07:00"),
            dict(type="STUDY", user_id="Roommate", weekday=i, start="1970-01-01 20:20:00", end="1970-01-01 21:35:00"),
            dict(type="EXERCISE", user_id="Roommate", weekday=i, start="1970-01-01 16:01:00",
                 end="1970-01-01 16:54:00"),
        ])
        weekly_df = pd.concat([weekly_df, _df])

    return weekly_df


def weekly_routine_fake_my_data() -> pd.DataFrame:
    weekly_df = weekly_routine_fake_data()
    return weekly_df[weekly_df["user_id"] == "Me"]


def weekly_routine_timeline(df: pd.DataFrame) -> go.Figure:
    fig = make_subplots(rows=7, cols=1, shared_xaxes=True, vertical_spacing=0.02)
    timeline_figs = []
    for i in range(7):
        timeline_figs.append(
            px.timeline(df[df["weekday"] == i], x_start="start", x_end="end", y="user_id", color="user_id")
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

    fig.update_xaxes(tickformat="%H:%M")
    fig.update_layout(title="Weekly Routine")

    fig.update_xaxes(type="date")

    fig.update_layout(width=700, height=600)

    return fig
