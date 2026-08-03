# storage.py — the file I/O layer
# Responsible for: talking to tasks.json only. Knows nothing about what a "task" means logically.
# tasks.py calls into this; this file never calls back into tasks.py.

import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    """
    Read tasks.json and return the data structure (list or dict — whichever you chose).
    
    Things to work through:
    - What if TASKS_FILE doesn't exist yet? (Requirement says: create it, don't crash.)
    - What if it exists but is empty (0 bytes)? json.load() will choke on that.
    - What if it exists but contains invalid JSON (someone hand-edited it badly)?
    - What should this function return in each of those cases — an empty list/dict?
      Decide on ONE consistent "empty" representation and stick to it everywhere.
    """
    pass


def save_tasks(tasks):
    """
    Write the given tasks data structure back to tasks.json.
    
    Things to work through:
    - Which json.dump() parameters matter here? (Think about human-readability —
      you'll be eyeballing this file a lot while testing.)
    - Does this function need to return anything, or is it pure side effect?
      (Tie back to your own notes: json.dump() itself returns None — is that
      relevant to how you design this wrapper?)
    """
    pass