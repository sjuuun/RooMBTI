# RooMBTI

2023 Spring, CS481 Data Visualization

Data Visualization to choose the best random roommate who has the most similar routines with me.

## Team Information

| Student ID | Name               | GitHub ID     |
|------------|--------------------|---------------|
| 20160381   | Seungjun Oh (오승준)  | sjuuun        |
| 20170152   | Jeongmin Kim (김정민) | sillysillyman |
| 20190419   | Junseok Youk (육준석) | lsz4221       |

## Project Information

- [Process Book](https://docs.google.com/presentation/d/1kuU-V88qBJ4Ogxo-qTaQh4tEqD8Xr45Mj6PrIO1u69o/edit#slide=id.g1f9df24d571_0_171)
- [Prototype URL](https://roombti.herokuapp.com/)

## Installation

Install using requirements.txt

```bash
$ pip install -r requirements.txt
```

Following libraries are needed.

```
pandas==2.0.1
dash==2.9.3
dash-core-components==2.0.0
dash-bootstrap-components==1.4.1
plotly==5.14.1
notebook==6.5.4
gunicorn==20.1.0
dash_daq==0.5.0
scikit-learn==1.2.2
```

## Directory Information

### assets
- Assets such as css files.

### csv
- Processed data for visualization.
- routines
  - Aggregated routines per user.
  - There are one csv file for daily routines and one csv file for weekly routines per one user.
  - `{USER ID}-daily.csv`
  - `{USER_ID}-weekly.csv`
- routines_raw
  - Aggregated routines.
  - `{USER_ID}-location.csv`
    - Aggregated routines from LocationEntity data.
    - It contains routines for indoor time, class time, study time, exercise time.
  - `{USER_ID}-sleep.csv`
    - Aggregated routines from DeviceEventEntity data.
    - It contains routines for sleep time.
    - If there are no event during more than 4 hours, we assume it to sleep time.
- `bfi.csv`
  - Data of personal traits from BFI-15 data.
- `daily_routines.csv`
  - Merged data of daily routines in `routines` directory.
- `weekly_routines.csv`
  - Merged data of weekly routines in `routines` directory.
- `similarity.csv`
  - Data for similarity of routines.

### data_process

Jupyter Notebook or Python files for data processing.

### figures

Methods for visualizing data with Plotly.

### pages

Python files for page layout with Dash.
Here, the Dash application calls figure functions in `figures` directory.

### app.py

Main file of the web application.
Run the web application by the following command.

```bash
$ python app.py
```

### Configuration files

- `.gitignore`: List of files which are ignored in git repository.
- `.mapbox_token`: API token for visualization of Mapbox scatter plot.
- `requirements.txt`: List of required libraries.
- `Procfile`: Configuration for Heroku. (Command to be executed in Heroku)
- `runtime.txt`: Configuration for Heroku. (Python runtime version)

## Pages

Following files are in `pages` directory. This is brief information about those files.

- `overview.py`
  - Overview of my routines. 
  - User can analyze their own routines in this page.
- `users.py`
  - List of roommates. 
  - User can compare roommates by similarity of sleep routines.
- `comparison.py`
  - Comparison between my routines and roommate's routines.
  - If user select one of roommates, user can compare routines with he/she.

## Figures

Following files are in `figures` directory. This is brief information about those files.

- `bfi.py`: Pentagon widget for BFI-15 data.
- `daily_routine.py`: Bar chart of daily routine.
- `weekly_routine.py`: Bar chart of weekly routine.
- `indoor.py`: Line chart to visualize when users are in indoor.
- `location_mapbox.py`: Scatter chart to visualize location information.

## Data Process

Following files are in `data_process` directory. This is brief information about those files.

- `location.ipynb`
  - Analyze routines by LocationEntity data.
  - We used DBSCAN to cluster geographical data and derive routines from location data.
  - Derive routines of indoor time, class time, study time, exercise time.
- `sleep_by_device.ipynb`
  - Analyze sleep routine by DeviceEventEntity data.
  - We assume that if device is not used more than 4 hours, it will be sleep routine.
- `aggregate_routine.ipynb`
  - Aggregate routines from the result of location and sleep data.
  - Aggregate into daily routines and weekly routines.
- `concat_routines.py`
  - Concat daily and weekly routines of each users.
- `bfi.py`
  - Select required data from BFI-15 data.
- `get_similarity.ipynb`
  - Calculate similarity of sleep routines.
