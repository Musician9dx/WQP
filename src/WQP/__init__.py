import os 
import sys
import logging


log_filepath=os.path.join("logs","runninglogs.log")
os.makedirs("logs",exist_ok=True)


logging.basicConfig(

    format='[%(asctime)s : %(levelname)s : %(module)s: %(message)s]',
    level=logging.INFO,
    handlers=[

        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]

)

logger=logging.getLogger('WQP')