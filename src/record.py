#!/usr/bin/env python

import logging
import util

@util.SingletonCls
class Record(object):
    """docstring for record
    singlton record, but return different logger
    could be used in different file.
    """
    def __init__(self):
        self._setHandler()

    def _setHandler(self):
        self.handlers = [logging.StreamHandler(),logging.FileHandler("record.log")]
        fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(threadName)s %(message)s"
        datefmt = "%a %d %b %Y %H:%M:%S"
        formatter = logging.Formatter(fmt, datefmt)
        for handler in self.handlers:
            handler.setFormatter(formatter)

    def logger(self, name = ''):
        print(name)
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        for handler in self.handlers:
            logger.addHandler(handler)
        return logger

if __name__ == '__main__':
    #class init test
    cls1 = Record()
    print(cls1)
    #class getLogger test
    logger = cls1.logger(__name__)
    print(logger)
    #logger usage checker
    logger.debug("Debug Info Test.")
    logger.info("Debug Info Test.")
    logger.warning("Debug Info Test.")
    logger.error("Debug Info Test.")
    logger.critical("Debug Info Test.")