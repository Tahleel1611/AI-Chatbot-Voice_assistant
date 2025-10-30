# 🤖 AI Chatbot Voice Assistant

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Maintenance](https://img.shields.io/badge/maintained-yes-brightgreen.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**A sophisticated AI-powered voice assistant that combines natural language processing with task automation to provide an intelligent, hands-free computing experience.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Documentation](#-api-documentation) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Screenshots](#-screenshots)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)

---

## 🎯 About

The **AI Chatbot Voice Assistant** (also known as "Friday AI") is a versatile, intelligent voice assistant that leverages cutting-edge AI technology to understand and respond to natural language commands. Whether you need to automate tasks, get information, or simply have a conversation, this assistant is designed to make your computing experience more intuitive and efficient.

### Key Highlights

✨ **Intelligent Conversation** - Powered by Hugging Face's BlenderBot for natural, context-aware responses

🎤 **Voice Control** - Hands-free operation using advanced speech recognition

🌐 **Web API** - RESTful API for integration with web and mobile applications

🛠️ **Task Automation** - Execute common tasks through simple voice commands

📝 **Conversation Logging** - Automatic logging of all interactions for review and debugging

🔧 **Highly Configurable** - Customize behavior through configuration files and environment variables

---

## ✨ Features

### 🗣️ Voice Interaction
- **Speech Recognition**: Convert speech to text using Google Speech Recognition API
- **Text-to-Speech**: Natural voice output using pyttsx3 engine
- **Multi-language Support**: Configurable language settings (default: English-India)
- **Adjustable Sensitivity**: Customizable pause threshold for speech detection

### 🤖 AI-Powered Conversation
- **Natural Language Understanding**: Context-aware responses using BlenderBot
- **General Knowledge**: Answer questions on various topics
- **Conversational Memory**: Maintains conversation history during session
- **Personality**: Friendly, helpful AI personality

### 🎯 Task Automation
- **🌐 Web Navigation**: Open popular websites (Google, YouTube, GitHub, Wikipedia, ChatGPT)
- **🔍 Web Search**: Perform Google searches through voice commands
- **⏰ Time & Date**: Get current time and date information
- **📁 File Management**: Open documents and folders
- **🎵 Music Playback**: Play music through web services
- **😄 Entertainment**: Tell jokes and provide entertainment
- **⏲️ Reminders**: Set and manage reminders
- **ℹ️ System Information**: Query assistant information and capabilities

### 🌐 Web API
- **REST Endpoints**: Process commands remotely via HTTP
- **CORS Support**: Cross-origin requests enabled
- **JSON Responses**: Structured, easy-to-parse responses
- **Error Handling**: Comprehensive error messages and status codes
- **Web Interface**: Modern, responsive web UI included

### 📊 Logging & Monitoring
- **Structured Logging**: Advanced logging using loguru
- **Conversation History**: Automatic logging of all interactions
- **Error Tracking**: Detailed error logs for debugging
- **Configurable Log Levels**: Adjust verbosity as needed

---

## 🛠️ Technology Stack

### Core Technologies
- **Python 3.8+** - Primary programming language
- **Flask** - Web framework for REST API
- **Transformers (Hugging Face)** - AI model library
- **PyTorch** - Deep learning backend

### Speech Technologies
- **pyttsx3** - Text-to-speech conversion
- **SpeechRecognition** - Voice input processing
- **PyAudio** - Audio I/O handling

### Supporting Libraries
- **loguru** - Advanced logging functionality
- **python-dotenv** - Environment variable management
- **toml** - Configuration file parsing
- **flask-cors** - Cross-Origin Resource Sharing

---

## 📥 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **pip** (Python package manager, usually comes with Python)
- **Git** (for cloning the repository)
- **Microphone and speakers** (for voice interaction)

**System-specific requirements:**

- **Windows**: No additional requirements
- **macOS**: May need to install PortAudio: `brew install portaudio`
- **Linux**: Install PortAudio development files:
  ```bash
  sudo apt-get install portaudio19-dev python3-pyaudio
  ```

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/Tahleel1611/AI-Chatbot-Voice_assistant.git
cd AI-Chatbot-Voice_assistant
```

#### 2. Create Virtual Environment

Creating a virtual environment is recommended to avoid dependency conflicts:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

> **Note**: The first run may take longer as it downloads the BlenderBot AI model (approximately 1.6GB).

#### 4. Configure Environment (Optional)

```bash
cp .env.example .env
# Edit .env with your preferred settings
```

#### 5. Verify Installation

Test that everything is installed correctly:

```bash
python -c "import pyttsx3, speech_recognition, transformers, flask; print('All dependencies installed successfully!')"
```

---

## 🚀 Usage

The assistant can be run in two modes: **Voice Assistant Mode** and **Web API Mode**.

### Voice Assistant Mode

Run the voice-controlled assistant that listens to your microphone:

```bash
python main.py
```

**Example Interaction:**
```
Assistant: Hello, I am your AI assistant. How can I assist you today?
You: What time is it?
Assistant: The time is 14:30:45
You: Tell me a joke
Assistant: Why don't scientists trust atoms? Because they make up everything!
You: Open YouTube
Assistant: Opening YouTube
```

### Web API Mode

Run the Flask web server to access the assistant through a web interface or API:

```bash
python app.py
```

Then open your browser and navigate to: **http://localhost:5000**

### Available Voice Commands

#### General Conversation
- "Hello" / "Hi"
- "How are you?"
- "What can you help me with?"
- Any general question or conversation

#### Information Queries
- "What time is it?"
- "What's the date?"
- "What is your name?"
- "Who is your creator?"
- "Tell me about yourself"

#### Web Navigation
- "Open Google"
- "Open YouTube"
- "Open ChatGPT"
- "Open GitHub"
- "Open Wikipedia"

#### Web Search
- "Search for [query]"
- Example: "Search for Python tutorials"

#### Task Management
- "Set reminder [reminder text]"
- "Open documents"

#### Entertainment
- "Tell me a joke"
- "Play music"

#### Exit
- "Exit"
- "Goodbye"
- "Quit"
- "Stop"

---

## 📡 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Home Page
```http
GET /
```
Returns the web interface.

#### 2. Process Command
```http
POST /process-command
Content-Type: application/json

{
  "command": "Your command here"
}
```

**Response:**
```json
{
  "response": "AI-generated response"
}
```

**Example using cURL:**
```bash
curl -X POST http://localhost:5000/process-command \
  -H "Content-Type: application/json" \
  -d '{"command": "Hello, how are you?"}'
```

**Example using Python:**
```python
import requests

response = requests.post(
    'http://localhost:5000/process-command',
    json={'command': 'What time is it?'}
)
print(response.json()['response'])
```

**Example using JavaScript:**
```javascript
fetch('http://localhost:5000/process-command', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({command: 'Tell me a joke'})
})
.then(res => res.json())
.then(data => console.log(data.response));
```

For detailed API documentation, see [docs/API.md](docs/API.md).

---

## 📁 Project Structure

```
AI-Chatbot-Voice_assistant/
│
├── main.py                  # Voice assistant entry point
├── app.py                   # Flask web API server
├── ai_friend.py             # AI conversation module (BlenderBot)
├── speech.py                # Speech recognition and TTS
├── task.py                  # Task handler for commands
│
├── utils/                   # Utility modules
│   ├── config.py           # Configuration loader
│   ├── logger.py           # Logging setup
│   └── constants.py        # Constants and error messages
│
├── static/                  # Web UI static files
│   ├── styles.css          # CSS styling
│   └── main.js             # JavaScript functionality
│
├── templates/               # HTML templates
│   └── index.html          # Web interface
│
├── logs/                    # Conversation logs (auto-generated)
│
├── docs/                    # Additional documentation
│   ├── ARCHITECTURE.md     # System architecture
│   ├── API.md              # API documentation
│   └── DEPLOYMENT.md       # Deployment guide
│
├── .github/                 # GitHub templates
│   ├── ISSUE_TEMPLATE/     # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
│
├── config.toml              # Configuration file
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
│
├── README.md               # This file
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contributing guidelines
├── CODE_OF_CONDUCT.md      # Code of conduct
└── CHANGELOG.md            # Version history
```

### Module Descriptions

- **main.py**: Main entry point for voice-controlled assistant
- **app.py**: Flask web server for API access
- **ai_friend.py**: Integration with BlenderBot AI model
- **speech.py**: Handles speech recognition and text-to-speech
- **task.py**: Processes task-oriented commands
- **utils/**: Helper modules for configuration, logging, and constants

---

## ⚙️ Configuration

### Configuration File (config.toml)

The `config.toml` file contains all configurable settings:

```toml
[assistant]
name = "Friday AI"
version = "1.0.0"

