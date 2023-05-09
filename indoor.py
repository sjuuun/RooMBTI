import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import fake_data

#indoor_columns = ['timestamp', 'IndoorRatio', 'user']

class indoor_fig:
    def __init__(self, userdata, roommatedata):
        self.user_df = userdata
        self.roommate_df = roommatedata
        self.fig = self.make_fig()

    def make_fig(self):
        indoor_fig = go.Figure(data=[
                      go.Scatter(x=self.user_df.timestamp, y=self.user_df.IndoorRatio, mode='lines', name='User', line_shape='spline'),
                      go.Scatter(x=self.roommate_df.timestamp, y=self.roommate_df.IndoorRatio, mode='lines' , name='Roommate', line_shape='spline')
                      ])
        indoor_fig.update_layout(template='simple_white')
        indoor_fig.update_yaxes(range=[0.0, 1.0])
        return indoor_fig


if __name__ == '__main__':
    df_user, df_roommate = fake_data.user_and_roommate_data()
    indoor = indoor_fig(df_user[2], df_roommate[2])
    indoor.fig.show()

