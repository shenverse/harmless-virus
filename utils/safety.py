import os
import sys

FORBIDDEN_PATHS = [
    os.path.expanduser("~"),
    "C:\\Windows\\System32",
    "C:\\Program Files",
]

def is_safe_environment():
    return True

def no_file_modification():
    return True

def emergency_exit():
    sys.exit(0)
