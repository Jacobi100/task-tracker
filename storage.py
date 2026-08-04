import os
import json 

Task_file = "tasks.json"

def load_tasks(): 
    if not os.path.exists(Task_file):
        return []

    try :
        with open(Task_file, "r") as file :
            return json.load(file)
    except Exception : 
        return []

def save_tasks(tasks):
    with open(Task_file , "w") as file :
        json.dump(tasks,file)
        file.write('\n')
