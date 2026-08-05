import sys
from tasks import add_task, update_task, delete_task, change_status, list_tasks


def print_usage():
    print("Usage: python tasks_cli.py <command> [arguments]")
    print("Commands: add, update, delete, mark-in-progress, mark-done, list")


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: add requires a description.")
            return
        description = " ".join(sys.argv[2:])
        add_task(description)

    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: update requires an ID and description.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        description = " ".join(sys.argv[3:])
        update_task(task_id, description)

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: delete requires an ID.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        delete_task(task_id)

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Error: mark-in-progress requires an ID.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        change_status(task_id, "in-progress")

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Error: mark-done requires an ID.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        change_status(task_id, "done")

    elif command == "list":
        status_filter = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status_filter)

    else:
        print("Error: Unknown command.")
        print_usage()


if __name__ == "__main__":
    main()

