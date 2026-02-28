"""
Flask server for deploying the Emotion Detection application.
Exposes a web interface and an API endpoint for emotion analysis.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main HTML page of the application.
    Returns:
        HTML template for user interface.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Route handler for emotion detection requests.

    Returns:
        str: A formatted text response containing emotion scores
        or an error message if input is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    # Handle blank or invalid text
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Normal formatted response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return response_text


if __name__ == "__main__":
    # Run Flask server on port 5000
    app.run(host="0.0.0.0", port=5000)
    