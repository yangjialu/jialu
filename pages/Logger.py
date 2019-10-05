import logging


class MyLog(object):

    def my_log(self, level, msg):
        mylog = logging.getLogger("api_log")
        mylog.setLevel("INFO")

        format = logging.Formatter("[%(asctime)s]-[%(levelname)s]-[%(lineno)d]-[日志信息]:%(message)s")
        ch = logging.StreamHandler()
        ch.setLevel("INFO")
        ch.setFormatter(format)

        fh = logging.FileHandler('test.log', encoding="utf-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(format)

        mylog.addHandler(ch)
        mylog.addHandler(fh)

        if level == "DEBUG":
            mylog.debug(msg)
        elif level == "INFO":
            mylog.info(msg)
        elif level == "WARNING":
            mylog.warning(msg)
        elif level == "ERROR":
            mylog.error(msg)
        else:
            mylog.critical(msg)
        mylog.removeHandler(fh)
        mylog.removeHandler(ch)

    def debug(self, msg):
        self.my_log("DEBUG", msg)

    def info(self, msg):
        self.my_log("INFO", msg)

    def warning(self, msg):
        self.my_log("WARNING", msg)

    def error(self, msg):
        self.my_log("ERROR", msg)

    def critical(self, msg):
        self.my_log("CRITICAL", msg)


if __name__ == '__main__':
    MyLog().info("自动化测试真的很好玩啊，棒棒的")