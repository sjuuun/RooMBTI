import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

'''(userid)-daily.csv columns: ["user_id", "start_at", "end_at", "routine"]

user_id: str
start_at: str
end_at: str
routine: str
'''
daily_routines_data = pd.read_csv(f'csv/daily_routines.csv')


def get_data(user_id: str) -> pd.DataFrame:
    global daily_routines_data
    df = daily_routines_data.loc[daily_routines_data['user_id']==user_id][["user_id", "start_at", "end_at", "routine"]].reset_index()
    if df.iloc[len(df)-1].tolist()[3] == "00:00:00":
        df.at[len(df)-1, 'end_at'] = "23:59:59"
    df['start_at'] = pd.to_datetime(df['start_at'], format='%H:%M:%S')
    df['end_at'] = pd.to_datetime(df['end_at'], format='%H:%M:%S')
    df.sort_values(by=['user_id', 'start_at'])
    merged_df = []
    cnt=0
    while cnt < (len(df)-1):
        new_row = df.iloc[cnt].tolist()
        while cnt < (len(df)-1) and df.at[cnt, 'routine'] == df.at[cnt+1, 'routine']:
            new_row[3] = df.at[cnt+1, 'end_at']
            cnt+=1
        merged_df.append(new_row)
        cnt+=1
    merged_df = pd.DataFrame(merged_df, columns=["index", "user_id", "start_at", "end_at", "routine"])
    return merged_df


def daily_routine(user_id: str) -> go.Figure:
    df = get_data(user_id)
    df = df.replace(user_id, "You")
    daily_routine_fig = px.timeline(df, x_start='start_at', x_end='end_at', y='user_id', color='routine', height=400, width=1200)
    daily_routine_fig.update_xaxes(tickformat="%H:%M")
    daily_routine_fig.update_layout(template='simple_white', title='Daily Routine', yaxis_title=None)
    return daily_routine_fig


def daily_routine_compare(user_id: str, roommate_id: str) -> go.Figure:
    user_df = get_data(user_id)
    roommate_df = get_data(roommate_id)
    df = pd.concat([user_df, roommate_df])[["user_id", "start_at", "end_at", "routine"]]
    df = df.replace(user_id, "You")
    df = df.replace(roommate_id, "Roommate")
    daily_routine_fig = px.timeline(df, x_start='start_at', x_end='end_at', y='user_id', color='routine', height=400, width=1200)
    daily_routine_fig.update_xaxes(tickformat="%H:%M")
    daily_routine_fig.update_layout(template='simple_white', title='Daily Routine', yaxis_title=None)
    return daily_routine_fig


if __name__ == '__main__':
    user_id = "P3029"
    roommate_id = "P3030"
    fig = daily_routine_compare(user_id, roommate_id)
    fig.show()
