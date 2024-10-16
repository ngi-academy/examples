import logging
from logging.handlers import SMTPHandler,RotatingFileHandler

def setup_logging(): 
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # File Handler
    file_handler = RotatingFileHandler("my_log.log", maxBytes=5000, backupCount=2)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    my_log = logging.getLogger()
    my_log.setLevel(logging.DEBUG) # Refer the note below to understand the presedence of this.
    my_log.addHandler(file_handler)
    my_log.addHandler(console_handler)

"""
The setLevel function in Python's logging module is used to specify the lowest-severity level of log messages that you want to handle. If a message's level is below the level set by setLevel, it will be ignored.

The setLevel function can be used on both logger objects and handler objects, and this creates a kind of hierarchy.

Logger Level: If a level is set for the logger, it acts as the starting point. Any log message with severity below this level will be ignored, no matter what level might be set for the handler.

Handler Level: If a level is set on a handler, it further filters the messages it sends on from the logger. It can't broaden the scope to include messages ignored by the logger level; it can only narrow it down further.

For example, if you set the logger level to WARNING, then only messages of severity WARNING, ERROR, and CRITICAL will be passed on to the handlers.

Now, if a particular handler has its level set to ERROR, it will only process ERROR and CRITICAL messages, ignoring WARNING messages, even though the logger level allows WARNING messages.

So the precedence is:

Logger level --> Handler level

And in terms of filtering scope:

Broadest --> Narrowest

Is:

Logger level --> Handler level
"""