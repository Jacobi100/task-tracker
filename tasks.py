import os
import json 
from datetime import datetime 

Task_file = "tasks.json"

def load_task():
    """return an empty list if doesn't exist, else load tasks from JSON file """
    if not os.path.exists(Task_file):
        return []
    
    try:
        with open(Task_file, "r") as file :
            return json.load(file)  #deserialize the json file object into corresponding Python datatype
     except Exception :
        return []

def saves_task(tasks):
    """saves tasks back to JSON file"""
    with open(Task_file, "w") as file :
        json.dump(tasks, file)

def get_task_id(tasks):
    """getting unique id for each tasks"""
    if not in tasks :
        return 1 
    return max([task['id'] for task in tasks]) + 1 

def add_task(description) :
     




        



