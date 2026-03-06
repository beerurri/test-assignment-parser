import logging
import colorlog

def setup_logger():
    handler = colorlog.StreamHandler()
    formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        },
        datefmt="%H:%M:%S"
    )
    handler.setFormatter(formatter)
    logger = colorlog.getLogger()
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False