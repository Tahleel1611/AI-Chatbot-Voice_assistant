import webbrowser
import os
import datetime
import random
from speech import say

# Function to handle task-oriented commands
def handle_task(text):
    text = text.lower()

    # Open websites
    if "open" in text:
        sites = [
            ["Google", "https://www.google.com"],
            ["YouTube", "https://www.youtube.com"],
            ["ChatGPT", "https://chat.openai.com"],
            ["GitHub", "https://github.com"],
            ["Wikipedia", "https://www.wikipedia.org"],
        ]
        for site in sites:
            if f"open {site[0].lower()}" in text:
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])
                return True

    # Tell the time
    elif "time" in text:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"The time is {current_time}")
        return True

    # Tell the date
    elif "date" in text:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        say(f"Today's date is {current_date}")
        return True

    # Open documents folder
    elif "open documents" in text:
        documents_path = os.path.expanduser("~/Documents")
        say("Opening Documents")
        os.startfile(documents_path)  # For Windows
        return True

    # Perform a web search
    elif "search" in text:
        query = text.replace("search", "").strip()
        if query:
            say(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return True
        
    # Set a reminder
    elif "set reminder" in text:
        reminder = text.replace("set reminder", "").strip()
        if reminder:
            set_reminder(reminder)
            say(f"Reminder set: {reminder}")
            return True

    # Play music
    elif "play music" in text:
        say("Playing music")
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Example: Rick Astley
        return True

    # Tell a joke
    elif "tell me a joke" in text or "joke" in text:
        joke = get_random_joke()
        say(joke)
        return True
    
    # Name
    elif "what is your name" in text:
        say("My name is Friday AI.")
        return True

    # about me
    elif "about yourself" in text:
        say("I am an AI assistant created by Tahleel. I am here to help you with your tasks.")
        return True
    
    # about creator
    elif "who is your creator" in text:
        say("My creator is Tahleel.")
        return True
    
# Function to set a reminder
def set_reminder(reminder):
    reminders_file = os.path.expanduser("/reminders.txt")
    with open(reminders_file, "a") as file:
        file.write(f"{datetime.datetime.now()}: {reminder}\n")

# Function to get a random joke
def get_random_joke():
    jokes = [
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
    return random.choice(jokes)
