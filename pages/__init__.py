from enum import Enum

SAMPLE_ME_ID = "P3029"
SAMPLE_ROOMMATE_ID = "P3030"


class Routine(Enum):
    SLEEP = "Sleeping Time"
    CLASS = "Class Time"
    MEAL = "Meal Time"
    STUDY = "Study Time"
    EXERCISE = "Exercise Time"
