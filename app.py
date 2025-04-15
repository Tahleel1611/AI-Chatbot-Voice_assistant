from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from ai_friend import ask_ai_friend

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process-command', methods=['POST'])
def handle_command():
    try:
        data = request.json
        command = data.get('command')
        if not command:
            return jsonify({"error": "No command provided"}), 400
        ai_response = ask_ai_friend(command)
        return jsonify({"response": ai_response})
    except Exception as e:
        print(f"Error processing command: {e}")
        return jsonify({"error": "An error occurred while processing the command"}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)