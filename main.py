from speech import say, take_command
from task import handle_task
from ai_friend import ask_ai_friend
from utils.logger import get_logger
from utils.config import load_config
from utils.constants import ERROR_MESSAGES

logger = get_logger()


def daily_assistant():
    """
    Main assistant loop that handles user interactions and commands.
    """
    try:
        config = load_config()
        logger.info("Starting assistant with configuration:")
        logger.info(f"Language: {config['settings']['language']}")
        logger.info(f"Pause threshold: {config['settings']['pause_threshold']}")

        say(config['greetings']['welcome'])
        conversation_history = []

        while True:
            try:
                logger.info("Listening for command...")
                text = take_command()

                if text == "None":
                    logger.info("No command detected")
                    continue

                logger.info(f"Received command: {text}")

                # Handle task-oriented commands
                if handle_task(text):
                    continue

                # Handle AI friend functionality
                response = ask_ai_friend(text)
                say(response)
                conversation_history.append(f"You: {text}")
                conversation_history.append(f"AI Friend: {response}")

                # Exit command
                if any(word in text.lower() for word in config['exit_commands']):
                    say(config['greetings']['goodbye'])
                    break

            except KeyboardInterrupt:
                logger.info("Assistant interrupted by user")
                say("Assistant interrupted. Goodbye!")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {str(e)}")
                say(ERROR_MESSAGES["unknown_command"])

    except Exception as e:
        logger.error(f"Critical error in daily_assistant: {str(e)}")
        raise


if __name__ == '__main__':
    try:
        logger.info("Starting Daily Assistant...")
        daily_assistant()
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")