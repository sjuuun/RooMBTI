import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import fake_data

#daily_routine_columns = ['timestamp', 'Sleeping', 'Class', 'Meal', 'Study', 'Exercise', 'user']


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