[greetings]
welcome = "Hello, I am your AI assistant. How can I assist you today?"
goodbye = "Goodbye! Have a great day!"

[settings]
language = "en-in"           # Speech recognition language
pause_threshold = 1.0        # Pause detection threshold (seconds)
max_retries = 3             # Maximum retry attempts
speech_timeout = 5          # Speech timeout (seconds)

exit_commands = ["exit", "goodbye", "quit", "stop"]

[logging]
level = "INFO"              # Log level (DEBUG, INFO, WARNING, ERROR)
```

### Environment Variables (.env)

Create a `.env` file from `.env.example` for environment-specific settings:

```bash
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_PORT=5000
LOG_LEVEL=INFO
```

See [.env.example](.env.example) for all available options.

---

## 📸 Screenshots

### Web Interface
![Web Interface](docs/images/web-interface.png)
*Coming soon: Modern web interface for browser-based interaction*

### Voice Assistant in Action
![Voice Assistant](docs/images/voice-assistant.png)
*Coming soon: Console output showing voice interaction*

---

## 🔧 Troubleshooting

### Common Issues

#### 1. PyAudio Installation Fails

**Windows:**
- Download pre-built wheel from [PyAudio wheels](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- Install: `pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl`

**Linux:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
pip install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

#### 2. Microphone Not Detected

- Check system microphone permissions
- Verify microphone is working in system settings
- Try listing available devices:
```python
import speech_recognition as sr
print(sr.Microphone.list_microphone_names())
```

#### 3. Model Download Issues

If the BlenderBot model fails to download:
```bash
# Clear cache and retry
rm -rf ~/.cache/huggingface
python -c "from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration; BlenderbotTokenizer.from_pretrained('facebook/blenderbot-400M-distill'); BlenderbotForConditionalGeneration.from_pretrained('facebook/blenderbot-400M-distill')"
```

#### 4. Speech Recognition Not Working

- Ensure you have an active internet connection (Google Speech Recognition requires internet)
- Check microphone permissions in system settings
- Adjust the `pause_threshold` in `config.toml`

#### 5. Port Already in Use

If port 5000 is already in use:
```bash
# Find process using port 5000
lsof -i :5000  # Linux/macOS
netstat -ano | findstr :5000  # Windows

