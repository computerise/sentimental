"""Logging utility."""

from pathlib import Path
from logging import Logger, FileHandler, Formatter, getLogger


class Logger:
    """Logger configuration."""

    def custom_logger(
        parent_file: str,
        log_level: str = "DEBUG",
        log_format: str = ("%(asctime)s:%(levelname)s:%(message)s"),
        log_path: str = None,
    ) -> Logger:
        """Configure logger path, level and add formatting."""
        log_path = Path(log_path)
        if log_path is None:
            log_path = Path(parent_file).with_suffix(".log")
        file_handler = FileHandler(log_path)
        file_handler.setFormatter(Formatter(log_format))
        logger = getLogger()
        logger.setLevel(log_level)
        logger.addHandler(file_handler)
        return logger
