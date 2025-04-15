"""
Constants for the daily assistant project.
"""

# Speech recognition settings
SPEECH_RECOGNITION_TIMEOUT = 5  # seconds
MAX_RETRIES = 3

# Web browser settings
DEFAULT_BROWSERS = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "chatgpt": "https://chat.openai.com",
    "github": "https://github.com",
    "wikipedia": "https://www.wikipedia.org"
}

# File paths
LOGS_DIR = "logs"
CONFIG_FILE = "config.toml"

# Error messages
ERROR_MESSAGES = {
    "speech_recognition": "Sorry, I encountered an error with the speech recognition system.",
    "speech_synthesis": "Sorry, I encountered an error with the speech synthesis system.",
    "web_service": "Sorry, I'm having trouble connecting to the service.",
    "unknown_command": "I'm not sure how to help with that. Could you please rephrase your request?"
}