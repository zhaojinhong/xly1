import logging

def my_log():
    logger = logging.getLogger()
    logger.handlers.clear()
    fh = logging.FileHandler("51reboot.log")
    fh.setLevel(logging.ERROR)
    fmt = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger


