# Architecture Documentation

## Overview

The AI Chatbot Voice Assistant is designed with a modular architecture that separates concerns and promotes maintainability. The project follows a clean architecture pattern with distinct layers for presentation, business logic, and data handling.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│  ┌──────────────────────┐   ┌──────────────────────────┐  │
│  │   Voice Interface    │   │    Web Interface         │  │
│  │   (main.py)          │   │    (templates/index.html)│  │
│  └──────────────────────┘   └──────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
│  ┌──────────────────────┐   ┌──────────────────────────┐  │
│  │   Flask API          │   │   Assistant Core         │  │
│  │   (app.py)           │   │   (main.py)              │  │
│  └──────────────────────┘   └──────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     Business Logic Layer                     │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   Speech    │  │     Tasks    │  │   AI Friend      │  │
│  │  (speech.py)│  │  (task.py)   │  │(ai_friend.py)    │  │
│  └─────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      Utility Layer                           │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   Logger    │  │   Config     │  │   Constants      │  │
│  │(logger.py)  │  │(config.py)   │  │(constants.py)    │  │
│  └─────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   External Services                          │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐  │
│  │   Google    │  │  Hugging     │  │   pyttsx3        │  │
│  │   Speech    │  │   Face       │  │   TTS            │  │
│  │     API     │  │  BlenderBot  │  │                  │  │
│  └─────────────┘  └──────────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. User Interface Layer

#### Voice Interface (`main.py`)
- Entry point for voice-based interaction
- Manages the main conversation loop
- Coordinates between speech recognition, task handling, and AI responses
- Handles graceful shutdown and error recovery

#### Web Interface (`templates/index.html`, `static/`)
- Provides a web-based UI for the assistant
- Allows remote access to assistant functionality
- Responsive design for various devices

### 2. Application Layer

#### Flask API (`app.py`)
- RESTful API endpoint: `/process-command`
- Accepts JSON requests with voice commands
- Returns AI-generated responses
- Implements CORS for cross-origin requests
- Error handling and logging

#### Assistant Core (`main.py`)
- Main orchestration logic
- Manages conversation flow
- Maintains conversation history
- Integrates all components

### 3. Business Logic Layer

#### Speech Module (`speech.py`)
- **Text-to-Speech (TTS)**: Converts text responses to voice output
  - Uses pyttsx3 engine
  - Configurable voice settings
- **Speech Recognition**: Converts voice input to text
  - Uses Google Speech Recognition API
  - Handles audio capture from microphone
  - Error handling for recognition failures

#### Task Handler (`task.py`)
- Processes task-oriented commands
- Implements specific functionalities:
  - Web navigation (opening websites)
  - System information (time, date)
  - File system operations
  - Web searches
  - Reminders
  - Entertainment (music, jokes)
- Extensible design for adding new tasks

#### AI Friend (`ai_friend.py`)
- Natural language conversation using BlenderBot
- Generates context-aware responses
- Handles conversational queries not covered by tasks

### 4. Utility Layer

#### Logger (`utils/logger.py`)
- Centralized logging using loguru
- Configurable log levels
- Conversation history logging
- Error tracking and debugging

#### Configuration (`utils/config.py`)
- TOML-based configuration management
- Loads settings from `config.toml`
- Provides default values
- Validates configuration

#### Constants (`utils/constants.py`)
- Centralized constant definitions
- Error messages
- Command patterns
- Configuration defaults

## Data Flow

### Voice Command Flow

```
User speaks → Microphone capture → Speech Recognition
    → Text command → Task Handler (if task-specific)
    → AI Friend (if conversational)
    → Response text → Text-to-Speech → Audio output
```

### Web API Flow

```
HTTP Request → Flask endpoint → JSON parsing
    → AI Friend processing → Response generation
    → JSON response → HTTP Response
```

## Key Design Patterns

### 1. Separation of Concerns
- Each module has a single, well-defined responsibility
- Business logic separated from presentation and data access

### 2. Dependency Injection
- Configuration loaded at startup
- Components receive dependencies through parameters

### 3. Factory Pattern
- Logger creation through factory function
- Model initialization centralized

### 4. Error Handling
- Try-except blocks at appropriate levels
- Graceful degradation
- User-friendly error messages

## Technology Stack

### Core Technologies
- **Python 3.8+**: Primary programming language
- **Flask**: Web framework for REST API
- **Transformers**: Hugging Face library for AI models
- **PyTorch**: Deep learning backend

### Speech Technologies
- **pyttsx3**: Text-to-speech conversion
- **SpeechRecognition**: Voice input processing
- **PyAudio**: Audio I/O handling

### Supporting Libraries
- **loguru**: Advanced logging
- **python-dotenv**: Environment variable management
- **toml**: Configuration file parsing
- **flask-cors**: CORS support

## File Structure

```
AI-Chatbot-Voice_assistant/
├── main.py                 # Voice assistant entry point
├── app.py                  # Flask web API
├── ai_friend.py            # AI conversation module
├── speech.py               # Speech I/O module
├── task.py                 # Task handler
├── config.toml             # Configuration file
├── requirements.txt        # Python dependencies
├── utils/
│   ├── config.py          # Configuration loader
│   ├── logger.py          # Logging setup
│   └── constants.py       # Constants definitions
├── static/
│   ├── styles.css         # Web UI styles
│   └── main.js            # Web UI JavaScript
├── templates/
│   └── index.html         # Web UI template
└── logs/                  # Conversation logs

```

## Configuration Management

Configuration is managed through multiple layers:

1. **config.toml**: Primary configuration file
   - Assistant settings
   - Speech parameters
   - Logging configuration

2. **.env**: Environment-specific settings (optional)
   - API keys
   - Secret keys
   - Environment-specific overrides

3. **constants.py**: Hard-coded constants
   - Error messages
   - Default values

## Extensibility

The architecture is designed for easy extension:

### Adding New Tasks
1. Add new condition in `task.py`
2. Implement handler function
3. Update documentation

### Adding New AI Models
1. Modify `ai_friend.py`
2. Update dependencies in `requirements.txt`
3. Adjust configuration if needed

### Adding New APIs
1. Add new route in `app.py`
2. Implement endpoint logic
3. Update API documentation

## Security Considerations

- Environment variables for sensitive data
- Input validation for API endpoints
- Error messages don't expose sensitive information
- CORS configured for security
- No hardcoded credentials

## Performance Considerations

- Model loaded once at startup
- Lazy loading where appropriate
- Efficient audio processing
- Minimal memory footprint
- Async operations for non-blocking I/O

## Future Improvements

1. **Database Integration**: Store conversation history persistently
2. **User Authentication**: Multi-user support with authentication
3. **Plugin System**: Dynamic task loading
4. **Cloud Deployment**: Containerization and cloud hosting
5. **Advanced NLP**: Better context understanding
6. **Multi-language Support**: Beyond English
7. **Voice Customization**: Multiple voice options
8. **Performance Monitoring**: Metrics and analytics
