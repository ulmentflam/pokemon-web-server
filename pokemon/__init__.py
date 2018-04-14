import sys
import logging
import environs


env = environs.Env()

formatter = logging.Formatter("[%(asctime)s]\t[%(module)s:%(funcName)s:%(lineno)d]%(levelname)s\t: %(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)