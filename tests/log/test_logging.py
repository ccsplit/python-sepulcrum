import logging

import pytest

from ..context import get_logger


def test_get_logger_default():
    logger = get_logger("test_logger")
    assert logger.level == logging.INFO, "Default log level should have been INFO."


@pytest.mark.parametrize(
    "level", ["debug", "DEBUG", "DeBuG", "dEbUg", "DEbUG", logging.DEBUG]
)
def test_get_logger_debug(level):
    logger = get_logger("test_logger", level=level)
    assert logger.level == logging.DEBUG, "Log level should have been DEBUG."


@pytest.mark.parametrize(
    "level", ["info", "INFO", "InFo", "iNfO", "INfO", logging.INFO]
)
def test_get_logger_info(level):
    logger = get_logger("test_logger", level=level)
    assert logger.level == logging.INFO, "Log level should have been INFO."


@pytest.mark.parametrize(
    "level", ["warn", "WARN", "WaRn", "wArN", "WArn", logging.WARN]
)
def test_get_logger_warn(level):
    logger = get_logger("test_logger", level=level)
    assert logger.level == logging.WARN, "Log level should have been WARN."
