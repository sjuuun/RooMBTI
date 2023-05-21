import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import fake_data

bfi_df = pd.read_csv("./csv/bfi.csv")
bfi_columns = ['Openness', 'Conscientiousness', 'Neuroticism', 'Extraversion', 'Agreeableness']

class bfi_fig:
    def __init__(self, user, roommate=pd.DataFrame()):
        self.user_df = user
        self.roommate_df = roommate
        # self.user_name = user['user_id']
        # self.roommate_name = roommate['user_id']
        if not roommate.empty:
            self.fig_cmp = self.make_fig_compare()
        self.fig = self.make_fig()
    
    def make_fig(self):
        bfi_fig = go.Figure()
        bfi_fig.add_trace(
            go.Scatterpolar(
                r=self.user_df.iloc[0].tolist()[1:6] + [self.user_df.iloc[0].tolist()[1]],
                theta=bfi_columns + [bfi_columns[0]],
                # name=f"{self.user_name}"
                name="P3029"
            )
        )
        bfi_fig.update_layout(template='simple_white', width=500, height=500, title="BFI")
        return bfi_fig

    def make_fig_compare(self):
        bfi_fig = go.Figure()
        bfi_fig.add_trace(
            go.Scatterpolar(
                r=self.user_df.iloc[0].tolist()[1:6] + [self.user_df.iloc[0].tolist()[1]],
                theta=bfi_columns + [bfi_columns[0]],
                # name=f"{self.user_name}"
                name="P3029"
            )
        )
        bfi_fig.add_trace(
            go.Scatterpolar(
                r=self.roommate_df.iloc[0].tolist()[1:6] + [self.roommate_df.iloc[0].tolist()[1]],
                theta=bfi_columns + [bfi_columns[0]],
                # name=f"{self.roommate_name}"
                name="P3030"
            )
        )
        bfi_fig.update_layout(template='simple_white', width=500, height=500, title="BFI")
        return bfi_fig


if __name__ == '__main__':
    user_df = bfi_df[bfi_df['user_id']=='P3029']
    roommate_df = bfi_df[bfi_df['user_id']=='P3030']
    bfi = bfi_fig(user_df, roommate_df)
    bfi.fig.show()

