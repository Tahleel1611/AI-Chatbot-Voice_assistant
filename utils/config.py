import toml
from typing import Dict, Any
from pathlib import Path
from utils.logger import get_logger

logger = get_logger()

def load_config() -> Dict[str, Any]:
    """
    Load configuration from TOML file.
    
    Returns:
        Dict[str, Any]: Configuration dictionary
    
    Raises:
        FileNotFoundError: If config file is not found
        toml.TomlDecodeError: If config file is invalid
    """
    try:
        config_path = Path(__file__).parent.parent / "config.toml"
        
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found at {config_path}")
            
        with open(config_path, 'r') as f:
            config = toml.load(f)
            logger.info("Successfully loaded configuration")
            return config
            
    except FileNotFoundError as e:
        logger.error(f"Error loading config: {str(e)}")
        raise
        
    except toml.TomlDecodeError as e:
        logger.error(f"Invalid TOML configuration: {str(e)}")
        raise