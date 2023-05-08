import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import fake_data

#bfi_columns = ['Openness', 'Conscientiousness', 'Neuroticism', 'Extraversion', 'Agreeableness', 'user']

class bfi_fig:
    def __init__(self, userdata, roommatedata):
        self.user_df = userdata
        self.roommate_df = roommatedata
        self.fig = self.make_fig()
    

    def make_fig(self):
        bfi_fig = go.Figure()
        bfi_fig.add_trace(go.Scatterpolar(r=self.user_df.iloc[0].tolist()[0:5]+[self.user_df.iloc[0].tolist()[0]], theta=fake_data.bfi_columns+[fake_data.bfi_columns[0]], name='User' ))
        bfi_fig.add_trace(go.Scatterpolar(r=self.roommate_df.iloc[0].tolist()[0:5]+[self.roommate_df.iloc[0].tolist()[0]], theta=fake_data.bfi_columns+[fake_data.bfi_columns[0]], name='Roommate' ))
        bfi_fig.update_layout(template='simple_white')
        return bfi_fig


if __name__ == '__main__':
    df_user, df_roommate = fake_data.user_and_roommate_data()
    bfi = bfi_fig(df_user[0], df_roommate[0])
    bfi.fig.show()

