import logging

from extension_handler import ExtensionHandler


class Logger:
    """Logger configuration."""

    def custom_logger(parent_file: str,
                      log_level='DEBUG',
                      log_format=(
                          '%(asctime)s:%(levelname)s:%(message)s'),
                      log_path=None):
        """Configure logger path, level and add formatting."""

        def build_logger(log_path, log_format, log_level):
            def configure_file_handler(log_path, log_format):
                """Set format and file path for the log."""
                file_handler = logging.FileHandler(log_path)
                formatter = logging.Formatter(log_format)
                file_handler.setFormatter(formatter)
                return file_handler
            logger = logging.getLogger()
            logger.setLevel(log_level)
            logger.addHandler(configure_file_handler(log_path, log_format))
            return logger

        if log_path is None:
            log_path = ExtensionHandler.change_file_extension(
                parent_file, '.log')
        return build_logger(log_path, log_format, log_level)
