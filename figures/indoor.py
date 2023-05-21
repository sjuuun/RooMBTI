import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

'''(userid)-weekly.csv columns: ["user_id", "start_at", "end_at", "weekday", "routine"]

user_id: str
start_at: str
end_at: str
weekday: int
routine: str
'''

daily_routines_data = pd.read_csv(f'csv/weekly_routines.csv')

def get_data(user_id: str) -> pd.DataFrame:
    global daily_routines_data
    df = daily_routines_data.loc[daily_routines_data['user_id']==user_id][["user_id", "start_at", "end_at", "weekday", "routine"]].reset_index()
    df['start_at'] = pd.to_datetime(df['start_at'], format='%H:%M:%S')
    df['end_at'] = pd.to_datetime(df['end_at'], format='%H:%M:%S')
    df.sort_values(by=['start_at'])
    start_time = pd.to_datetime("00:00:00", format='%H:%M:%S') 
    timedelta = pd.to_timedelta('1hour')
    indoor_df = []
    rown = 0
    for i in range(24):
        indoorcnt = 0
        outdoorcnt = 0
        while rown < len(df) and start_time <= df.at[rown,"start_at"] and df.at[rown, "end_at"] <= start_time+timedelta:
            if df.at[rown, "routine"] == "SLEEP" or df.at[rown, "routine"] == "INDOOR":
                indoorcnt+=1
            else:
                outdoorcnt+=1
            rown+=1
        if indoorcnt+outdoorcnt > 0:
            indoor_ratio=indoorcnt/(indoorcnt+outdoorcnt)
            indoor_df.append([user_id, start_time, start_time+timedelta, indoor_ratio])
        start_time += timedelta
    indoor_df.append([user_id, start_time, start_time+timedelta, indoor_df[0][3]])
    indoor_df = pd.DataFrame(indoor_df, columns=["user_id", "start_at", "end_at", "indoor_ratio"])
    return indoor_df
    

def indoor(user_id: str) -> go.Figure:
    df = get_data(user_id)
    indoor_fig = go.Figure(data=[
                      go.Scatter(x=df.start_at, y=df.indoor_ratio, mode='lines', name='User')
                      ])
    indoor_fig.update_layout(template='simple_white', title='Indoor', width=400, height=300)
    indoor_fig.update_xaxes(tickformat="%H:%M")
    indoor_fig.update_yaxes(range=[0.0, 1.1])
    return indoor_fig


def indoor_compare(user_id: str, roommate_id: str) -> go.Figure:
    user_df = get_data(user_id)
    roommate_df = get_data(roommate_id)
    """indoor_fig = go.Figure(data=[
                      go.Scatter(x=user_df.start_at, y=user_df.indoor_ratio, mode='lines', name='User', line_shape='spline'),
                      go.Scatter(x=roommate_df.start_at, y=roommate_df.indoor_ratio, mode='lines', name='User', line_shape='spline')
                      ])"""
    indoor_fig = go.Figure(data=[
                      go.Scatter(x=user_df.start_at, y=user_df.indoor_ratio, mode='lines', name='User'),
                      go.Scatter(x=roommate_df.start_at, y=roommate_df.indoor_ratio, mode='lines', name='Roommate')
                      ])
    indoor_fig.update_layout(template='simple_white', title='Indoor', width=400, height=300)
    indoor_fig.update_xaxes(tickformat="%H:%M")
    indoor_fig.update_yaxes(range=[0.0, 1.1])
    return indoor_fig



if __name__ == '__main__':
    user_id = "P3029"
    roommate_id = "P3030"
    fig = indoor_compare(user_id, roommate_id)
    fig.show()

