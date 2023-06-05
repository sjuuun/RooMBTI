"""
Concat routines.

- Concat daily routines in csv/routines/xxx-daily.csv
- Concat weekly routine in csv/routines/xxx-weekly.csv
"""
import pandas as pd
import glob


def concat_daily_routines():
    daily_routine_files = glob.glob('../csv/routines/*-daily.csv')
    daily_df = pd.concat([pd.read_csv(f) for f in daily_routine_files])

    daily_df.to_csv('../csv/daily_routines.csv')


def concat_weekly_routines():
    daily_routine_files = glob.glob('../csv/routines/*-weekly.csv')
    daily_df = pd.concat([pd.read_csv(f) for f in daily_routine_files])

    daily_df.to_csv('../csv/weekly_routines.csv')


if __name__ == "__main__":
    concat_daily_routines()
    concat_weekly_routines()
