import pyttsx3
import speech_recognition as sr
from utils.logger import get_logger
from utils.config import load_config
from utils.constants import ERROR_MESSAGES

logger = get_logger()

# Initialize text-to-speech engine
engine = pyttsx3.init()


def say(text: str) -> None:
    """
    Speak the given text using text-to-speech.
    
    Args:
        text: The text to be spoken
    """
    try:
        logger.info(f"Speaking: {text}")
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        logger.error(f"Error in speech synthesis: {str(e)}")
        raise


def take_command() -> str:
    """
    Listen for and recognize speech input.
    
    Returns:
        Recognized text or "None" if recognition fails
    """
    try:
        logger.info("Starting to listen for command")
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            logger.info("Listening...")
            r.pause_threshold = load_config()['settings']['pause_threshold']
            audio = r.listen(source)
            
        try:
            logger.info("Recognizing speech...")
            query = r.recognize_google(audio, language=load_config()['settings']['language'])
            logger.info(f"Recognized: {query}")
            return query
            
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            say(ERROR_MESSAGES["speech_recognition"])
            return "None"
            
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service: {str(e)}")
            say(ERROR_MESSAGES["web_service"])
            return "None"
            
    except Exception as e:
        logger.error(f"Error in speech recognition: {str(e)}")
        say(ERROR_MESSAGES["speech_recognition"])
        return "None"