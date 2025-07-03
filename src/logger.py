import logging
import os
from datetime import datetime


#create file log
file_log = f"a{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

#select path
file_path = os.path.join(os.getcwd(), "logs")
os.makedirs(file_path, exist_ok=True)


#select path file log
file_log_path = os.path.join(file_path, file_log)


#message style
logging.basicConfig(
    filename=file_log_path,
    format="[%(asctime)s] [Line:%(lineno)d] [%(name)s] [%(levelname)s] - %(message)s",
    level=logging.INFO
)