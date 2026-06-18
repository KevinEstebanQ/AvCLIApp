import logging
from logging import Logger, StreamHandler, FileHandler, Formatter

class AppLogger:
    logger: Logger
    console_handler: StreamHandler
    file_handler: FileHandler
    log_formatter: Formatter
    def __init__(self, logger_name: str = "default",
                 logger_level: int = logging.DEBUG,
                 formatter_string: str = '%(asctime)s - %(levelname)s - %(message)s',
                 file_name: str = 'app.log'):
        
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logger_level)
        self.console_handler = logging.StreamHandler()
        self.file_handler = logging.FileHandler(filename=file_name)
        self.log_formatter = logging.Formatter(formatter_string)
        self.console_handler.setFormatter(self.log_formatter)
        self.file_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(self.console_handler)
        self.logger.addHandler(self.file_handler)

    def get_logger(self) -> Logger:
        return self.logger
    
