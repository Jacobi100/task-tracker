# Task Tracker CLI

A simple, dependency-free command-line application for tracking work. Tasks are
saved as JSON so they can be reviewed, backed up, or edited without a database.

- [Project brief](https://roadmap.sh/projects/task-tracker)
- Repository: https://github.com/elmustapha100/task-tracker

## Features

- Create, update, and delete tasks.
- Change a task to `in-progress` or `done`.
- List every task, or filter by `todo`, `in-progress`, and `done`.
- Keep task creation and modification timestamps.
- Store data automatically in a `tasks.json` file in the directory where the
  CLI is run.
- Use only Python's standard library.

## Requirements

- Python 3.8 or newer
- A command line

No packages or virtual environment are required.

## Project structure

| File | Purpose |
| --- | --- |
| `tasks_cli.py` | Parses positional command-line arguments and dispatches commands. |
| `tasks.py` | Implements task operations and output. |
| `storage.py` | Loads and saves the JSON task store. |
| `tasks.json` | Created automatically; contains the persisted tasks. |

## Installation

Clone the repository and enter its directory:

```bash
git clone https://github.com/elmustapha100/task-tracker.git
cd task-tracker
```

Verify that the CLI is available:

```bash
python3 tasks_cli.py
```

With no command, the application prints its usage information. On Windows,
replace `python3` with `python` if that command is available on your system.

## Usage

Each command is run with the following form:

```text
python3 tasks_cli.py <command> [arguments]
```

### Add a task

```bash
python3 tasks_cli.py add "Buy groceries"
```

The description may contain spaces and must not be empty.

```text
Task added successfully (ID: 1)
```

### Update a task

Provide the task ID followed by the complete new description:

```bash
python3 tasks_cli.py update 1 "Buy groceries and cook dinner"
```

```text
Task 1 updated successfully.
```

### Delete a task

```bash
python3 tasks_cli.py delete 1
```

```text
Task 1 deleted successfully.
```

### Mark a task in progress

```bash
python3 tasks_cli.py mark-in-progress 1
```

### Mark a task done

```bash
python3 tasks_cli.py mark-done 1
```

Both status commands update the task's `updatedAt` value.

### List tasks

List all tasks:

```bash
python3 tasks_cli.py list
```

Filter tasks by status:

```bash
python3 tasks_cli.py list todo
python3 tasks_cli.py list in-progress
python3 tasks_cli.py list done
```

If no tasks match, the CLI prints `No tasks found.`

## Command reference

| Command | Arguments | Description |
| --- | --- | --- |
| `add` | `"description"` | Adds a task with the `todo` status. |
| `update` | `id "new description"` | Changes a task description. |
| `delete` | `id` | Removes a task. |
| `mark-in-progress` | `id` | Sets a task status to `in-progress`. |
| `mark-done` | `id` | Sets a task status to `done`. |
| `list` | no argument | Lists all tasks. |
| `list todo` | none | Lists tasks waiting to be started. |
| `list in-progress` | none | Lists tasks currently being worked on. |
| `list done` | none | Lists completed tasks. |

## Data storage

`tasks.json` is created in the current working directory when it does not exist.
The CLI does not require a task file to be present before its first run.

For example, running the CLI from `/home/user/projects` looks for and stores its
tasks in `/home/user/projects/tasks.json`.

Every task has this shape:

```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-08-05T12:34:56.123456",
    "updatedAt": "2026-08-05T12:34:56.123456"
  }
]
```

### Task fields

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Unique task identifier generated automatically. |
| `description` | string | The work that needs to be completed. |
| `status` | string | One of `todo`, `in-progress`, or `done`. |
| `createdAt` | string | ISO 8601 timestamp from when the task was created. |
| `updatedAt` | string | ISO 8601 timestamp from the latest change. |

Deleting the highest task ID does not reuse that ID for a later task; new IDs
continue from the largest remaining ID.

## Running from another directory

Because imports are resolved relative to the script, invoke the CLI with its
file path and run from the directory where you want `tasks.json` to live:

```bash
cd /path/to/task-directory
python3 /path/to/task-tracker/tasks_cli.py add "Write documentation"
```

## Error handling

The CLI reports invalid input with an actionable message and exits normally:

- A missing description is rejected.
- Task IDs must be integers.
- Unknown commands and status filters are rejected.
- Empty descriptions are rejected.
- Updates, deletions, and status changes fail safely when an ID does not exist.

## Development

Run each behavior manually from a clean temporary directory:

```bash
mkdir -p /tmp/task-tracker-check
cd /tmp/task-tracker-check
python3 /path/to/task-tracker/tasks_cli.py add "Test task"
python3 /path/to/task-tracker/tasks_cli.py list
```

The application is split into these layers:

1. `tasks_cli.py` validates positional arguments.
2. `tasks.py` applies task rules and formats output.
3. `storage.py` serializes the task list using Python's `json` module.

Keep the storage format backwards compatible when changing task fields, and add
new commands by extending the dispatcher in `tasks_cli.py`.

## Troubleshooting

### `ModuleNotFoundError`

Run `tasks_cli.py` directly with its repository path, or change to the project
root before running `python3 tasks_cli.py`.

### The wrong `tasks.json` was created

Task storage follows the process's current working directory. Run the command
from the directory that should own the task file.

### Invalid JSON

Make a backup of `tasks.json`, ensure its contents are a valid JSON array, and
run the command again. Each task should be represented by a JSON object.

