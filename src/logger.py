import os
import logging
from datetime import datetime


file_name=f"{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}.log"
os.makedirs("log_folder",exist_ok=True)
file_name_path=os.path.join("log_folder",file_name)

logging.basicConfig(
    filename=file_name_path,
    level=logging.INFO,
    format="[%(asctime)s-%(levelname)s]:%(message)s",
)