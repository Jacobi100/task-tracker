import sys 
from tasks import add_task, update_task, delete_task, change_status, list_tasks

def main(): 
    if len(sys.argv) < 2 : 
        print("Usage: python tasks.py <command> [arguments]")
        return command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3 :
            print("Error : add requires a description.")    
        return description = " ".join(sys.argv[2:])
        add_task(description)

     elif command == "update":
        if len(sys.argv) < 4:
            print("Error: update requires an ID and description.")
            return
        task_id = int(sys.argv[2])
        description = " ".join(sys.argv[3:])
        update_task(task_id, description)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: delete requires an ID.")
            return
        task_id = int(sys.argv[2])
        delete_task(task_id)

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: mark-in-progress requires an ID.")
            return
        task_id = int(sys.argv[2])
        change_status(task_id, "in-progress")    

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: mark-done requires an ID.")
            return
        task_id = int(sys.argv[2])
        change_status(task_id, "done")

    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()    

    else : 
        print("Unknown command.")       

if __name__ == "__main__" : 
    main()        

