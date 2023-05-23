import pandas as pd
import plotly.graph_objects as go

bfi_df = pd.read_csv("./csv/bfi.csv")
bfi_columns = ["Openness", "Conscientiousness", "Neuroticism", "Extraversion", "Agreeableness"]


def bfi_single(user_id: str) -> go.Figure:
    df = bfi_df[bfi_df["user_id"] == user_id]
    bfi_fig = go.Figure()
    bfi_fig.add_trace(
        go.Scatterpolar(
            r=df.iloc[0].tolist()[1:6] + [df.iloc[0].tolist()[1]],
            theta=bfi_columns + [bfi_columns[0]],
            # name=f"{self.user_name}"
            name=user_id
        )
    )
    bfi_fig.update_layout(template="simple_white", title="BFI")
    return bfi_fig


def bfi_compare(me_id: str, roommate_id: str) -> go.Figure:
    me_df = bfi_df[bfi_df["user_id"] == me_id]
    roommate_df = bfi_df[bfi_df["user_id"] == roommate_id]

    bfi_fig = go.Figure()
    bfi_fig.add_trace(
        go.Scatterpolar(
            r=me_df.iloc[0].tolist()[1:6] + [me_df.iloc[0].tolist()[1]],
            theta=bfi_columns + [bfi_columns[0]],
            # name=f"{self.user_name}"
            name=me_id
        )
    )
    bfi_fig.add_trace(
        go.Scatterpolar(
            r=roommate_df.iloc[0].tolist()[1:6] + [roommate_df.iloc[0].tolist()[1]],
            theta=bfi_columns + [bfi_columns[0]],
            # name=f"{self.roommate_name}"
            name=roommate_id
        )
    )
    bfi_fig.update_layout(template="simple_white", title="BFI")
    return bfi_fig


if __name__ == "__main__":
    user_id = "P3029"
    roommate_id = "P3030"
    fig = bfi_compare(user_id, roommate_id)
    fig.show()
