from bot.logging_config import setup_logger

logger = setup_logger()

logger.info("Application Started")
logger.warning("Warning Example")
logger.error("Error Example")