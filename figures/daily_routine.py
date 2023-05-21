import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import fake_data

'''(userid)-daily.csv columns: ["user_id", "start_at", "end_at", "routine"]

user_id: str
start_at: str
end_at: str
routine: str
'''


def get_data(user_id: str) -> pd.DataFrame:
    data_dir = f'csv/routines/{user_id}-daily.csv'
    df = pd.read_csv(data_dir)
    if df.iloc[len(df)-1].tolist()[3] == "00:00:00":
        df.at[len(df)-1, 'end_at'] = "23:59:59"
    return df

def daily_routine(user_id: str) -> go.Figure:
    df = get_data(user_id)
    df['start_at'] = pd.to_datetime(df['start_at'], format='%H:%M:%S')
    df['end_at'] = pd.to_datetime(df['end_at'], format='%H:%M:%S')
    daily_routine_fig = px.timeline(df, x_start='start_at', x_end='end_at', y='user_id', color='routine', height=400, width=1200)
    daily_routine_fig.update_xaxes(tickformat="%H:%M")
    daily_routine_fig.update_layout(template='simple_white', title='Daily Routine')
    return daily_routine_fig

def daily_routine_compare(user_id: str, roommate_id: str) -> go.Figure:
    user_df = get_data(user_id)
    roommate_df = get_data(roommate_id)
    df = pd.concat(user_df, roommate_df)
    daily_routine_fig = px.timeline(user_df, x_start='start_at', x_end='end_at', y='user_id', color='routine', height=400, width=1200)
    daily_routine_fig.update_layout(template='simple_white', title='Daily Routine')
    return daily_routine_fig


class daily_routine_fig:
    def __init__(self, userdata, roommatedata=pd.DataFrame()):
        self.user_df = userdata
        self.roommate_df = roommatedata
        if not roommatedata.empty:
            self.fig_cmp = self.make_fig_compare()
        self.fig = self.make_fig()

    def make_fig(self):
        df = self.user_df
        daily_routine_fig = px.timeline(df.loc[df['routine']!='None'], x_start='start', x_end='end', y='user', color='routine', height=400, width=1200)
        daily_routine_fig.update_layout(template='simple_white', title='Daily Routine')
        return daily_routine_fig

    def make_fig_compare(self):
        df = pd.concat([self.user_df, self.roommate_df])
        daily_routine_fig = px.timeline(df.loc[df['routine']!='None'], x_start='start', x_end='end', y='user', color='routine', height=400, width=1200)
        daily_routine_fig.update_layout(template='simple_white', title='Daily Routine')
        return daily_routine_fig

if __name__ == '__main__':
    df_user, df_roommate = fake_data.user_and_roommate_data()
    daily_routine = daily_routine_fig(df_user[1], df_roommate[1])
    print(daily_routine.user_df)
    daily_routine.fig.show()

