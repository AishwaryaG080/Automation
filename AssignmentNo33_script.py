import argparse
from AssignmentNo33_loggers import setup_logger
from AssignmentNo33_backup import create_backup
from AssignmentNo33_restore import restore_backup
from AssignmentNo33_history import save_history, show_history
from AssignmentNo33_email import send_email
from AssignmentNo33_utils import validate_directory

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--backup", help="Source directory")
    parser.add_argument("--restore", help="Zip file to restore")
    parser.add_argument("--dest", help="Restore destination")
    parser.add_argument("--history", action="store_true")
    parser.add_argument("--exclude", nargs="*", default=[])
    parser.add_argument("--email", action="store_true")

    args = parser.parse_args()
    log_file = setup_logger()

    if args.backup:
        if not validate_directory(args.backup):
            return

        zip_file, count = create_backup(args.backup, args.exclude)
        save_history(count, zip_file)

        if args.email:
            send_email(
                sender="your_email@gmail.com",
                password="app_password",
                receiver="receiver@gmail.com",
                log_file=log_file,
                zip_file=zip_file
            )

    elif args.restore:
        restore_backup(args.restore, args.dest)

    elif args.history:
        show_history()

if __name__ == "__main__":
    main()