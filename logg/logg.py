# set logging_dir system variable

import os
import logging
from datetime import datetime

current_month = datetime.now().strftime("%Y-%m")
current_date = datetime.now().strftime("%Y-%m-%d")

def setup_logging():
    
    logging_dir = os.environ.get('logging_dir')

    if not logging_dir:
        logging_dir = "./logs"
    
    if not os.path.exists(logging_dir):
        os.mkdir(logging_dir)

    logging_file_path = os.path.join(logging_dir,f'{current_month}.log')

    logging.basicConfig(
        filename=logging_file_path,
        level = logging.INFO,
        format = '%(asctime)s;%(levelname)s;%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
    )

if __name__ == "__main__":
    setup_logging()
    logging.info(f"logger test from file: {__file__}")