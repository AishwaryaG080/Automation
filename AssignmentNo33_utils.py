import os

DEFAULT_EXCLUDE = [".tmp", ".log", ".exe"]

def validate_directory(path):
    return os.path.exists(path) and os.path.isdir(path)

def should_exclude(file, user_ext):
    ext = os.path.splitext(file)[1]
    return ext in DEFAULT_EXCLUDE or ext in user_ext