# Kill the process or change port in app.py
```

### Getting Help

If you encounter issues not listed here:
1. Check [existing issues](https://github.com/Tahleel1611/AI-Chatbot-Voice_assistant/issues)
2. Review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for system details
3. Create a [new issue](https://github.com/Tahleel1611/AI-Chatbot-Voice_assistant/issues/new) with details

---

## 🤝 Contributing

We welcome contributions from the community! Whether it's bug fixes, new features, documentation improvements, or suggestions, your help is appreciated.

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Follow our code style guidelines
4. **Test thoroughly**: Ensure all functionality works
5. **Commit your changes**: `git commit -m 'Add amazing feature'`
6. **Push to the branch**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code
- Write clear, descriptive commit messages
- Update documentation for new features
- Add tests for new functionality
- Ensure all tests pass before submitting PR

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Tahleel1611

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

---

## 🙏 Acknowledgments

### Technologies & Libraries
- [Hugging Face Transformers](https://huggingface.co/transformers/) - For the BlenderBot AI model
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [pyttsx3](https://pyttsx3.readthedocs.io/) - Text-to-speech conversion
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Speech recognition library
- [PyTorch](https://pytorch.org/) - Deep learning framework
- [loguru](https://github.com/Delgan/loguru) - Logging library

### Inspiration
- Inspired by popular AI assistants like Siri, Alexa, and Google Assistant
- Built with the goal of creating an open-source, customizable voice assistant

### Special Thanks
- Thanks to all contributors who help improve this project
- The open-source community for providing excellent tools and libraries

---

## 📞 Contact

**Tahleel1611**

- GitHub: [@Tahleel1611](https://github.com/Tahleel1611)
- Project Link: [https://github.com/Tahleel1611/AI-Chatbot-Voice_assistant](https://github.com/Tahleel1611/AI-Chatbot-Voice_assistant)

### Support

- 📫 **Issues**: [GitHub Issues](https://github.com/Tahleel1611/AI-Chatbot-Voice_assistant/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Tahleel1611/AI-Chatbot-Voice_assistant/discussions)
- 📖 **Documentation**: [docs/](docs/)

---

## 🌟 Star History

If you find this project useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=Tahleel1611/AI-Chatbot-Voice_assistant&type=Date)](https://star-history.com/#Tahleel1611/AI-Chatbot-Voice_assistant&Date)

---

<div align="center">

**Made with ❤️ by Tahleel1611**

[⬆ Back to Top](#-ai-chatbot-voice-assistant)

</div>
