import logging

def get_logs(level, message):

    logging.basicConfig(level=level, format = '%(asctime)s - %(message)s', datefmt = '%d-%b-%y %H:%M:%S')
    logger = logging.getLogger()
    if level == "DEBUG":
        logger.debug(f"{level}: {message}")
    elif level == "INFO":
        logger.info(f"{level}: {message}")  
    elif level == "WARNING":
        logger.warning(f"{level}: {message}")
    elif level == "ERROR":
        logger.error(f"{level}: {message}")
    elif level == "CRITICAL":
        logger.critical(f"{level}: {message}")
    else:
        print('Podaj odpowiedni parametr')

get_logs("INFO", 'wszystko ok') 
get_logs("niewiem", 'sprawdzam')
get_logs('CRITICAL', 'serwer pada')