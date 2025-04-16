import logging
import os

class Logger:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), '../logs/tests.log'), 
                            format='%(asctime)s:%(levelname)s:%(message)s', 
                            datefmt="%Y-%m-%d %H:%M:%S", 
                            force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger