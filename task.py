import webbrowser
import os
import datetime
import random
import platform
from typing import Optional
from speech import say

class TaskHandler:
    """
    Enhanced task handler with better command parsing and extensibility.
    """
    
    def __init__(self):
        self.websites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "chatgpt": "https://chat.openai.com",
            "github": "https://github.com",
            "wikipedia": "https://www.wikipedia.org",
            "reddit": "https://www.reddit.com",
            "stackoverflow": "https://stackoverflow.com",
        }
        
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "What do you get when you cross a snowman and a vampire? Frostbite!",
            "How does a penguin build its house? Igloos it together!",
            "Why did the math book look sad? Because it had too many problems.",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
        ]
        
        self.reminders_file = os.path.expanduser("~/reminders.txt")
    
    def handle_task(self, text: str) -> bool:
        """
        Process task-oriented commands.
        
        Args:
            text: User command text
        
        Returns:
            bool: True if task was handled, False otherwise
        """
        if not text:
            return False
        
        text_lower = text.lower().strip()
        
        # Open websites
        if "open" in text_lower:
            return self._handle_open_website(text_lower)
        
        # Time query
        elif "time" in text_lower:
            return self._handle_time()
        
        # Date query
        elif "date" in text_lower:
            return self._handle_date()
        
        # Web search
        elif "search" in text_lower or "google" in text_lower:
            return self._handle_search(text)
        
        # Reminders
        elif "reminder" in text_lower:
            return self._handle_reminder(text)
        
        # Music
        elif "play music" in text_lower or "music" in text_lower:
            return self._handle_music()
        
        # Jokes
        elif "joke" in text_lower:
            return self._handle_joke()
        
        # System information
        elif "system info" in text_lower or "system information" in text_lower:
            return self._handle_system_info()
        
        # Assistant information
        elif "your name" in text_lower:
            return self._handle_name()
        elif "about yourself" in text_lower or "who are you" in text_lower:
            return self._handle_about()
        elif "your creator" in text_lower or "who created you" in text_lower:
            return self._handle_creator()
        
        # File operations
        elif "open documents" in text_lower or "open folder" in text_lower:
            return self._handle_open_folder(text_lower)
        
        return False
    
    def _handle_open_website(self, text: str) -> bool:
        """Handle website opening commands."""
        for site_name, url in self.websites.items():
            if f"open {site_name}" in text or site_name in text:
                say(f"Opening {site_name.title()}")
                try:
                    webbrowser.open(url)
                    return True
                except Exception as e:
                    say(f"Sorry, I couldn't open {site_name}")
                    return False
        return False
    
    def _handle_time(self) -> bool:
        """Handle time query."""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        say(f"The time is {current_time}")
        return True
    
    def _handle_date(self) -> bool:
        """Handle date query."""
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        day_of_week = datetime.datetime.now().strftime("%A")
        say(f"Today is {day_of_week}, {current_date}")
        return True
    
    def _handle_search(self, text: str) -> bool:
        """Handle web search commands."""
        # Extract search query
        query = text.lower().replace("search", "").replace("google", "").replace("for", "").strip()
        if query:
            say(f"Searching for {query}")
            try:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                return True
            except Exception:
                say("Sorry, I couldn't perform the search")
                return False
        return False
    
    def _handle_reminder(self, text: str) -> bool:
        """Handle reminder setting."""
        reminder_text = text.lower().replace("set reminder", "").replace("remind me", "").strip()
        if reminder_text:
            try:
                with open(self.reminders_file, "a") as file:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f"[{timestamp}] {reminder_text}\n")
                say(f"Reminder set: {reminder_text}")
                return True
            except Exception:
                say("Sorry, I couldn't set the reminder")
                return False
        return False
    
    def _handle_music(self) -> bool:
        """Handle music playback."""
        say("Playing music")
        try:
            webbrowser.open("https://www.youtube.com/results?search_query=popular+music")
            return True
        except Exception:
            say("Sorry, I couldn't play music")
            return False
    
    def _handle_joke(self) -> bool:
        """Handle joke requests."""
        joke = random.choice(self.jokes)
        say(joke)
        return True
    
    def _handle_system_info(self) -> bool:
        """Handle system information requests."""
        system = platform.system()
        release = platform.release()
        say(f"You are running {system} version {release}")
        return True
    
    def _handle_name(self) -> bool:
        """Handle name query."""
        say("My name is Friday AI, your intelligent assistant.")
        return True
    
    def _handle_about(self) -> bool:
        """Handle about query."""
        say("I am Friday AI, an intelligent voice assistant created by Tahleel. I can help you with various tasks like opening websites, searching the web, setting reminders, and answering your questions.")
        return True
    
    def _handle_creator(self) -> bool:
        """Handle creator query."""
        say("I was created by Tahleel, a talented developer passionate about AI and automation.")
        return True
    
    def _handle_open_folder(self, text: str) -> bool:
        """Handle folder opening commands."""
        try:
            if "documents" in text:
                path = os.path.expanduser("~/Documents")
            elif "downloads" in text:
                path = os.path.expanduser("~/Downloads")
            elif "desktop" in text:
                path = os.path.expanduser("~/Desktop")
            else:
                return False
            
            say(f"Opening {os.path.basename(path)} folder")
            
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":  # macOS
                os.system(f"open '{path}'")
            else:  # Linux
                os.system(f"xdg-open '{path}'")
            
            return True
        except Exception:
            say("Sorry, I couldn't open the folder")
            return False

# Create a global instance for backward compatibility
_task_handler = TaskHandler()

def handle_task(text: str) -> bool:
    """
    Legacy function for backward compatibility.
    
    Args:
        text: User command text
    
    Returns:
        bool: True if task was handled, False otherwise
    """
    return _task_handler.handle_task(text)
