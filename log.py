import logging
import logging.config
from time import ctime

logging.config.fileConfig("log.conf")
logging = logging.getLogger()

logging.debug(f"debug log")
logging.info(f"info log")
logging.warning(f"warning log")
logging.error(f"error log")
logging.critical(f"critical log")

