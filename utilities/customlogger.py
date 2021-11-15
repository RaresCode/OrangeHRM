import logging

class logGen():
    @staticmethod
    def logger():
        logging.basicConfig(filename="..\\Logs\\automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.DEBUG, force=True)
        logger= logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
