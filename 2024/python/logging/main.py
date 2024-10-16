import logging
from config import setup_logging
logging = logging.getLogger("main") # changed the logger name, default is "root"

setup_logging()

logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.debug('This is an debug message')