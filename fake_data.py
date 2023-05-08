import pandas as pd
import numpy as np
import random


timestamp_columns = ['timestamp']

bfi_columns = ['Openness', 'Conscientiousness', 'Neuroticism', 'Extraversion', 'Agreeableness']
daily_routine_columns = timestamp_columns+['Sleeping', 'Class', 'Meal', 'Study', 'Exercise']
indoor_columns = timestamp_columns+['IndoorRatio']

class dummydata:
    def __init__(self):
        self.bfi = []
        self.daily_routine = []
        self.indoor = []
    def makedata(self, setseed = 12345, init_time = 1557276595830, interval = 2000, data_num=2000):
        random_bfi = [[random.randrange(3,16) for i in range(5)]]
        self.bfi=pd.DataFrame(random_bfi, columns=bfi_columns)
        random.seed(setseed)
        daily_routine_data = []
        indoor_data = []
        randval = 0
        daily_routine_change = 0
        daily_routine = 0
        for i in range(data_num):
            time = [init_time + i*interval]
            select_routine = random.randrange(0,6)
            if daily_routine_change <= i:
                daily_routine = [j==select_routine for j in range(1,6)]
                daily_routine_change = daily_routine_change+random.randrange(100, 250)
            indoor = 0
            if i%10==0:
                randval = (random.random()-0.5)*0.005
            if i==0:
                indoor=random.random()
            else:
                indoor=indoor_data[i-1][1]+randval+0.005*(random.random()-0.5)
                if indoor > 1:
                    indoor = 1
                if indoor < 0:
                    indoor = 0
            daily_routine_data.append(time+daily_routine)
            indoor_data.append([time[0],indoor])
    
        self.daily_routine = pd.DataFrame(daily_routine_data, columns=daily_routine_columns)
        self.indoor = pd.DataFrame(indoor_data, columns=indoor_columns)
        return self.bfi, self.daily_routine, self.indoor
    
    
    
def user_and_roommate_data(userseed = 12345, roommateseed = 54321):
    data1 = dummydata()
    data2 = dummydata()
    userdf = data1.makedata(setseed=userseed)
    roommatedf = data2.makedata(setseed=roommateseed)

    df_user = []
    df_roommate = []

    userdf[0]['user'] = ['User']
    roommatedf[0]['user'] = ['Roommate']
    df_user.append(userdf[0])
    df_roommate.append(roommatedf[0])

    userdf[1]['timestamp'] = pd.to_datetime(userdf[1]['timestamp'], unit='ms')
    roommatedf[1]['timestamp'] = pd.to_datetime(roommatedf[1]['timestamp'], unit='ms')

    daily_routine = daily_routine_timeline(userdf[1], roommatedf[1])
    df_user.append(daily_routine[0])
    df_roommate.append(daily_routine[1])

    userdf[2]['user'] = ['User' for i in range(2000)]
    roommatedf[2]['user'] = ['Roommate' for i in range(2000)]
    userdf[2]['timestamp'] = pd.to_datetime(userdf[2]['timestamp'], unit='ms')
    roommatedf[2]['timestamp'] = pd.to_datetime(roommatedf[2]['timestamp'], unit='ms')
    df_user.append(userdf[2])
    df_roommate.append(roommatedf[2])
    return df_user, df_roommate


def daily_routine_timeline(userdata, roommatedata):
    df_user = userdata
    df_roommate = roommatedata
    new_data_user = []
    new_data_roommate = []
    routine_name = ['None', 'Sleeping', 'Class', 'Meal', 'Study', 'Exercise']


    start=0
    prev_routine = 0
    for i in range(len(df_user)):
        row_user = df_user.iloc[i].tolist()
        routine = 0
        for j in range(1,6):
            if row_user[j]:
                routine=j
        if i==0:
            start = row_user[0]
            prev_routine = routine
        elif routine != prev_routine:
            new_data_user.append([start, row_user[0], routine_name[routine], 'User'])
            start = row_user[0]
            prev_routine = routine

        
    start=0
    prev_routine=0
    for i in range(len(df_roommate)):
        row_roommate = df_roommate.iloc[i].tolist()
        routine = 0
        for j in range(1,6):
            if row_roommate[j]:
                routine=j
        if i==0:
            start = row_roommate[0]
            prev_routine = routine
        elif routine != prev_routine:
            new_data_roommate.append([start, row_roommate[0], routine_name[routine], 'Roommate'])
            start = row_roommate[0]
            prev_routine = routine

    df_user = pd.DataFrame(new_data_user, columns=['start', 'end', 'routine', 'user'])
    df_roommate = pd.DataFrame(new_data_roommate, columns=['start', 'end', 'routine', 'user'])
    return df_user, df_roommate



def daily_routine_data(userdata, roommatedata):
    df_user = userdata
    df_roommate = roommatedata
    new_data_user = []
    new_data_roommate = []

    for i in range(len(df_user)):
        row_user = df_user.iloc[i].tolist()
        routine = 0
        for j in range(1,6):
            if row_user[j]:
                routine=j
        new_data_user.append([row_user[0], routine, 'User'])


    for i in range(len(df_roommate)):
        row_roommate = df_roommate.iloc[i].tolist()
        routine = 0
        for j in range(1,6):
            if row_roommate[j]:
                routine=j
        new_data_roommate.append([row_roommate[0], routine, 'Roommate'])

    df_user = pd.DataFrame(new_data_user, columns=['timestamp', 'routine', 'user'])
    df_roommate = pd.DataFrame(new_data_roommate, columns=['timestamp', 'routine', 'user'])
    return df_user, df_roommate



    

    
