# Task Tracker CLI

Repository: https://github.com/elmustapha100/task-tracker

Submission / Project page: https://roadmap.sh/projects/task-tracker

A minimal command-line Task Tracker to add, update, list, and manage tasks stored in a JSON file.

## Features

- Add, update, and delete tasks
- Mark tasks as `in-progress` or `done`
- List all tasks or filter by status (`todo`, `in-progress`, `done`)
- Tasks persisted to `tasks.json` in the project directory (created automatically)

## Files

- [tasks_cli.py](tasks_cli.py) — small CLI entrypoint (parses `sys.argv` and dispatches commands)
- [tasks.py](tasks.py) — task operations: add, update, delete, change status, list
- [storage.py](storage.py) — read/write helpers for `tasks.json`

## Quick Start

Run commands from the project root (where the `.py` files live).

Add a task:

```bash
python3 tasks_cli.py add "Buy groceries"
```

Update a task:

```bash
python3 tasks_cli.py update 1 "Buy groceries and cook dinner"
```

Delete a task:

```bash
python3 tasks_cli.py delete 1
```

Mark a task in progress or done:

```bash
python3 tasks_cli.py mark-in-progress 1
python3 tasks_cli.py mark-done 1
```

List tasks:

```bash
python3 tasks_cli.py list         # all tasks
python3 tasks_cli.py list todo    # only todo
python3 tasks_cli.py list done    # only done
python3 tasks_cli.py list in-progress
```

## Task JSON format

Tasks are stored as a list of objects in `tasks.json`. Each task object contains:

```json
{
	"id": 1,
	"description": "Buy groceries",
	"status": "todo",
	"createdAt": "2026-08-05T12:34:56",
	"updatedAt": "2026-08-05T12:34:56"
}
```

## Development notes

- No external libraries are used; the CLI uses `sys.argv` for positional arguments.
- `storage.py` ensures the JSON file is created and handles corrupt/empty files gracefully.
- Run the project from the repository root to ensure module imports work correctly.

## Troubleshooting

- `ModuleNotFoundError`: make sure you run commands from the project directory and your Python path includes the folder.
- `IndexError` when running commands: include the required positional arguments (see usage examples above).

## Contributing

Feel free to open issues or PRs. Small improvements:

- pretty-print timestamps when listing
- add a `search` or `filter` command
- switch to `argparse` if you want richer CLI parsing (optional)

---


