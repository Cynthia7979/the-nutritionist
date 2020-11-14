import logging
from shutil import move
from time import strftime

# Logging
DEFAULT_LOGLEVEL = logging.DEBUG
DEFAULT_LOG_FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

DEFAULT_STREAMHANDLER = logging.StreamHandler()
DEFAULT_FILEHANDLER = logging.FileHandler('the_nutritionist.log')
DEFAULT_STREAMHANDLER.setLevel(logging.DEBUG)
DEFAULT_FILEHANDLER.setLevel(DEFAULT_LOGLEVEL)
DEFAULT_FILEHANDLER.setFormatter(DEFAULT_LOG_FORMATTER)
DEFAULT_STREAMHANDLER.setFormatter(DEFAULT_LOG_FORMATTER)


def get_public_logger(name, loglevel=DEFAULT_LOGLEVEL):
    """
    Get a public logger for a file.
    :param name: Name of the logger.
    :param loglevel: Logging level in strings (so that people don't have to import logging first to use loggers).
    """
    logger = logging.getLogger(name)
    logger.setLevel(loglevel)
    logger.addHandler(DEFAULT_FILEHANDLER)
    logger.addHandler(DEFAULT_STREAMHANDLER)
    return logger


def logged_class(cls):
    """
    Descriptor for classes that require a logger. Example:
    ```
    @logger.logged_class
    class MyClass(object):
        def __init__(self):
            self.logger.debug('hello logger!')
    ```
    """
    class_name = cls.__name__
    logger = logging.getLogger(class_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(DEFAULT_FILEHANDLER)
    logger.addHandler(DEFAULT_STREAMHANDLER)
    logger.propagate = False
    logger.debug('Logger {} created.'.format(class_name))
    setattr(cls, 'logger', logger)
    return cls


def move_log():
    """
    Move the log file to ./Log/ after program is closed
    """
    DEFAULT_FILEHANDLER.close()
    DEFAULT_STREAMHANDLER.close()
    try:
        move('the_nutritionist.log', strftime('Logs/log_%y-%m-%d_%H-%M-%S.log'))
    except OSError as e:
        # As when multiple games were opened at the same time
        if e.winerror == 32:
            _meta_logger.warning("Another program is using log file. Now exiting.")
        else:
            _meta_logger.error("Unexpected error when moving log file: {}".format(e))


def logger_exit():
    _meta_logger.info('Ready to close.')
    DEFAULT_FILEHANDLER.close()
    DEFAULT_STREAMHANDLER.close()
    move_log()


_meta_logger = get_public_logger('init_py')
GLOBAL_LOGGER = get_public_logger('global')