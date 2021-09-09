import logging
import datetime

log_date = datetime.date.today()
log_time = datetime.datetime.now().time().strftime("%H%M%S")

log_format = "%(asctime)s - %(message)s"

logging.basicConfig(filename=fr"Logs/log_{log_date}.log",
                    level=logging.INFO,
                    datefmt='%d-%m-%y %H:%M:%S',
                    format=log_format,
                    filemode='a')

logster = logging.StreamHandler()
logster.setLevel(logging.INFO)

fmtr = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
logster.setFormatter(fmtr)
logging.getLogger().addHandler(logster)

log = logging.getLogger()
