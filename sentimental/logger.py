"""Logging utility."""

from logging import Logger, FileHandler, Formatter, getLogger

from sentimental.extension_handler import ExtensionHandler


class Logger:
    """Logger configuration."""

    def custom_logger(
        parent_file: str, log_level="DEBUG", log_format=("%(asctime)s:%(levelname)s:%(message)s"), log_path=None
    ) -> Logger:
        """Configure logger path, level and add formatting."""
        if log_path is None:
            log_path = ExtensionHandler.change_file_extension(parent_file, ".log")
        file_handler = FileHandler(log_path)
        file_handler.setFormatter(Formatter(log_format))
        logger = getLogger()
        logger.setLevel(log_level)
        logger.addHandler(file_handler)
        return logger
