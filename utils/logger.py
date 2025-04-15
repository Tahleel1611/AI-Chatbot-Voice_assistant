from loguru import logger
import os
from datetime import datetime

# Configure logger
log_file = os.path.join(os.path.dirname(__file__), "../logs/daily_assistant_{time}.log")
logger.add(
    log_file,
    rotation="00:00",
    retention="10 days",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
)

def get_logger():
    """
    Get the configured logger instance.
    
    Returns:
        logger: Configured logger instance
    """
    return logger