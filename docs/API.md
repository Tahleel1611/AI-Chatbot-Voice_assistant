# API Documentation

## Overview

The AI Chatbot Voice Assistant provides a REST API built with Flask that allows remote access to the assistant's capabilities. This API enables integration with web applications, mobile apps, or other services.

## Base URL

```
http://localhost:5000
```

For production deployments, replace with your actual domain.

## Authentication

Currently, the API does not require authentication. For production use, consider implementing:
- API keys
- OAuth 2.0
- JWT tokens

## Endpoints

### 1. Get Home Page

Serves the web interface for the assistant.

**Endpoint:** `GET /`

**Description:** Returns the HTML interface for browser-based interaction.

**Response:**
- **Content-Type:** `text/html`
- **Status Code:** `200 OK`

**Example:**

```bash
curl http://localhost:5000/
```

---

### 2. Process Command

Processes a text command and returns an AI-generated response.

**Endpoint:** `POST /process-command`

**Description:** Accepts a text command and returns an intelligent response from the AI assistant.

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**

```json
{
  "command": "string"
}
```

**Parameters:**

| Parameter | Type   | Required | Description                           |
|-----------|--------|----------|---------------------------------------|
| command   | string | Yes      | The text command to process           |

**Response:**

**Success Response (200 OK):**

```json
{
  "response": "string"
}
```

**Error Responses:**

**400 Bad Request** - No command provided:
```json
{
  "error": "No command provided"
}
```

**500 Internal Server Error** - Processing error:
```json
{
  "error": "An error occurred while processing the command"
}
```

**Example Usage:**

```bash
# Using curl
curl -X POST http://localhost:5000/process-command \
  -H "Content-Type: application/json" \
  -d '{"command": "Hello, how are you?"}'
```

```python
# Using Python requests
import requests

url = "http://localhost:5000/process-command"
payload = {"command": "What's the weather like?"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

```javascript
// Using JavaScript fetch
fetch('http://localhost:5000/process-command', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    command: 'Tell me a joke'
  })
})
.then(response => response.json())
.then(data => console.log(data.response));
```

---

## Response Examples

### Conversational Query

**Request:**
```json
{
  "command": "What can you help me with?"
}
```

**Response:**
```json
{
  "response": "I can help you with various tasks like opening websites, telling you the time and date, searching the web, setting reminders, playing music, telling jokes, and having conversations. Just ask me anything!"
}
```

### Task-Based Command

**Request:**
```json
{
  "command": "What time is it?"
}
```

**Response:**
```json
{
  "response": "The time is 14:30:45"
}
```

### General Conversation

**Request:**
```json
{
  "command": "How are you today?"
}
```

**Response:**
```json
{
  "response": "I'm doing great, thank you for asking! I'm here to help you with whatever you need. How can I assist you today?"
}
```

---

## Error Handling

The API uses standard HTTP status codes to indicate success or failure:

| Status Code | Meaning                                      |
|-------------|----------------------------------------------|
| 200         | Success - Request processed successfully     |
| 400         | Bad Request - Invalid or missing parameters  |
| 500         | Internal Server Error - Server-side error    |

All error responses include a JSON object with an `error` field describing the issue.

---

## CORS Support

The API supports Cross-Origin Resource Sharing (CORS), allowing requests from web applications hosted on different domains.

**Allowed Methods:** GET, POST, OPTIONS

**Allowed Headers:** Content-Type, Authorization

---

## Rate Limiting

Currently, no rate limiting is implemented. For production use, consider:
- Implementing rate limiting to prevent abuse
- Using tools like Flask-Limiter
- Setting reasonable limits (e.g., 100 requests per minute)

---

## Best Practices

### 1. Input Validation

Always validate and sanitize user input:

```python
def is_valid_command(command):
    if not command or not isinstance(command, str):
        return False
    if len(command) > 500:  # Maximum length
        return False
    return True
```

### 2. Error Handling

Implement proper error handling in your client code:

```python
try:
    response = requests.post(url, json=payload, timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except ValueError as e:
    print(f"Invalid JSON response: {e}")
```

### 3. Timeout Configuration

Set appropriate timeouts to avoid hanging requests:

```python
response = requests.post(url, json=payload, timeout=10)
```

### 4. Retry Logic

Implement retry logic for transient failures:

```python
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=0.3)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
```

---

## Integration Examples

### Web Application (React)

```javascript
import React, { useState } from 'react';

function AssistantChat() {
  const [command, setCommand] = useState('');
  const [response, setResponse] = useState('');

  const sendCommand = async () => {
    try {
      const res = await fetch('http://localhost:5000/process-command', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command })
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error('Error:', error);
      setResponse('Error processing command');
    }
  };

  return (
    <div>
      <input 
        value={command} 
        onChange={(e) => setCommand(e.target.value)}
        placeholder="Enter command"
      />
      <button onClick={sendCommand}>Send</button>
      <p>Response: {response}</p>
    </div>
  );
}
```

### Python Script

```python
import requests
import json

class AssistantClient:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def send_command(self, command):
        """Send a command to the assistant."""
        url = f"{self.base_url}/process-command"
        payload = {"command": command}
        
        try:
            response = self.session.post(
                url, 
                json=payload,
                timeout=10
            )
            response.raise_for_status()
            return response.json()["response"]
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

# Usage
client = AssistantClient()
response = client.send_command("Hello, how are you?")
print(f"Assistant: {response}")
```

### Mobile App (Flutter)

```dart
import 'dart:convert';
import 'package:http/http.dart' as http;

class AssistantService {
  final String baseUrl = 'http://localhost:5000';

  Future<String> sendCommand(String command) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/process-command'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'command': command}),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        return data['response'];
      } else {
        throw Exception('Failed to process command');
      }
    } catch (e) {
      print('Error: $e');
      return 'Error processing command';
    }
  }
}
```

---

## Testing the API

### Using Postman

1. Create a new POST request
2. Set URL to `http://localhost:5000/process-command`
3. Set Headers: `Content-Type: application/json`
4. Set Body (raw JSON):
   ```json
   {
     "command": "Your command here"
   }
   ```
5. Send the request

### Using pytest

```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_process_command(client):
    response = client.post('/process-command',
                          json={'command': 'hello'},
                          content_type='application/json')
    assert response.status_code == 200
    data = response.get_json()
    assert 'response' in data

def test_missing_command(client):
    response = client.post('/process-command',
                          json={},
                          content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
```

---

## Future API Enhancements

### Planned Features

1. **WebSocket Support**: Real-time bidirectional communication
2. **Streaming Responses**: Stream long responses chunk by chunk
3. **Conversation History**: Endpoint to retrieve past conversations
4. **User Sessions**: Multi-user support with session management
5. **Voice Endpoints**: Direct audio input/output endpoints
6. **Task Management**: CRUD operations for reminders and tasks
7. **Analytics**: Usage statistics and metrics
8. **Webhooks**: Event notifications for integrations

### Potential New Endpoints

```
POST   /api/v1/voice/upload       # Upload audio file
GET    /api/v1/conversations      # Get conversation history
POST   /api/v1/tasks              # Create a task/reminder
GET    /api/v1/tasks/:id          # Get specific task
PUT    /api/v1/tasks/:id          # Update task
DELETE /api/v1/tasks/:id          # Delete task
GET    /api/v1/stats              # Usage statistics
```

---

## Support

For API-related issues or questions:
- Open an issue on GitHub
- Check the troubleshooting guide
- Review the CONTRIBUTING.md for development guidelines

---

## Changelog

See [CHANGELOG.md](../CHANGELOG.md) for API version history and updates.
