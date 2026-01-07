import os
import time
import logging


TARGET_DIR = "path/to/your/directory"   # change this
DAYS_OLD = 30                            # files older than this
MIN_SIZE_MB = 5                          # minimum size to consider
DRY_RUN = True                           # True = no deletion
LOG_FILE = "cleanup.log"


# setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

now = time.time()
deleted_files = 0
skipped_files = 0

for root, dirs, files in os.walk(TARGET_DIR):
    for file in files:
        file_path = os.path.join(root, file)

        try:
            file_age_days = (now - os.path.getmtime(file_path)) / 86400
            file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

            if file_age_days > DAYS_OLD and file_size_mb > MIN_SIZE_MB:
                if DRY_RUN:
                    logging.info(f"[DRY RUN] Would delete: {file_path}")
                else:
                    os.remove(file_path)
                    logging.info(f"Deleted: {file_path}")
                deleted_files += 1
            else:
                skipped_files += 1

        except Exception as e:
            logging.error(f"Error processing {file_path}: {e}")

# summary
logging.info("Cleanup Summary")
logging.info(f"Deleted files: {deleted_files}")
logging.info(f"Skipped files: {skipped_files}")

print("Cleanup task completed. Check cleanup.log for details.")