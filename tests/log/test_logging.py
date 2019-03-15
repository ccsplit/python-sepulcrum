import logging

from ..context import get_logger


def test_get_logger_default():
    logger = get_logger("test_logger")
    assert logger.level == logging.INFO, "Default log level should have been INFO."
