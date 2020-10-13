import logging
import time
from demo.common.function import project_path


class FrameLog:
    def __init__(self, logger=None):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        self.log_time = time.strftime("%Y-%m-%d")
        self.log_path = project_path() + "/Logs/"
        self.log_name = self.log_path + self.log_time + 'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter('[%(asctime)s]  '
                                      '%(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        #self.logger.removeHandler(fh)
        fh.close()

    def log(self):
        return self.logger


if __name__ == '__main__':
    lo = FrameLog()
    log = lo.log()
    log.error("error")
    log.debug("debug")
    log.info("info")
    log.critical("严重")
