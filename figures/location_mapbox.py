import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def location_mapbox_fake_data() -> pd.DataFrame:
    return pd.read_csv("csv/sample_location.csv")


def location_mapbox(df: pd.DataFrame) -> go.Figure:
    px.set_mapbox_access_token(open(".mapbox_token").read())
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="user_id",
        hover_name="type",
        hover_data=["latitude", "longitude"],
        zoom=3,
        width=600,
        height=600
    )
    fig.update_layout(title="Location", mapbox_style="streets")
    fig.update_layout(mapbox_bounds={"west": 127.35, "east": 127.37, "south": 36.36, "north": 36.38})

    return fig
