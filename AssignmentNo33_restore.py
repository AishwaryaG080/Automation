import zipfile
import os
from AssignmentNo33_loggers import log_info, log_error

def restore_backup(zip_file, destination):
    try:
        if not os.path.exists(zip_file):
            raise FileNotFoundError("Zip file not found")

        if not os.path.exists(destination):
            os.makedirs(destination)

        with zipfile.ZipFile(zip_file, 'r') as zipf:
            zipf.extractall(destination)

        log_info(f"Backup restored to {destination}")

    except Exception as e:
        log_error(str(e))
        raise