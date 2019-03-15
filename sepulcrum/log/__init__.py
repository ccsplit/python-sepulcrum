import logging


# The LOGGING_FORMAT will be in the following format:
# Time [LogLevel] {LoggerName:ProcessID(if available)}: Message
# Example:
# 2018-02-19 15:55:27,888 [INFO] {ThreadedTCPRequestHandler:23546}: Session timedout from: 127.0.0.1:50891  # noqa: E501
LOGGING_FORMAT = (
    "%(asctime)-15s [%(levelname)s] " "{%(name)s:%(process)s}: %(message)s"
)  # noqa: E501
logging.basicConfig(format=LOGGING_FORMAT, level=logging.INFO)


def get_logger(name, level="info"):
    logger = logging.getLogger(name)
    level = logging.getLevelName(level.upper())
    logger.setLevel(level)
    return logger
