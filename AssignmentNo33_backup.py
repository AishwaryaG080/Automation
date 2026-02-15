import os
import zipfile
from datetime import datetime
from AssignmentNo33_loggers import log_info, log_error
from AssignmentNo33_utils import should_exclude

def create_backup(source, exclude_ext):
    try:
        if not os.path.exists("Backups"):
            os.makedirs("Backups")

        start_time = datetime.now()
        zip_name = f"Backups/backup_{start_time.strftime('%Y%m%d_%H%M%S')}.zip"

        files_copied = 0

        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(source):
                for file in files:
                    if not should_exclude(file, exclude_ext):
                        full_path = os.path.join(root, file)
                        zipf.write(full_path)
                        files_copied += 1

        log_info(f"Backup start time: {start_time}")
        log_info(f"Files copied: {files_copied}")
        log_info(f"Zip file: {zip_name}")

        return zip_name, files_copied

    except Exception as e:
        log_error(str(e))
        raise