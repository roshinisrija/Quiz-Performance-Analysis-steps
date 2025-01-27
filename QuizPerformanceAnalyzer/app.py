from flask import Flask, jsonify

app = Flask(__name__)

# Mock recommendations data
recommendations_data = [
    {"topic": "Biology", "recommendation": "Focus on genetics and molecular biology."},
    {"topic": "Physics", "recommendation": "Revise Newton's laws and practice problem-solving."},
    {"topic": "Chemistry", "recommendation": "Work on organic chemistry and reaction mechanisms."}
]

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """Return recommendations as a JSON response."""
    
    return jsonify(recommendations_data)

if __name__ == '__main__':
    app.run(debug=True)
