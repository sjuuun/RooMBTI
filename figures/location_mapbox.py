import glob
from typing import List

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

COLOR_MAP = {"You": "#1F77B4", "Roommate": "#FF7F0E"}


def get_location_data():
    location_files = glob.glob("csv/routines_raw/*-location.csv")
    return pd.concat([pd.read_csv(f) for f in location_files])


location_df = get_location_data()


def location_mapbox(user_ids: List[str], routine_type: str = None) -> go.Figure:
    df = location_df.loc[location_df["user_id"].isin(user_ids)]
    df = df.replace(user_ids[0], "You")
    if len(user_ids) == 2:
        df = df.replace(user_ids[1], "Roommate")
    if routine_type:
        routine_type = routine_type if routine_type != "SLEEP" else "INDOOR"
        df = df[df["routine"] == routine_type]

    px.set_mapbox_access_token(open(".mapbox_token").read())
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="user_id",
        hover_name="routine",
        hover_data=["latitude", "longitude"],
        zoom=3,
        width=500,
        height=600,
        color_discrete_map=COLOR_MAP,
    )
    fig.update_layout(title="Location", mapbox_style="streets")
    fig.update_layout(mapbox_bounds={"west": 127.35, "east": 127.37, "south": 36.36, "north": 36.38})

    return fig
