# Contributing to AI Chatbot Voice Assistant

First off, thank you for considering contributing to AI Chatbot Voice Assistant! It's people like you that make this project great.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
  - [Git Commit Messages](#git-commit-messages)
  - [Python Style Guide](#python-style-guide)
- [Additional Notes](#additional-notes)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

**Use the bug report template** which includes:

- A clear and descriptive title
- Detailed steps to reproduce the problem
- Expected behavior vs. actual behavior
- Screenshots or error messages (if applicable)
- Your environment (OS, Python version, etc.)

### Suggesting Features

Feature requests are welcome! Before submitting:

1. Check if the feature has already been suggested
2. Provide a clear description of the feature
3. Explain why this feature would be useful
4. Consider the scope and feasibility

**Use the feature request template** to structure your suggestion.

### Pull Requests

We actively welcome your pull requests:

1. **Fork the repository** and create your branch from `main`
2. **Follow the development setup** instructions below
3. **Make your changes** following our style guidelines
4. **Test your changes** thoroughly
5. **Update documentation** if necessary
6. **Submit a pull request** with a clear description

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Steps

1. **Clone your fork:**
   ```bash
   git clone https://github.com/your-username/AI-Chatbot-Voice_assistant.git
   cd AI-Chatbot-Voice_assistant
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application:**
   ```bash
   # For voice assistant
   python main.py

   # For web API
   python app.py
   ```

## Style Guidelines

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

**Examples:**
```
Add voice command for weather information

- Integrate weather API
- Add weather query parsing
- Update documentation

Fixes #123
```

### Python Style Guide

We follow **PEP 8** conventions with some additions:

#### Code Formatting

- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use meaningful variable and function names
- Add docstrings to all functions, classes, and modules

#### Example:

```python
def process_voice_command(command: str) -> dict:
    """
    Process a voice command and return the appropriate response.
    
    Args:
        command: The voice command string to process
        
    Returns:
        dict: A dictionary containing the response and metadata
        
    Raises:
        ValueError: If command is empty or invalid
    """
    if not command:
        raise ValueError("Command cannot be empty")
    
    # Process command logic here
    return {"response": "Processed", "status": "success"}
```

#### Import Organization

```python
# Standard library imports
import os
import sys

# Third-party imports
import flask
from transformers import BlenderbotTokenizer

# Local imports
from utils.logger import get_logger
from speech import say
```

#### Type Hints

Use type hints where appropriate:

```python
def calculate_confidence(text: str, threshold: float = 0.8) -> bool:
    """Check if confidence exceeds threshold."""
    pass
```

#### Error Handling

Always handle exceptions appropriately:

```python
try:
    result = risky_operation()
except SpecificException as e:
    logger.error(f"Error occurred: {e}")
    # Handle error gracefully
```

#### Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Keep README.md and other documentation up-to-date
- Add inline comments for complex logic

### Testing

- Write tests for new features
- Ensure existing tests pass
- Aim for good test coverage
- Use descriptive test names

## Additional Notes

### Issue and Pull Request Labels

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

### Questions?

Feel free to open an issue with your question or reach out to the maintainers.

---

Thank you for contributing to AI Chatbot Voice Assistant! 🎉
