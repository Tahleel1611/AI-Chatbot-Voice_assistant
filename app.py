from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from ai_friend import ask_ai_friend, clear_conversation_history
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join('logs', f'app_{datetime.now().strftime("%Y%m%d")}.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Configuration
app.config['JSON_SORT_KEYS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max request size

@app.route('/')
def index():
    """Serve the main web interface."""
    try:
        logger.info("Serving index page")
        return render_template('index.html')
    except Exception as e:
        logger.error(f"Error serving index page: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/process-command', methods=['POST'])
def handle_command():
    """
    Process user commands via POST request.
    
    Expected JSON payload:
    {
        "command": "user command text"
    }
    
    Returns:
    {
        "response": "AI response text"
    }
    """
    try:
        # Validate request
        if not request.is_json:
            logger.warning("Received non-JSON request")
            return jsonify({"error": "Content-Type must be application/json"}), 400
        
        data = request.json
        command = data.get('command', '').strip()
        
        # Validate command
        if not command:
            logger.warning("Empty command received")
            return jsonify({"error": "No command provided"}), 400
        
        if len(command) > 1000:
            logger.warning(f"Command too long: {len(command)} characters")
            return jsonify({"error": "Command too long. Maximum 1000 characters."}), 400
        
        logger.info(f"Processing command: {command[:100]}...")  # Log first 100 chars
        
        # Get AI response
        ai_response = ask_ai_friend(command)
        
        logger.info(f"Response generated: {ai_response[:100]}...")
        return jsonify({"response": ai_response}), 200
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return jsonify({"error": "Invalid request data"}), 400
    
    except Exception as e:
        logger.error(f"Error processing command: {str(e)}", exc_info=True)
        return jsonify({
            "error": "An error occurred while processing the command",
            "message": "Please try again later"
        }), 500

@app.route('/clear-history', methods=['POST'])
def clear_history():
    """
    Clear the conversation history.
    
    Returns:
    {
        "message": "History cleared successfully"
    }
    """
    try:
        clear_conversation_history()
        logger.info("Conversation history cleared")
        return jsonify({"message": "History cleared successfully"}), 200
    except Exception as e:
        logger.error(f"Error clearing history: {str(e)}")
        return jsonify({"error": "Failed to clear history"}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for monitoring.
    
    Returns:
    {
        "status": "healthy",
        "timestamp": "current timestamp"
    }
    """
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    logger.warning(f"404 error: {request.url}")
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"500 error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Flask application on port {port} (debug={debug})")
    app.run(host='0.0.0.0', port=port, debug=debug)
