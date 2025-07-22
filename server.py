"""Flask server to deploy emotion detection application."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_endpoint():
    """Handle emotion analysis request via GET or POST."""
    if request.method == "GET":
        text = request.args.get("textToAnalyze", "")
    else:
        text = request.json.get("text", "")

    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return jsonify({"result": "Invalid text! Please try again!"})

    response_text = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"result": response_text})


@app.route("/")
def index():
    """Render the main web interface."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
