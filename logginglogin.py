import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s')


# StreamHandler
streamingHandler = logging.StreamHandler()
streamingHandler.setFormatter(formatter)


# FileHandler
file_handler = logging.FileHandler('.C:\Users\liam\Desktop\log\1.log')
file_handler.setFormatter(formatter)


# RotatingFileHandler 
log_max_size = 10 * 1024 * 1024  ## 10MB
log_file_count = 20
rotatingFileHandler = logging.handlers.RotatingFileHandler(
    filename='./logs/output.log',
    maxBytes=log_max_size,
    backupCount=log_file_count
)
rotatingFileHandler.setFormatter(formatter)


# RotatingFileHandler
timeFileHandler = logging.handlers.TimedRotatingFileHandler(
    filename='./logs/output.log',
    when='midnight',
    interval=1,
    encoding='utf-8'
)
timeFileHandler.setFormatter(formatter)